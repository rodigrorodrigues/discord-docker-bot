from os import getenv
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv('DISCORD_TOKEN')
DOCKER_IMAGE = getenv('DOCKER_IMAGE')
DOCKER_CONTAINER_NAME = getenv('DOCKER_CONTAINER_NAME')