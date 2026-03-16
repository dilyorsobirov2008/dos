#!/usr/bin/env python3
"""
SuperMarket Telegram Bot
Admin: 7351189083
"""

import logging
import os  # Portni olish uchun qo'shildi
from flask import Flask  # Render porti uchun qo'shildi
from threading import Thread  # Serverni parallel ishlatish uchun qo'shildi
from telegram import Update, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- PORT UCHUN QO'SHIMCHA ---
flask_app = Flask('')

@flask_app.route('/')
def health_check():
    return "Bot is alive!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()
# ------------------------------

BOT_TOKEN = "8714108548:AAGnRXk-xKqGluK_EAZqUVjfFEdlW9EK6mI"
ADMIN_ID = 7351189083

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
        [InlineKeyboardButton("📞 Aloqa", url="+998975062020")]
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
    # Render portini band qilishni boshlaymiz
    keep_alive()

    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin_panel))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    logger.info("Bot ishga tushdi...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
