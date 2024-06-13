from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import  models, schemas,crud
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
def get_db():
       db = SessionLocal()
       try:
           yield db
       finally:
           db.close()


@app.post("/create_configuration/", response_model=schemas.CountryConfigurationCreate)
def create_configuration(config: schemas.CountryConfigurationCreate, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code=config.country_code)
    if db_config:
        raise HTTPException(status_code=400, detail="Configuration already exists")
    return crud.create_configuration(db=db, config=config)


@app.get("/get_configuration/{country_code}", response_model=schemas.CountryConfiguration)
def get_configuration(country_code: str, db: Session = Depends(get_db)):
    print(f"Get configuration called for country_code: {country_code}")
    db_config = crud.get_configuration(db, country_code=country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config

@app.post("/update_configuration/", response_model=schemas.CountryConfiguration)
def update_configuration(config: schemas.CountryConfigurationUpdate, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code=config.country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return crud.update_configuration(db=db, country_code=config.country_code, config=config)

@app.delete("/delete_configuration/", response_model=bool)
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    success = crud.delete_configuration(db, country_code=country_code)
    if not success:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return success
