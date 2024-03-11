"""
download_video.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Drive the downloading of a YouTube video

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the Clippy project and is released under
the MIT License. See the LICENSE file for more details.
"""


async def download_video(message):
    if message.content.startswith("!download-video-only"):
        await message.channel.send("Download a video (video only)")
    elif message.content.startswith("!download-audio"):
        await message.channel.send("Download a video (audio)")
    elif message.content.startswith("!download-video"):
        await message.channel.send("Download a video (multimedia)")
