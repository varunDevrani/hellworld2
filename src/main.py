from fastapi import FastAPI

from src.routes.auth import router as auth_router
from src.routes.settings import router as settings_router
from src.routes.users import router as users_router
from src.routes.skills import router as skills_router

app = FastAPI()


app.include_router(auth_router, prefix="/api/v1")
app.include_router(settings_router, prefix="/api/v1")
app.include_router(users_router, prefix="/api/v1")
app.include_router(skills_router, prefix="/api/v1")