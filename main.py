from fastapi import FastAPI
from api.video import router as video_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"]  # You can replace "*" with your allowed origins

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(video_router, prefix="/video", tags=["video"])
