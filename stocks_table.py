from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:postgres@localhost:5433/nafaDb')
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