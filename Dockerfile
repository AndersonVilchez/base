FROM python:3.9-slim

# Instala dependencias del sistema necesarias para pillow
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    libfreetype6-dev \
    zlib1g-dev \
    && apt-get clean

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto
COPY . /app

# Instala dependencias de Python
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Ejecuta la aplicación Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.headless=true"]
