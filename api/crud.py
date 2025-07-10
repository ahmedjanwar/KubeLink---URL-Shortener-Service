import random
import string
from sqlalchemy.orm import Session
import models

def create_short_url(db: Session, url: str):
    short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    db_url = models.URL(original_url=url, short_code=short_code)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_url_by_code(db: Session, short_code: str):
    return db.query(models.URL).filter(models.URL.short_code == short_code).first()
