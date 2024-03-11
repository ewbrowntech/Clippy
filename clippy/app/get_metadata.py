"""
get_metadata.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Get the available metadata of a YouTube video via the PyTube API

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the Clippy project and is released under
the MIT License. See the LICENSE file for more details.
"""

import os
import json
import logging
import httpx


async def get_metadata(video_id: str):
    if video_id is None:
        return ValueError("video_id is None")

    logger = logging.getLogger(__name__)

    # Get the hostname of the PyTube API server
    pytube_api_hostname = os.environ.get("PYTUBE_API_HOSTNAME")
    if pytube_api_hostname is None:
        raise EnvironmentError(
            "The environment variable PYTUBE_API_HOSTNAME is not set"
        )

    request_url = "http://pytube-api:8000/metadata"
    params = {"v": video_id}

    # Execute the request
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(request_url, params=params)
            response.raise_for_status()  # Raises an exception for 4XX/5XX responses
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.info(f"HTTP error occurred: {e.response.status_code}")
    except httpx.RequestError as e:
        logger.info(
            f"An error {e.response.status_code} occurred while requesting {e.request.url!r}."
        )
