# Cyklops: Video/Image to Text Conversational Agent

Cyklops is an intelligent conversational agent that provides video/image-to-text capabilities. It utilizes the FastAPI framework along with the open-source LLaVA model for efficient image-to-caption processing.For Frontend , visit [Cyklops_Fronted Repo](https://github.com/Ghat0tkach/Cyklops_Frontend)


## Demo Video
https://github.com/Ghat0tkach/Cyklops_Frontend/assets/59855919/5c11b75a-3a59-40e9-850d-6991a0b8166d



## Running Using Docker

```bash
docker build --build-arg ENV_FILE=.env -t your_image_name .
```

Make sure to add all env keys

## Setup

### 1. Requirements Installation

```bash
pip install -r requirements.txt
```

### 2. Environment Variables

Create an `.env` file with the following variables:

```bash
GITHUB_REPO = "username/repo"  # Replace with your GitHub username and repository name
GITHUB_TOKEN = "github_personal_access_token"  # Replace with your GitHub personal access token
GOOGLE_API_KEY = "google_gemini_api_key"  # Replace with your Google Gemini API key
```

### 3. Run this Server

```bash
python -m uvicorn main:app --reload
```

`By default , the API documentation will be available at localhost:8000/docs`

### Overview

Cyklops processes images using the LLaVA model and requires a cloud storage solution to temporarily store images during the processing phase. This README provides details on using GitHub as the cloud storage.Using Intelligent frames cutting using scenedetect , Cyklops provides a way to interact with videos as well.

### GitHub Setup

1. # Create a Repository:

   - Create a new GitHub repository where processed images will be stored.

2. # Generate Personal Access Token::

   - Generate a GitHub personal access token with the necessary permissions to read and write to the repository. Set this token as GITHUB_TOKEN in the .env file.

3. # Configure Environment Variables::
   - Set GITHUB_REPO in the .env file to match your GitHub username and repository name.

### Google API Key

Obtain a Google Gemini API key and set it as GOOGLE_API_KEY in the `.env` file.

### Running the Server

After completing the setup steps, run the FastAPI server using the provided command. The server will be accessible, and you can begin utilizing Cyklops for video/image-to-text conversations.

Feel free to customize the configuration based on your specific needs and requirements. For any assistance or issues, refer to the documentation or raise a issue for support.

Proudly Open-Source
