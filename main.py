from fastapi import FastAPI
from api.video import router as video_router

app = FastAPI()

app.include_router(video_router, prefix="/video", tags=["video"])
