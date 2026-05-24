"""
GoldenSeeker — Database Connection
-----------------------------------
This file handles everything related to connecting
to our PostgreSQL database. Every other file that
needs database access imports from here.
"""

import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from loguru import logger

# Load all variables from our .env file into memory
# After this line, os.getenv() can read DB_NAME, DB_USER etc.
load_dotenv()

# Read each database credential from .env file
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# Build the connection string
# This is the address SQLAlchemy uses to find your database
# Format: postgresql://username:password@host:port/database_name
DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Create the engine
# The engine is the core of SQLAlchemy — it manages
# the actual connection to PostgreSQL
# pool_pre_ping=True means it checks the connection
# is alive before using it
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=False  # Set to True if you want to see every SQL query printed
)

# Create a session factory
# A session is like a conversation with your database
# You open a session, do some work, then close it
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create a base class for your database table definitions
# Every table you create will inherit from this Base
Base = declarative_base()


def get_db():
    """
    Creates a database session and automatically closes
    it when you are done — even if an error occurs.

    Use this function whenever you need to talk to the database.

    Example:
        db = next(get_db())
        results = db.execute(text("SELECT * FROM jobs"))
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_connection():
    """
    Tests that your database connection is working.
    Run this file directly to verify your setup.

    Returns True if connection works, False if it fails.
    """
    try:
        # Try to connect and run a simple query
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version()"))
            version = result.fetchone()[0]
            logger.success(f"Connected to database successfully")
            logger.info(f"PostgreSQL version: {version}")
            return True
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        logger.error("Check your .env file credentials")
        return False


# This block only runs when you execute this file directly
# It will NOT run when other files import from this file
if __name__ == "__main__":
    logger.info("Testing database connection...")
    test_connection()