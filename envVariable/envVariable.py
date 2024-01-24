# Todo: Import Libraries
import os
from dotenv import load_dotenv

# Todo: load dotenv
load_dotenv()  # take environment variables from .env.


# Todo: Access the Keys
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

print(OPENAI_API_KEY)