from pydantic import BaseModel
from datetime import date
class StockSchema(BaseModel):
    id: int
    name: str
    ticker: str    
    sector =str
    open =float
    high = float
    low = float
    current_price = float
    change = float
    volume = float
    beta = float
    shariah_status = str
    risk_level = str
    timestamp = date

    class config:
        orm_mode = True

