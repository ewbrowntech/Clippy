"""
bot.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Drive the Discord bot

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the Clippy project and is released under
the MIT License. See the LICENSE file for more details.
"""

import os
import time
import logging
import discord

from healthcheck import healthcheck
from download_video import download_video

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define the intents of the Discord client
intents = discord.Intents.default()
intents.message_content = True

# Generate the Discord bot client
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!hello"):
        print("Hello message")
        await message.channel.send("Hello!")
    if any(
        message.content.startswith(command)
        for command in ["!download-video", "!download-audio", "!download-video-only"]
    ):
        await download_video(message)


# Verify that the API key is set
api_token = os.environ.get("API_TOKEN")
if api_token is None:
    raise EnvironmentError("Environment variable API_TOKEN is not set")

# Run the Discord bot client
logging.info("Running healthcheck on microservices...")
time.sleep(5)
healthcheck()
logging.info("Healthcheck passed. Starting Discord bot...")
client.run(api_token)
