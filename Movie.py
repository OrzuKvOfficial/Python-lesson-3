from telegram import *
from telegram.ext import *
from requests import *

updater = Updater(token="6421682986:AAEwiMVGiUIMjXgBro5oXoCrfgAkUmN_uyU")
dispatcher = updater.dispatcher

def startCommand(update: Update, context: CallbackContext):
    print(update.effective_chat.username)
    print(update.message.text)

dispatcher.add_handler(CommandHandler("start", startCommand))

updater.start_polling()
