#!/usr/bin/env python3
"""
SuperMarket Telegram Bot
Admin: 7351189083
"""

import logging
from telegram import Update, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8714108548:AAFV9S6A49kGxT9Sm3mu3sY6TuMfuq0ix9E"
ADMIN_ID = 7351189083

# MINI APP URL - shu yerga o'zingizning hosting URL'ini qo'ying
# Masalan: https://yourname.github.io/supermarket/
# Yoki: https://your-domain.com/supermarket/index.html
WEBAPP_URL = "https://dos-amber-eight.vercel.app/"


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Bot ishga tushganda"""
    user = update.effective_user
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "🛒 Do'konni ochish",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )],
        [InlineKeyboardButton("📞 Aloqa", url="@superrmarkettbot")]
    ])
    
    await update.message.reply_text(
        f"👋 Salom, {user.first_name}!\n\n"
        f"🏪 *SuperMarket*ga xush kelibsiz!\n\n"
        f"🛒 300+ mahsulot\n"
        f"📦 Tez yetkazib berish\n"
        f"💳 Qulay to'lov\n\n"
        f"Quyidagi tugmani bosing:",
        parse_mode='Markdown',
        reply_markup=keyboard
    )


async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin panel"""
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ Siz admin emassiz!")
        return
    
    await update.message.reply_text(
        "👨‍💼 *Admin Panel*\n\n"
        "📊 Bot ishlayapti!\n"
        "🛒 Buyurtmalar kelganda bu yerda ko'rasiz.\n\n"
        "Buyruqlar:\n"
        "/stats - Statistika\n"
        "/broadcast - Xabar yuborish",
        parse_mode='Markdown'
    )


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Statistika"""
    if update.effective_user.id != ADMIN_ID:
        return
    await update.message.reply_text("📊 Statistika yaqinda qo'shiladi!")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Oddiy xabarlar"""
    await update.message.reply_text(
        "🛒 Do'konni ochish uchun /start bosing!"
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin_panel))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    logger.info("Bot ishga tushdi...")
app = Flask('')

@app.route('/')
def home():
    return "Bot ishlayapti!"

def run():
    # Render avtomatik ravishda PORT o'zgaruvchisini beradi
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def start_server():
    t = Thread(target=run)
    t.start()

# Botni ishga tushirishdan oldin serverni yoqing
if __name__ == "__main__":
    start_server()
    # Bu yerda botingizning asosiy (polling) kodi bo'ladi
    # Masalan: bot.polling()


if __name__ == "__main__":
    main()
