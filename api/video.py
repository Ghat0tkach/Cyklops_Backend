import shutil
import os
from fastapi import APIRouter, File, UploadFile, HTTPException
from scenedetect_utils import find_scenes, extract_frames, upload_frames_to_github
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve GitHub token and repo from environment variables


router = APIRouter()

@router.post("/detect-scenes/")
async def detect_scenes(video: UploadFile):
    try:
        threshold: float = 27.0
        github_token = os.getenv("GITHUB_TOKEN")
        github_repo = os.getenv("GITHUB_REPO")
        # Get the frame numbers
        frames_to_extract = find_scenes(video, threshold=threshold)

        # Extract frames and upload to GitHub
        output_directory = extract_frames("temp_video.mp4", frames_to_extract)
        upload_frames_to_github(output_directory, github_token, github_repo)

        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Optionally, you can delete the temporary file after processing
    
        os.remove("temp_video.mp4")
        return {"message": "Frames extracted and uploaded to GitHub", "output_directory": output_directory, "frame_count": len(frames_to_extract)}

def delete_temp_files_folder(temp_folder):
    if os.path.exists(temp_folder):
        shutil.rmtree(temp_folder)
        print(f"Temporary files folder '{temp_folder}' deleted.")
