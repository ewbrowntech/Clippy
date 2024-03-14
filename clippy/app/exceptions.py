import httpx


class PytubeApiException(Exception):
    def __init__(self):
        self.message = "Failed to reach PyTube-API"
        super().__init__(self.message)
