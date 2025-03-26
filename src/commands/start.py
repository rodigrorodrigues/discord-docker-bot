from services.docker_service import DockerService
from config.config import Config

async def start_container(ctx):
    docker_service = DockerService()
    result = docker_service.start_container(Config.DOCKER_IMAGE, Config.DOCKER_CONTAINER_NAME)
    if result:
        await ctx.send(f"Container {Config.DOCKER_CONTAINER_NAME} iniciado com sucesso!")
    else:
        await ctx.send("Erro ao iniciar o container")