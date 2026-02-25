from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

from src.database.base import Base
from src.database.connect_db import engine

from src.routes.auth import router as auth_router
from src.routes.setting import router as settings_router
from src.routes.user import router as users_router
from src.routes.skill import router as skills_router

from src.exceptions import register_exception_handlers


app = FastAPI()

@app.on_event("startup")
def startup():
	Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
def shutdown():
	print("App Shutting Down...")
	engine.dispose()

@app.exception_handler(HTTPException)
def http_exception_handler(
	request: Request,
	exception: HTTPException
):
	return JSONResponse(
        status_code=exception.status_code,
        content={
			"success": False,
            "errors": {
				"detail": exception.detail
			}
        }
    )

register_exception_handlers(app)

app.include_router(auth_router, prefix="/api/v1")
app.include_router(settings_router, prefix="/api/v1")
app.include_router(users_router, prefix="/api/v1")
app.include_router(skills_router, prefix="/api/v1")