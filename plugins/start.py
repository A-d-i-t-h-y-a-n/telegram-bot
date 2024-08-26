from telethon import events
from telethon.tl.custom import Button

@bot.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    buttons = [
        [Button.inline("Source Bot", b'source_bot')]
    ]
    await event.respond(
        "Welcome to Hermit! Click the button below to get the source bot.",
        buttons=buttons
    )

@bot.on(events.CallbackQuery(data=b'source_bot'))
async def callback_handler(event):
    buttons = [
        [Button.inline("Back", b'home')]
    ]
    await event.edit(
        "Here's the source bot: [Source Code](https://github.com/A-d-i-t-h-y-a-n/telegram-bot)",
        buttons=buttons
    )

@bot.on(events.CallbackQuery(data=b'home'))
async def back_handler(event):
    buttons = [
        [Button.inline("Source Bot", b'source_bot')]
    ]
    await event.edit(
        "Welcome to Hermit! Click the button below to get the source bot.",
        buttons=buttons
    )
