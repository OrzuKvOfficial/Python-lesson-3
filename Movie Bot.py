from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Salom!")

def main():
    updater = Updater("6421682986:AAEwiMVGiUIMjXgBro5oXoCrfgAkUmN_uyU", use_context=True)
    dispatcher = updater.dispatcher

    # "start" tugmasiga javob beruvchi handler
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
