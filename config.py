import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_HOSTNAME = os.getenv("GITHUB_HOSTNAME")

BASE_URL = os.getenv("BASE_URL")
ENDPOINT = os.getenv("ENDPOINT")