import shutil
import os
from fastapi import APIRouter, File, UploadFile, HTTPException
from scenedetect_utils import find_scenes, extract_frames, upload_frames_to_github
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve GitHub token and repo from environment variables
github_token = os.getenv("GITHUB_TOKEN")
github_repo = os.getenv("GITHUB_REPO")

router = APIRouter()

@router.post("/detect-scenes/")
async def detect_scenes(file: UploadFile = File(...), threshold: float = 27.0):
    try:
        # Get the frame numbers
        frames_to_extract = find_scenes(file, threshold=threshold)

        # Extract frames and upload to GitHub
        output_directory = extract_frames("temp_video.mp4", frames_to_extract)
        upload_frames_to_github(output_directory, github_token , github_repo)

        return {"message": "Frames extracted and uploaded to GitHub", "output_directory": output_directory}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Optionally, you can delete the temporary file after processing
        delete_temp_files_folder()
        os.remove("temp_video.mp4")

def delete_temp_files_folder():
    temp_folder = "temp_videos"
    if os.path.exists(temp_folder):
        shutil.rmtree(temp_folder)
        print(f"Temporary files folder '{temp_folder}' deleted.")

# Function to delete files uploaded to GitHub
@router.post("/delete-github-files/")
async def delete_github_files(github_token: str, github_repo: str):
    try:
        # Your logic to delete files from GitHub goes here
        # You may use the PyGitHub library or GitHub API for this task

        return {"message": "GitHub files deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))