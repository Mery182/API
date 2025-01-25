# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /API

# Копируем файл requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем виртуальное окружение
RUN python -m venv /venv

# Устанавливаем зависимости в виртуальное окружение
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

# Копируем файлы проекта в контейнер
COPY . .

# Открываем порт 8000 для приложения
EXPOSE 8000

# Команда для запуска FastAPI с Uvicorn
CMD ["/venv/bin/uvicorn", "myapp:app", "--host", "0.0.0.0", "--port", "8000"]