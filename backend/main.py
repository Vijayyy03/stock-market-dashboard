from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, func
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from typing import List

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "sqlite:///./stocks.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    stock_prices = relationship("StockPrice", back_populates="company")

class StockPrice(Base):
    __tablename__ = "stock_prices"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    date = Column(String)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Integer)
    company = relationship("Company", back_populates="stock_prices")

# Pydantic schemas
from pydantic import BaseModel

class CompanyOut(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class StockPriceOut(BaseModel):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    class Config:
        orm_mode = True

class AnalyticsOut(BaseModel):
    high_52week: float
    low_52week: float
    avg_volume: float

    class Config:
        orm_mode = True

@app.get("/companies", response_model=List[CompanyOut])
def get_companies():
    db = SessionLocal()
    companies = db.query(Company).all()
    db.close()
    return companies

@app.get("/stocks/{company_id}", response_model=List[StockPriceOut])
def get_stock_prices(company_id: int):
    db = SessionLocal()
    prices = db.query(StockPrice).filter(StockPrice.company_id == company_id).all()
    db.close()
    if not prices:
        raise HTTPException(status_code=404, detail="No stock prices found for this company.")
    return prices

@app.get("/analytics/{company_id}", response_model=AnalyticsOut)
def get_analytics(company_id: int):
    db = SessionLocal()
    prices = db.query(StockPrice).filter(StockPrice.company_id == company_id).all()
    db.close()
    if not prices:
        raise HTTPException(status_code=404, detail="No stock prices found for this company.")
    closes = [p.close for p in prices]
    volumes = [p.volume for p in prices]
    return AnalyticsOut(
        high_52week=max(closes),
        low_52week=min(closes),
        avg_volume=sum(volumes) / len(volumes) if volumes else 0
    )

@app.get("/")
def read_root():
    return {"message": "Backend is running!"} 