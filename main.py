from fastapi import FastAPI
from api.video import router as video_router
from api.chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"] 

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def docs():
    return ["For Documentation visit /docs"]
app.include_router(video_router, prefix="/video", tags=["video"])
app.include_router(chat_router, prefix="/chat", tags=["chat"])
