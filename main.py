from fastapi import FastAPI

app = FastAPI(
    title="Berrinio Auth Service",
    description="Kullanıcı kimlik doğrulama ve yönetim servisi",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Berrinio Auth Service çalışıyor! 🚀"}

@app.get("/health")
def health_check():
    return {
        "status": "healthy", 
        "database": "bağlantı bekleniyor..." 
    }
