"""
download_video.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Drive the downloading of a YouTube video

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the Clippy project and is released under
the MIT License. See the LICENSE file for more details.
"""

import discord
from discord import Message
from extract_video_id import extract_video_id, NoURLException
from get_metadata import get_metadata


async def download_video(message: Message):
    """
    Run the download operation
    """
    # Extract the URL
    try:
        video_id = await extract_video_id(message.content)
    except NoURLException:
        await message.channel.send(
            "Please include a valid YouTube URL in your request. (ex: <https://youtu.be/dQw4w9WgXcQ>)",
            reference=message,
        )
        return

    # Get the video metadata
    metadata = await get_metadata(video_id)
    if metadata["age_restricted"]:
        await message.channel.send(
            "This video is age restricted, and it, therefore, cannot be downloaded.",
            reference=message,
        )
        return

    # Get the title of the video
    title = metadata["title"]

    if message.content.startswith("!download-audio"):
        response_main = await message.channel.send(
            f"Downloading **{title}** as an **audio** file...", reference=message
        )
        status = await message.channel.send("Starting...", reference=message)
        # Download the audio stream
        status = await download_audio_stream(video_id, status)
        # Upload the audio stream

    elif message.content.startswith("!download-video-only"):
        response_main = await message.channel.send(
            f"Downloading **{title}** as a **video** file...", reference=message
        )
        status = await message.channel.send("Starting...", reference=message)
        # Get the available resolutions
        # Download video stream
        status = await download_video_stream(video_id, status)
        # Upload the video stream

    elif message.content.startswith("!download-video"):
        response_main = await message.channel.send(
            f"Downloading **{title}** as a **multimedia** file...", reference=message
        )
        status = await message.channel.send("Starting...", reference=message)
        # Get the available resolutions
        # Download the audio stream
        status = await download_audio_stream(video_id, status)
        # Download the video stream
        status = await download_video_stream(video_id, status)
        # Merge the audio and video streams
        status = await merge_multimedia(status)
        # Upload the multimedia file

    return


async def download_audio_stream(video_id: str, response: Message):
    response = await response.edit(content="Downloading the audio stream...")
    return response


async def download_video_stream(video_id: str, response: Message):
    response = await response.edit(content="Downloading the video stream...")
    return response


async def merge_multimedia(response: Message):
    response = await response.edit(
        content="Merging the audio and video stream... (This may take a while)"
    )
    return response
