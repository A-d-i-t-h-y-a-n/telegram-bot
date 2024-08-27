# Hermit Telegram Bot

A Telegram bot built using Python and the Telethon library.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/A-d-i-t-h-y-a-n/telegram-bot.git
    cd telegram-bot
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Copy the example environment file and edit it:

    ```bash
    cp .env.example .env
    ```

    Open `.env` and add your API credentials. To get your `API_ID` and `API_HASH`, follow these steps:

    - Go to [my.telegram.org](https://my.telegram.org).
    - Log in with your Telegram account.
    - Go to the "API development tools" section.
    - Create a new application to get your API ID and Hash.

    ```env
    API_ID=your_api_id
    API_HASH=your_api_hash
    BOT_TOKEN=your_bot_token
    ```

## Usage

Run the bot with:

```bash
python3 bot.py
