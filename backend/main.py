from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.voice_api import router as voice_router

app = FastAPI(title="AI Voice Detection System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(voice_router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "Backend is running"}
