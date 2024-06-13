from pydantic import BaseModel
from typing import Dict, Any

class CountryConfigurationBase(BaseModel):
    country_code: str
    configuration: Dict[str, Any]


class CountryConfigurationCreate(CountryConfigurationBase):
    pass

class CountryConfigurationUpdate(CountryConfigurationBase):
    pass

class CountryCode(BaseModel):
    country_code: str
    
class CountryConfiguration(CountryConfigurationBase):
    id: int

    class Config:
        orm_mode = True
