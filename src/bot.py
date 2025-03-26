import discord
from discord.ext import commands
from config.config import TOKEN
from commands.start import start_container
from commands.stop import stop_container
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='start')
async def start(ctx):
    try:
        await start_container(ctx)
    except Exception as e:
        logger.error(f"Error executing start command: {e}")
        await ctx.send("An error occurred while starting the container")

@bot.command(name='stop')
async def stop(ctx):
    try:
        await stop_container(ctx)
    except Exception as e:
        logger.error(f"Error executing stop command: {e}")
        await ctx.send("An error occurred while stopping the container")

@bot.event
async def on_ready():
    logger.info(f'Bot {bot.user.name} is online!')
    logger.info(f'Bot ID: {bot.user.id}')
    logger.info(f'Connected to {len(bot.guilds)} servers')

@bot.event
async def on_error(event, *args, **kwargs):
    logger.error(f"Error in event {event}: {args[0]}")

if __name__ == '__main__':
    try:
        logger.info("Starting bot...")
        if not TOKEN:
            raise ValueError("Token not found! Check your .env file")
        bot.run(TOKEN)
    except Exception as e:
        logger.error(f"Error starting bot: {e}")