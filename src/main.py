import os
import discord
from discord.ext import commands
from config.config import TOKEN, DOCKER_IMAGE, DOCKER_CONTAINER_NAME
from services.docker_service import DockerService

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
docker_service = DockerService()

@bot.event
async def on_ready():
    print(f'{bot.user} is online!')

@bot.command(name='start')
async def start(ctx):
    await ctx.send('Starting container...')
    if docker_service.start_container(DOCKER_IMAGE, DOCKER_CONTAINER_NAME):
        await ctx.send(f'Container {DOCKER_CONTAINER_NAME} started successfully!')
    else:
        await ctx.send('Error starting container')

@bot.command(name='stop')
async def stop(ctx):
    await ctx.send('Stopping container...')
    if docker_service.stop_container(DOCKER_CONTAINER_NAME):
        await ctx.send(f'Container {DOCKER_CONTAINER_NAME} stopped successfully!')
    else:
        await ctx.send('Error stopping container')

if __name__ == '__main__':
    bot.run(TOKEN)