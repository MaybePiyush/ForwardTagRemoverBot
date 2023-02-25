import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    SOURCE = "https://github.com/MaybePiyush/ForwardTagRemoverBot"
    START_TEXT = """
Hi [{}](tg://user?id={}) 
I am A Forward Tag remover Bot.
Send /help to know more ©[Piyush Garg](https://github.com/MaybePiyush)"""
    HELP_TEXT = "Forward Me A File,Video,Audio,Photo or Anything And \nI will Send You the File Back\n\n`How to Set Caption?`\nReply Caption to a File,Photo,Audio,Media"
