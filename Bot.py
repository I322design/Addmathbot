import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# KONFIGURASI
TOKEN = '8772520971:AAEZEZE27a1pRqYpIb8pjtQ3UA_Rr1gOvrMuw'
TNG = '131449517376'

logging.basicConfig(level=logging.INFO)

async def start(u, c):
    kb = [[InlineKeyboardButton("📘 T4", callback_data='4'), InlineKeyboardButton("📕 T5", callback_data='5')],
          [InlineKeyboardButton("❓ TAK TAHU", callback_data='u')]]
    await u.message.reply_text("Pilih kategori:", reply_markup=InlineKeyboardMarkup(kb))

async def btn(u, c):
    q = u.callback_query
    await q.answer()
    p = 6 if q.data == 'u' else 5
    c.user_data['p'] = p
    await q.edit_message_text(f"Harga: RM{p}. Sila hantar GAMBAR soalan.")

async def img(u, c):
    p = c.user_data.get('p', 5)
    await u.message.reply_text(f"Diterima! Sila bayar RM{p} ke TNG:\n{TNG}")

if __name__ == '__main__':
    print("ENJIN AKTIF!")
    bot = Application.builder().token(TOKEN).build()
    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(CallbackQueryHandler(btn))
    bot.add_handler(MessageHandler(filters.PHOTO, img))
    bot.run_polling()