# Create a environment file
- Create a .env file, Here you will save all your credentials.

# Install the dotenv python package
- pip install python-dotenv

# Import Libraries
- import os
- from dotenv import load_dotenv

# load dotenv
- load_dotenv()  , this takes environment variables from .env.

# Access the Keys
- access_key = os.getenv('access_key')
- OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')