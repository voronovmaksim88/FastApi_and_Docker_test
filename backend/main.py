from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=[
         "http://localhost:5173",
         "http://176.124.213.202",
        ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello, World from SibPLC !"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
