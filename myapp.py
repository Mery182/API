from fastapi import FastAPI, HTTPException, Query, Response
from typing import Optional, Dict
from pydantic import BaseModel, Field

app = FastAPI()

# Глоссарий
dictionary: Dict[int, Dict] = {
    1: {"term": "Vue.js", "definition": "JavaScript-фреймворк с открытым исходным кодом для создания пользовательских интерфейсов", "priority": 1},
    2: {"term": "Веб-приложение", "definition": "Клиент-серверное приложение, в котором клиент взаимодействует с веб-сервером при помощи браузера.", "priority": 2},
    3: {"term": "JavaScript", "definition": "Mультипарадигменный язык программирования.", "priority": 1},
    4: {"term": "VanillaJS", "definition": "Использование чистого JavaScript без библиотек или фреймворков", "priority": 1},
    5: {"term": "CRUX API", "definition": "Обеспечивает доступ к данным о реальном пользовательском опыте", "priority": 1},
    6: {"term": "Веб-анимация", "definition": "Термин для множества анимаций, используемых в вебе", "priority": 1},
    7: {"term": "W3C", "definition": "World Wide Web Consortium — организация, разрабатывающая стандарты для Интернета", "priority": 1},
    8: {"term": "Google", "definition": "Компания, предоставляющая интернет-сервисы и продукты, такие как поиск, карты и аналитика", "priority": 1},
    9: {"term": "PS", "definition": "Page Speed — метрика производительности страницы", "priority": 2},
    10: {"term": "GPU Used", "definition": "Использование графического процессора (GPU) для рендеринга", "priority": 2},
    11: {"term": "LCP", "definition": "Largest Contentful Paint — время отображения самого большого элемента", "priority": 1},
    12: {"term": "Core Web Vitals", "definition": "Набор ключевых метрик для оценки производительности страниц", "priority": 1},
    13: {"term": "UX", "definition": "User Experience — пользовательский опыт", "priority": 1},
    14: {"term": "MDN Web Docs", "definition": "Документация для веб-разработчиков", "priority": 1},
    15: {"term": "FPS", "definition": "Frames Per Second — частота кадров в секунду", "priority": 1},
    16: {"term": "INP", "definition": "Interaction to Next Paint — метрика задержки взаимодействия", "priority": 2},
    17: {"term": "Total Blocking Time (TBT)", "definition": "Общее время блокировки между загрузкой и интерактивностью", "priority": 1},
    18: {"term": "Time to Interactive (TTI)", "definition": "Время до интерактивности страницы", "priority": 1},
    19: {"term": "Cumulative Layout Shift (CLS)", "definition": "Метрика, показывающая визуальную стабильность страницы", "priority": 1},
    20: {"term": "Google Chrome DevTools", "definition": "Инструменты разработчика в браузере Google Chrome", "priority": 1},
    21: {"term": "WebPageTest", "definition": "Инструмент тестирования производительности страниц", "priority": 1},
    22: {"term": "stats.js", "definition": "Библиотека для отслеживания производительности JavaScript", "priority": 2},
    23: {"term": "GSAP", "definition": "GreenSock Animation Platform — библиотека для сложных анимаций", "priority": 1},
    24: {"term": "Anime.js", "definition": "JavaScript-библиотека для создания анимаций", "priority": 1},
}

# Pydantic модель для термина
class Term(BaseModel):
    term: str
    definition: str
    priority: int
    relation: Optional[int] = None
    author: Optional[str] = "mery182"

# Эндпоинт для получения всех терминов
@app.get("/terms", response_model=Dict[int, Term])
async def get_all_terms(response: Response):
    add_cors_headers(response)
    return dictionary

# Эндпоинт для графа
@app.get("/graph", response_model=dict)
async def get_graph(response: Response):
    add_cors_headers(response)
    nodes = [{"id": key, "label": term["term"], "definition": term["definition"]} for key, term in dictionary.items()]
    
    # Создаем связи (edges) для терминов
    edges = [
        {"from_node": 1, "to_node": 3, "relation": "depends_on"}, #зависит от
        {"from_node": 4, "to_node": 3, "relation": "extends"}, #расширяется
        {"from_node": 2, "to_node": 1, "relation": "uses"}, #использует
        {"from_node": 3, "to_node": 5, "relation": "integrates"}, #интегрирует
        {"from_node": 12, "to_node": 11, "relation": "includes"}, 
        {"from_node": 13, "to_node": 12, "relation": "enhances"}, #enhances
        {"from_node": 8, "to_node": 7, "relation": "follows_standards"},
        {"from_node": 15, "to_node": 22, "relation": "measures"},
        {"from_node": 23, "to_node": 6, "relation": "supports"},
        {"from_node": 24, "to_node": 6, "relation": "supports"},
        {"from_node": 10, "to_node": 6, "relation": "accelerates"}, # Ускоряет
        {"from_node": 21, "to_node": 12, "relation": "tests"},
        {"from_node": 20, "to_node": 18, "relation": "analyzes"},
                {"from_node": 20, "to_node": 9, "relation": "analyzes"},
         {"from_node": 20, "to_node": 17, "relation": "analyzes"},
            {"from_node": 20, "to_node": 19, "relation": "analyzes"},
             {"from_node": 20, "to_node": 16, "relation": "analyzes"},
    {"from_node": 20, "to_node": 10, "relation": "analyzes"},
        {"from_node": 16, "to_node": 9, "relation": "relates_to"},
        {"from_node": 16, "to_node": 17, "relation": "influences"},
  
    ]

    return {"nodes": nodes, "edges": edges}

# Добавление CORS заголовков
def add_cors_headers(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"

# Preflight-запросы
@app.options("/{path:path}")
async def preflight_handler(response: Response):
    add_cors_headers(response)
    return Response(status_code=204)