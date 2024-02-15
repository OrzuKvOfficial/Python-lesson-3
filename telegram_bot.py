import logging
from telegram import Update
from telegram.ext import CommandHandler, Updater, CallbackContext

print('Starting up bot...')

TOKEN = "6421682986:AAEwiMVGiUIMjXgBro5oXoCrfgAkUmN_uyU"
BOTNAME = "orzu_movie_bot"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Create a decorator that takes users as an argument and if the user is in the list, it will run the function
def user_allowed(users):
    def decorator(func):
        async def wrapper(update: Update, context: CallbackContext):
            user = update.message.from_user
            logging.info(f'User {user.username} is trying to access the bot. id: {user.id}, message: {update.message.text}')
            if user.username in users:
                await func(update, context)
            else:
                await update.message.reply_text('You are not allowed to use this command')
        return wrapper
    return decorator

# Define start_command, help_command, custom_command, restart_command functions
def start_command(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! Welcome to Orzu Movie Bot.")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("This is a movie bot. You can use /custom command for custom actions.")

def custom_command(update: Update, context: CallbackContext):
    update.message.reply_text("This is a custom command.")

def restart_command(update: Update, context: CallbackContext):
    update.message.reply_text("Restart command is not available.")

# Run the program
if __name__ == '__main__':
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Commands
    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('help', help_command))
    dispatcher.add_handler(CommandHandler('custom', custom_command))
    dispatcher.add_handler(CommandHandler('restart', restart_command))

    updater.start_polling()
    updater.idle()
