import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# Gantikan dengan Token anda
TOKEN = '8772520971:AAEZE27a1pRqYpIb8pjtQ3UA_Rr1gOvrMuw'

# Setup Logging (Untuk kesan error)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# 1. MENU UTAMA
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Tingkatan 4 (F4)", callback_query_data='f4')],
        [InlineKeyboardButton("Tingkatan 5 (F5)", callback_query_data='f5')],
        [InlineKeyboardButton("Saya Tak Tahu Topik (+RM1)", callback_query_data='unknown')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Selamat datang ke Addmath Solver!\n\nSila pilih kategori topik soalan anda:",
        reply_markup=reply_markup
    )

# 2. HANDLE PILIHAN USER
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    if data == 'f4':
        text = "Topik F4 terpilih. (Kos: RM5)"
        price = 5
    elif data == 'f5':
        text = "Topik F5 terpilih. (Kos: RM5)"
        price = 5
    else:
        text = "Anda memilih 'Tak Tahu Topik'. (Kos: RM6)"
        price = 6

    context.user_data['final_price'] = price
    await query.edit_message_text(text=f"{text}\n\nSila HANTAR GAMBAR soalan anda sekarang.")

# 3. TERIMA GAMBAR
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price = context.user_data.get('final_price', 5)
    await update.message.reply_text(
        f"Gambar diterima! ✅\n\nSila buat bayaran RM{price} ke TNG: 01X-XXXXXXX.\n"
        "Hantar resit selepas bayar."
    )

def main():
    # Bina Application
    application = Application.builder().token(TOKEN).build()

    # Tambah Handler
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    print("Bot sedang aktif dan diperbaiki... Cuba tekan /start di Telegram!")
    application.run_polling()

if __name__ == '__main__':
    main()
