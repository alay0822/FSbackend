from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Use SQLite for local or change to your PostgreSQL URL
DATABASE_URL = "sqlite:///./tasks.db"
# DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
