from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import time
import pymysql

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://appuser:apppassword@db:3306/contactbook")

# Add retry logic
max_retries = 30  # Try for 30 seconds
retry_interval = 1  # Wait 1 second between retries

# Try to connect to the database with retries
for i in range(max_retries):
    try:
        # Test connection
        conn = pymysql.connect(
            host="db",
            user=os.getenv("MYSQL_USER", "appuser"),
            password=os.getenv("MYSQL_PASSWORD", "apppassword"),
            connect_timeout=5
        )
        conn.close()
        break
    except pymysql.err.OperationalError as e:
        if i < max_retries - 1:
            print(f"Database connection failed. Retrying in {retry_interval} seconds... ({i+1}/{max_retries})")
            time.sleep(retry_interval)
        else:
            print("Failed to connect to the database after multiple attempts.")
            raise

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
