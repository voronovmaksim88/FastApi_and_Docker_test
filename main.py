from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!!!!"}

# для автоматического перезапуска приложения при изменении кода
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
