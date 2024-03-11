"""
extract_video_id.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Extract the video ID from a Discord message

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the Clippy project and is released under
the MIT License. See the LICENSE file for more details.
"""

import re


async def extract_video_id(message_content: str):
    pattern = re.compile(
        r"https?://(?:www\.youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]+)"
    )
    matches = pattern.findall(message_content)
    if len(matches) < 1:
        raise NoURLException
    else:
        return matches[0]


class NoURLException(Exception):
    def __init__(self):
        self.message = "No YouTube URL was found in the given message"
        super().__init__(self.message)
