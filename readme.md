# Проект FastAPI Dictionary

Этот проект представляет собой **приложение-словарь**, созданное с использованием **FastAPI** для backend и **Vue.js** для frontend. Оно предоставляет платформу для хранения, поиска и управления терминами с их определениями и взаимосвязями.

---

## Особенности

### Backend (FastAPI)
- API для управления словарём терминов.
- Семантическое представление графа терминов с узлами и связями.
- Встроенные эндпоинты для:
  - Получения всех терминов.
  - Поиска терминов по ключевому слову.
  - Добавления, обновления и удаления терминов.
  - Представления терминов и их взаимосвязей в виде графа.
- Основано на **FastAPI** и **Uvicorn** для асинхронной работы.

### Frontend (Vue.js)
- Интерактивный пользовательский интерфейс для просмотра и управления терминами.
- Визуализация семантических графов с использованием **vis-network**.
- Стилизация с помощью **TailwindCSS** для чистого и адаптивного дизайна.

---

## Технологии

- **Backend**: FastAPI, Python 3.9
- **Frontend**: Vue 3, Vite, TailwindCSS
- **Визуализация**: vis-network
- **Docker**: Для контейнерной разработки

---

## Предварительные требования

Убедитесь, что у вас установлены:
- **Docker** и **Docker Compose**
- **Python 3.9** (если проект запускается локально)
- **Node.js** (для локальной разработки frontend)

---

## Установка

### Клонирование репозитория
```bash
git clone https://github.com/YourUsername/fastapi-dictionary.git
cd fastapi-dictionary
```

### Установка с использованием Docker
1. Соберите и запустите контейнеры:
   ```bash
   docker-compose up --build
   ```

2. Доступ к приложению:
   - **Frontend**: [http://localhost:8080](http://localhost:8080)
   - **Backend**: [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI для документации API)

---

## Локальная разработка

### Backend
1. Перейдите в папку с backend:
   ```bash
   cd venv
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Запустите приложение FastAPI:
   ```bash
   uvicorn myapp:app --reload
   ```

4. Backend будет доступен по адресу [http://localhost:8000](http://localhost:8000).

### Frontend
1. Перейдите в папку с frontend:
   ```bash
   cd frontend-vue
   ```

2. Установите зависимости:
   ```bash
   npm install
   ```

3. Запустите сервер разработки Vue.js:
   ```bash
   npm run dev
   ```

4. Frontend будет доступен по адресу [http://localhost:4173](http://localhost:4173).



## Автор
Разработано [Mery182](https://github.com/Mery182).
