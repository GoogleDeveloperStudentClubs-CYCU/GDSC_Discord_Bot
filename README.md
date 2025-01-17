Copyright (C) 2024 Chung Yuan Christian University,Taiwan. X Google Developer Groups On Campus
Copyright (C) 2024 Google Developer Groups On Campus Taiwan.

# GDG On Campus CYCU Discord Bot

## Installation

```bash
git clone https://github.com/GoogleDeveloperStudentClubs-CYCU/GDSC_Discord_Bot
cd GDSC_Discord_Bot
pip install -r requirements.txt
```

## Usage

1. Create `secrets.json` file in the root directory.
2. Fill in the `secrets.json` file with the following content

```json
{
    "discord_bot_token": "YOUR_DISCORD_BOT_TOKEN",
    "gemini_api_key": "YOUR_GEMINI_API_KEY"
}
```

The Discord bot token can be obtained by creating a new bot in the [Discord Developer Portal](https://discord.com/developers/applications).

The Gemini API key can be obtained on [AI Studio](https://aistudio.google.com/).

3. Run the bot

```bash
python3 main.py
```