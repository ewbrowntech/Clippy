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

    if message.content.startswith("!download-audio"):
        response = await message.channel.send(
            "Download a video (audio)", reference=message
        )
        # Download the audio stream
        response = await download_audio_stream(video_id, response)
        # Upload the audio stream

    elif message.content.startswith("!download-video-only"):
        response = await message.channel.send(
            "Download a video (video only)", reference=message
        )
        # Get the available resolutions
        # Download video stream
        response = await download_video_stream(video_id, response)
        # Upload the video stream

    elif message.content.startswith("!download-video"):
        await message.channel.send("Download a video (multimedia)", reference=message)
        # Get the available resolutions
        # Download the audio stream
        response = await download_audio_stream(video_id, response)
        # Download the video stream
        response = await download_video_stream(video_id, response)
        # Merge the audio and video streams
        response = await merge_multimedia(response)
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
