from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

