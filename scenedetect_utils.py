from scenedetect import SceneManager, open_video, ContentDetector
import cv2
import os
import base64
from github import Github
import uuid
def find_scenes(file, threshold=27.0):
    with open("temp_video.mp4", "wb") as video_file:
        video_file.write(file.file.read())

    video = open_video("temp_video.mp4")
    scene_manager = SceneManager()
    scene_manager.add_detector(ContentDetector(threshold=threshold))
    scene_manager.detect_scenes(video)

    # Get the scene list
    scene_list = scene_manager.get_scene_list()

    # Extract unique frame numbers from the scene list
    frame_numbers_set = set(frame.frame_num for scene in scene_list for frame in scene)

    # Convert the set back to a sorted list if needed
    frame_numbers = sorted(list(frame_numbers_set))

    return frame_numbers

def extract_frames(video_file_path, frame_numbers):
    frames_folder_uuid = str(uuid.uuid4())  # Generate UUID
    frames_folder = f"frames_temp_{frames_folder_uuid}"
    os.makedirs(frames_folder, exist_ok=True)
    os.makedirs(frames_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_file_path)
    
    frame_index = 0  # Initialize frame index

    for frame_num in frame_numbers:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        ret, frame = cap.read()

        if ret:
            output_path = f"{frames_folder}/frame_{frame_index}.jpg"
            cv2.imwrite(output_path, frame)
            frame_index += 1  # Increment frame index
        else:
            print(f"Error reading frame {frame_num}")

    cap.release()

    return frames_folder

def upload_frames_to_github(frames_folder, github_token, github_repo):
    g = Github(github_token)
    repo = g.get_repo(github_repo)

    for frame in os.listdir(frames_folder):
        frame_path = os.path.join(frames_folder, frame)
        upload_image_to_github(repo, frame_path, frame, frames_folder)

def upload_image_to_github(repo, image_path, image_filename, folder_name):
    try:
        with open(image_path, "rb") as image_file:
            image_content = image_file.read()
            content_base64 = base64.b64encode(image_content).decode("utf-8")

        repo.create_file(f"{folder_name}/{image_filename}", f"Added {image_filename}", content_base64, branch="main")
    except Exception as e:
        print(f"Error uploading {image_filename} to GitHub: {str(e)}")
