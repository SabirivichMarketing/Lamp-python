FROM python:3.11-slim

WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Копирование requirements и установка Python пакетов
COPY bot/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода бота
COPY bot/ .

# Создание пользователя для безопасности
RUN useradd -m -u 1000 botuser
USER botuser

CMD ["python", "bot.py"]