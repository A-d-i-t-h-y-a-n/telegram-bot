import os
import asyncio
import importlib
import sys
from pathlib import Path
from telethon import TelegramClient, events
from loguru import logger
from config import API_ID, API_HASH, BOT_TOKEN
import builtins 

logger.remove()
logger.add(sys.stdout, level="INFO", format="<green>{time:DD-MM-YY HH:mm}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>")


bot = TelegramClient('bot', API_ID, API_HASH)

builtins.bot = bot

async def log_incoming_messages(event):
    logger.info(f"Message [{event.sender_id}]: {event.text}")

async def log_error(event, error):
    logger.error(f"Error handling event {event}: {error}")

def load_plugins(plugin_name):
    path = Path(f"plugins/{plugin_name}.py")
    name = f"plugins.{plugin_name}"
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logger.bind(plugin=plugin_name)
    spec.loader.exec_module(load)
    sys.modules[name] = load
    logger.info(f"Loaded plugin: {plugin_name}")

def load_all_plugins():
    plugin_dir = Path('plugins')
    for filename in plugin_dir.glob('*.py'):
        plugin_name = filename.stem
        load_plugins(plugin_name)

async def main():
    logger.info("Starting bot...")
    await bot.start(bot_token=BOT_TOKEN)
    logger.info("Bot started.")
    
    load_all_plugins()
    logger.info("Plugins loaded.")

    @bot.on(events.NewMessage)
    async def handler(event):
        try:
            await log_incoming_messages(event)
        except Exception as e:
            await log_error(event, e)

    logger.info("Bot is running...")
    await bot.run_until_disconnected()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped manually.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
