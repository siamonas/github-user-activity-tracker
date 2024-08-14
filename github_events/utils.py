import os
from dotenv import load_dotenv

def load_env_variables():
    load_dotenv()
    return os.getenv("GITHUB_TOKEN")