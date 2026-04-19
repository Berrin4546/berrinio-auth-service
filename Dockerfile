# Resmi ve hafif Python 3.11 imajını kullan
FROM python:3.11-slim

# Konteyner içindeki çalışma dizinini ayarla
WORKDIR /app

# Önce sadece requirements.txt dosyasını kopyala (Docker cache optimizasyonu için)
COPY requirements.txt .

# Kütüphaneleri kur
RUN pip install --no-cache-dir -r requirements.txt

# Şimdi tüm proje kodlarını kopyala
COPY . .

# FastAPI'nin dışarıya açılacağı port
EXPOSE 8000

# Uygulamayı başlatma komutu
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
