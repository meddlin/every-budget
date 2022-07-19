from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = "postgres"
password = "postgres"
host = "localhost"
port = "5432"
database = "everybudget_db"

engine = create_engine(
    f'postgresql://{user}:{password}@{host}:{port}/{database}'
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
metadata = MetaData()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close() 