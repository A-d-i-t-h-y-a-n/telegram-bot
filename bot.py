import os
import asyncio
import logging
import importlib
import sys
from pathlib import Path
from telethon import TelegramClient
import builtins
from config import API_ID, API_HASH, BOT_TOKEN

bot = TelegramClient('bot', API_ID, API_HASH)

builtins.bot = bot

def load_plugins(plugin_name):
    path = Path(f"plugins/{plugin_name}.py")
    name = f"plugins.{plugin_name}"
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules[name] = load
    print(f"TelethonBot has Imported {plugin_name}")

def load_all_plugins():
    plugin_dir = Path('plugins')
    for filename in plugin_dir.glob('*.py'):
        plugin_name = filename.stem
        load_plugins(plugin_name)

async def main():
    print("Starting bot...")
    await bot.start(bot_token=BOT_TOKEN)
    load_all_plugins()
    print("Bot is running...")
    await bot.run_until_disconnected()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped manually.")
