from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
import sqlite3

# توكن البوت
TOKEN = "7644997888:AAFXMpPVWTBK-3KIkd91-LZfmv6mWH7ogrk"

# إنشاء قاعدة بيانات لحفظ بيانات اللاعبين
conn = sqlite3.connect("game.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                  (user_id INTEGER PRIMARY KEY, ton_balance INTEGER, robot_level INTEGER, referrals INTEGER)''')
conn.commit()

# دالة لبدء البوت وعرض الواجهة الرئيسية
def start(update: Update, context: CallbackContext):
    user_id = update.message.chat_id

    # التحقق من وجود المستخدم في قاعدة البيانات
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = cursor.fetchone()
    if not user:
        cursor.execute("INSERT INTO users (user_id, ton_balance, robot_level, referrals) VALUES (?, ?, ?, ?)", (user_id, 0, 1, 0))
        conn.commit()

    # عرض الأزرار
    keyboard = [
        [InlineKeyboardButton("🏠 Home", callback_data="home"),
         InlineKeyboardButton("📜 Task", callback_data="task")],
        [InlineKeyboardButton("🔗 Referral", callback_data="referral"),
         InlineKeyboardButton("💰 Wallet", callback_data="wallet")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("مرحبًا بك في لعبة روبوت المستقبل! اختر من القائمة:", reply_markup=reply_markup)

# دالة عرض بيانات اللاعب
def home(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.message.chat_id

    cursor.execute("SELECT ton_balance, robot_level FROM users WHERE user_id=?", (user_id,))
    user = cursor.fetchone()
    ton_balance, robot_level = user

    message = f"🤖 **روبوتك:** مستوى {robot_level}\n💰 **رصيد TON:** {ton_balance}"
    query.edit_message_text(message)

# دالة عرض المهام
def task(update: Update, context: CallbackContext):
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("🔍 حل لغز المتاهة", callback_data="maze_puzzle")],
        [InlineKeyboardButton("⚙️ تحدي تطوير الروبوت", callback_data="robot_challenge")],
        [InlineKeyboardButton("⬅️ العودة", callback_data="home")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text("📜 اختر مهمة لإكمالها وكسب المكافآت:", reply_markup=reply_markup)

# دالة دعوة الأصدقاء
def referral(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.message.chat_id
    referral_link = f"https://t.me/YOUR_BOT_USERNAME?start={user_id}"

    message = f"🔗 شارك هذا الرابط لدعوة أصدقائك وكسب 5 TON لكل إحالة:\n{referral_link}"
    query.edit_message_text(message)

# دالة عرض المحفظة
def wallet(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.message.chat_id

    cursor.execute("SELECT ton_balance FROM users WHERE user_id=?", (user_id,))
    ton_balance = cursor.fetchone()[0]

    message = f"💰 **رصيدك:** {ton_balance} TON"
    query.edit_message_text(message)

# دالة تحدي لغز المتاهة الزمنية
def maze_puzzle(update: Update, context: CallbackContext):
    query = update.callback_query
    query.edit_message_text("❓ ألغاز المتاهة الزمنية قادمة قريبًا!")

# دالة تحدي تطوير الروبوت
def robot_challenge(update: Update, context: CallbackContext):
    query = update.callback_query
    query.edit_message_text("⚙️ تحديات تطوير الروبوت قادمة قريبًا!")

# إعداد الأوامر
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("home", home))
    dp.add_handler(CommandHandler("task", task))
    dp.add_handler(CommandHandler("referral", referral))
    dp.add_handler(CommandHandler("wallet", wallet))

    dp.add_handler(CommandHandler("maze_puzzle", maze_puzzle))
    dp.add_handler(CommandHandler("robot_challenge", robot_challenge))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()