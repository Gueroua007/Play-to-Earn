from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# التوكن الخاص بالبوت
TOKEN = "7644997888:AAFXMpPVWTBK-3KIkd91-LZfmv6mWH7ogrk"
# الاسم المختصر للعبة كما سجلته مع BotFather (هنا "Earn")
GAME_SHORT_NAME = "Earn"

def start(update: Update, context: CallbackContext):
    print("Received /start command")
    update.message.reply_game(game_short_name=GAME_SHORT_NAME)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()