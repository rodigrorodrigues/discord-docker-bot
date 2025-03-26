from services.docker_service import DockerService
from config.config import Config

async def stop_container(ctx):
    docker_service = DockerService()
    result = docker_service.stop_container(Config.DOCKER_CONTAINER_NAME)
    if result:
        await ctx.send(f"Container {Config.DOCKER_CONTAINER_NAME} parado com sucesso!")
    else:
        await ctx.send("Erro ao parar o container")