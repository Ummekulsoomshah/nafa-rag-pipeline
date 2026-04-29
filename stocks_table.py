import os

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5433")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")          
DB_NAME = os.getenv("DB_NAME", "nafaDb")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
Base=declarative_base()

class Stock(Base):
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    symbol = Column(String,index=True)
    sector = Column(String,index=True)
    open = Column(Integer)
    high = Column(Integer)
    low = Column(Integer)
    current_price = Column(Integer)
    change = Column(Integer)
    volume = Column(Integer)
    beta = Column(Integer)
    shariah_status = Column(String)
    risk_level = Column(String,index=True)
    timestamp = Column(String)


Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()