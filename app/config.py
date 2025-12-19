import os

def get_bot_token():
    token = os.getenv("8530548516:AAGolHePa16jWsDHxew4nibN9v0NW6YHFSs")
    if not token:
        raise RuntimeError("BOT_TOKEN is not set!")
    return token
