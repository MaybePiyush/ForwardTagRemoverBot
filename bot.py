import logging
from telegram.ext import (
    filters,
    ApplicationBuilder,
    CommandHandler,
    MessageHandler
)

from plugins.__main__ import *
from config import Config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def main():
    bot = ApplicationBuilder().token(Config.BOT_TOKEN).build()
    bot.add_handler(CommandHandler('start', startMessage))
    bot.add_handler(CommandHandler('help', helpMessage))
    bot.add_handler(MessageHandler(filters.REPLY, handleCaption))
    bot.add_handler(MessageHandler(
        filters.ALL & ~filters.COMMAND, handleMessage))
    bot.run_polling()


if __name__ == '__main__':
    main()
