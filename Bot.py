import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = '8772520971:AAEZE27a1pRqYpIb8pjtQ3UA_Rr1gOvrMuw'

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- 1. MENU UTAMA ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📘 TINGKATAN 4", callback_data='menu_f4')],
        [InlineKeyboardButton("📕 TINGKATAN 5", callback_data='menu_f5')],
        [InlineKeyboardButton("❓ TAK TAHU TOPIK (+RM1)", callback_data='unknown')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Selamat datang ke Addmath Solver!\nSila pilih kategori:", reply_markup=reply_markup)

# --- 2. LOGIK BUTANG & BAB ---
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    await query.answer()

    if data == 'menu_f4':
        keyboard = [
            [InlineKeyboardButton("C1: Functions", callback_data='p'), InlineKeyboardButton("C2: Quad Func", callback_data='p')],
            [InlineKeyboardButton("C3: Systems Eq", callback_data='p'), InlineKeyboardButton("C4: Indices/Log", callback_data='p')],
            [InlineKeyboardButton("C5: Progressions", callback_data='p'), InlineKeyboardButton("C6: Linear Law", callback_data='p')],
            [InlineKeyboardButton("C7: Coordinate", callback_data='p'), InlineKeyboardButton("C8: Vectors", callback_data='p')],
            [InlineKeyboardButton("C9: Different.", callback_data='p'), InlineKeyboardButton("C10: Prob Dist", callback_data='p')],
            [InlineKeyboardButton("⬅️ Kembali", callback_data='back')]
        ]
        await query.edit_message_text("Pilih Bab Tingkatan 4:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == 'menu_f5':
        keyboard = [
            [InlineKeyboardButton("C1: Circular", callback_data='p'), InlineKeyboardButton("C2: Adv Diff", callback_data='p')],
            [InlineKeyboardButton("C3: Integration", callback_data='p'), InlineKeyboardButton("C4: Trig Func", callback_data='p')],
            [InlineKeyboardButton("C5: P&C", callback_data='p'), InlineKeyboardButton("C6: Prob Dist", callback_data='p')],
            [InlineKeyboardButton("C7: Kinematics", callback_data='p'), InlineKeyboardButton("C8: Math Prog", callback_data='p')],
            [InlineKeyboardButton("⬅️ Kembali", callback_data='back')]
        ]
        await query.edit_message_text("Pilih Bab Tingkatan 5:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == 'back':
        keyboard = [
            [InlineKeyboardButton("📘 TINGKATAN 4", callback_data='menu_f4')],
            [InlineKeyboardButton("📕 TINGKATAN 5", callback_data='menu_f5')],
            [InlineKeyboardButton("❓ TAK TAHU TOPIK (+RM1)", callback_data='unknown')]
        ]
        await query.edit_message_text("Sila pilih kategori:", reply_markup=InlineKeyboardMarkup(keyboard))

    else:
        price = 6 if data == 'unknown' else 5
        context.user_data['final_price'] = price
        await query.edit_message_text(text=f"Harga: RM{price}\n\nSila HANTAR GAMBAR soalan anda.")

# --- 3. TERIMA GAMBAR ---
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price = context.user_data.get('final_price', 5)
    await update.message.reply_text(f"Gambar diterima! ✅\n\nSila bayar RM{price} ke TNG: 01X-XXXXXXX\n\nHantar resit selepas bayar.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    print("ENJIN AKTIF! Sila cuba /start di Telegram.")
    app.run_polling()

if __name__ == '__main__':
    main()
