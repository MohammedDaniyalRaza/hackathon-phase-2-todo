from sqlmodel import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/todo_db")

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)