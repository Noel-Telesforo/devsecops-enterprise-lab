# ============================================
# ETAPA 1: Build
# ============================================
FROM python:3.11-slim AS builder

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# ============================================
# ETAPA 2: Producción
# ============================================
FROM python:3.11-slim AS production

WORKDIR /app

# Crear usuario no root
RUN useradd -m -u 1000 appuser

# Copiar dependencias desde la etapa builder
COPY --from=builder /root/.local /home/appuser/.local

# Copiar código de la aplicación
COPY . .

# Ajustar permisos
RUN chown -R appuser:appuser /app
USER appuser

# Variables de entorno
ENV PATH=/home/appuser/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app/main.py
ENV FLASK_ENV=production

# Puerto expuesto
EXPOSE 5000

# Comando de inicio
CMD ["python", "-m", "app.main"]