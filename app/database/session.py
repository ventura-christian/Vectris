from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "")

# This tells me where the database is located
engine = create_engine(DATABASE_URL)

# This allows a connection to be opened
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This is the class the models will inherit from
Base = declarative_base()


# This function provides a database session to any route that needs one.
def get_db():
    db = SessionLocal()
    try:
        yield db
    # Always close the request is done.
    finally:
        db.close()
