from sqlalchemy import Column, String, Integer, JSON
from database import Base

class CountryConfiguration(Base):
    __tablename__ = "country_configurations"
    id = Column(Integer, primary_key=True, index=True)
    country_code = Column(String, unique=True, index=True)
    configuration = Column(JSON)