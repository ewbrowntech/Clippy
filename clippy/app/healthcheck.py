"""
healthcheck.py

@Author: Ethan Brown - ethan@ewbrowntech.com

Perform a health check on the PyTube API server

Copyright (C) 2024 by Ethan Brown
All rights reserved. This file is part of the Clippy project and is released under
the MIT License. See the LICENSE file for more details.
"""

import os
import logging
import httpx
from exceptions import PytubeApiException


def healthcheck():
    pytube_api_healthcheck()


def pytube_api_healthcheck():
    try:
        # Make a GET request to the healthcheck endpoint of PyTube API
        response = httpx.get("http://pytube-api:8000/healthcheck")

        # Check if the response status code is 200
        if response.status_code == 200:
            logging.info("Healthcheck passed")
        else:
            logging.error(
                "PyTube-API Healthcheck failed with status code: %d",
                response.status_code,
            )
            raise PytubeApiException("Healthcheck failed")

    except httpx.ConnectError as e:
        logging.error("PyTube-API healthcheck failed with error: %s", str(e))
        raise PytubeApiException()

    except httpx.RequestError as e:
        logging.error("PyTube-API Healthcheck failed with error: %s", str(e))
        raise PytubeApiException("Healthcheck failed")

    except Exception as e:
        # Handle any other exceptions that may occur
        logging.error("An unexpected error occurred during healthcheck: %s", str(e))
        raise
