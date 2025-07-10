import time
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from sqlalchemy.exc import OperationalError

from database import SessionLocal, engine, Base
import models, schemas, crud

app = FastAPI()

# Retry logic to wait for DB connection and create tables
MAX_RETRIES = 10
RETRY_DELAY = 3  # seconds

for i in range(MAX_RETRIES):
    try:
        Base.metadata.create_all(bind=engine)
        print("Database connected and tables created")
        break
    except OperationalError:
        print(f"Database not ready, retrying in {RETRY_DELAY}s...")
        time.sleep(RETRY_DELAY)
else:
    print("Failed to connect to the database after several retries")
    raise RuntimeError("Could not connect to the database")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/shorten")
def shorten_url(request: schemas.URLCreate, db: Session = Depends(get_db)):
    db_url = crud.create_short_url(db, request.url)
    return {"short_code": db_url.short_code}


@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    db_url = crud.get_url_by_code(db, short_code)
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(db_url.original_url)
