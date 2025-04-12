# Базовый образ
FROM python:3.11-slim

# 1. Установка системных зависимостей (только то, что нужно для ваших pip-пакетов)
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

# 2. Рабочая директория (может быть любой)
WORKDIR /app

# 3. Копируем зависимости
COPY requirements.txt .

# 4. Устанавливаем Python-пакеты
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копируем весь проект
COPY . .

# 6. Команда для запуска
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]