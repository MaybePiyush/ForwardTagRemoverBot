from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from config import Config

keyboard = [
    [
        InlineKeyboardButton("Source Code", url=Config.SOURCE)
    ],
    [
        InlineKeyboardButton("How To Create A Bot Like Me",
                             url="https://youtu.be/swg6un2N4Fk")
    ]
]

reply_markup = InlineKeyboardMarkup(keyboard)


async def startMessage(_, bot):
    await _.message.reply_text(Config.START_TEXT.format(_.message.from_user.full_name, _.message.chat.id), reply_markup=reply_markup,
                               parse_mode=ParseMode.MARKDOWN)


async def helpMessage(_, bot):
    await _.message.reply_text(Config.HELP_TEXT, reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN)


async def handleMessage(_, bot):
    
    await _.message.copy(_.effective_user.id)
