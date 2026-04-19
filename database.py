from sqlalchemy import create_backend_engine, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Docker Compose'da tanımladığımız bilgilere göre URL oluşturuyoruz
# Not: Host kısmına 'mariadb' (servis adı) yazıyoruz çünkü Docker ağında birbirlerini böyle tanırlar.
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root_password@mariadb:3306/berrinio_auth"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Veritabanı oturumunu yöneten yardımcı fonksiyon (Dependency Injection)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
