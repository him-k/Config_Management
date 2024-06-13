from sqlalchemy.orm import Session
from models import CountryConfiguration
from schemas import CountryConfigurationCreate, CountryConfigurationUpdate

def get_configuration(db: Session, country_code: str):
    return db.query(CountryConfiguration).filter(CountryConfiguration.country_code == country_code).first()

def create_configuration(db: Session, config: CountryConfigurationCreate):
    db_config = CountryConfiguration(**config.dict())
    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    return db_config

def update_configuration(db: Session, country_code: str, config: CountryConfigurationUpdate):
    db_config = get_configuration(db, country_code)
    if db_config:
        for key, value in config.dict().items():
            setattr(db_config, key, value)
        db.commit()
        db.refresh(db_config)
        return db_config
    return None

def delete_configuration(db: Session, country_code: str):
    db_config = get_configuration(db, country_code)
    if db_config:
        db.delete(db_config)
        db.commit()
        return True
    return False
