from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=[
         "http://176.124.213.202",
        ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    """Домашняя страница"""
    html_content = "<h2>FastAPI is the best backend framework 16-09-2024 </h2>"
    html_content = "<h2>правочки на сайте github </h2>"
    html_content += '<p>Интерактивная документация на <a href="/docs">/docs</a></p>'
    return HTMLResponse(content=html_content)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
