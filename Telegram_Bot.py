import telegram

import telegram
import time

bot_token = '2103546925:AAGQu5z8DvcdcPuxX42OZmFSeUHXZWYvYoc'
chat_id = '1271429755'

bot = telegram.Bot(token=bot_token)
#print(bot.get_me())
# People can use telegram.me/<bot_username> links or username search to find your bot.
#updates = bot.get_updates()
#print(updates[0])
#bot.send_message(text='Hi John!', chat_id=1271429755)
#updater = Updater(token='2103546925:AAGQu5z8DvcdcPuxX42OZmFSeUHXZWYvYoc', use_context=True)


#while True:
#    bot.send_message(chat_id=chat_id, text='Hola mundo, este es nuestro primer programa con la api de telegram')
#    time.sleep(5)

#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://git.io/JOmFw.
"""
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Ver Catálogo", callback_data='Ver Catálogo'),
            InlineKeyboardButton("Seleccionar componentes", callback_data='Seleccionar componentes'),
        ],

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Seleccione una opción :', reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    if (query.data=='Ver Catálogo'):
        query.edit_message_text(text=f"opción seleccionada : {query.data}")

        with open('Acer.jpg', 'rb') as photo_file:
            bot.sendPhoto(chat_id=chat_id,photo=photo_file,caption='$1.650.000')

        #else:
        #query.edit_message_text(text=f"opción seleccionada : {query.data}")

def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("2103546925:AAGQu5z8DvcdcPuxX42OZmFSeUHXZWYvYoc")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
