from fastapi import FastAPI
from .routes import router as NoteRouter

app = FastAPI()


@app.get("/", tags=["Deploy FastAPI to Vercel"])
async def root() -> dict:
    return {
        "message": "Welcome to my notes application, use the /docs route to proceed"
    }


app.include_router(NoteRouter, prefix="/note")
