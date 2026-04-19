from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from database import engine, get_db

# Tabloları veritabanında oluştur (Migration aracı kullanana kadar en basit yol)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Berrinio Auth Service")

@app.get("/")
def read_root():
    return {"message": "Berrinio Auth Service MariaDB'ye bağlandı! 🟡🔴"}

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    # Veritabanına basit bir sorgu atarak bağlantıyı doğrula
    try:
        db.execute("SELECT 1")
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "error", "database": str(e)}
