# Указываем базовый образ
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы requirements.txt и main.py в образ
COPY requirements.txt ./
COPY main.py ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем команду для запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# команда для сборки
# docker build -t fastapi-app .

# команда для запуска
# docker run -p 8000:8000 fastapi-app