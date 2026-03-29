import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = '8772520971:AAEZE27a1pRqYpIb8pjtQ3UA_Rr1gOvrMuw'

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- 1. START MENU ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📘 TINGKATAN 4", callback_query_data='menu_f4')],
        [InlineKeyboardButton("📕 TINGKATAN 5", callback_query_data='menu_f5')],
        [InlineKeyboardButton("❓ SAYA TAK TAHU TOPIK (+RM1)", callback_query_data='unknown')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Selamat datang ke Addmath Solver!\nSila pilih kategori soalan anda:",
        reply_markup=reply_markup
    )

# --- 2. HANDLE BUTTONS ---
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    await query.answer()

    # MENU FORM 4
    if data == 'menu_f4':
        keyboard = [
            [InlineKeyboardButton("C1: Functions", callback_query_data='f4_c1'), InlineKeyboardButton("C2: Quadratic", callback_query_data='f4_c2')],
            [InlineKeyboardButton("C3: Systems Eq", callback_query_data='f4_c3'), InlineKeyboardButton("C4: Indices/Log", callback_query_data='f4_c4')],
            [InlineKeyboardButton("C5: Progressions", callback_query_data='f4_c5'), InlineKeyboardButton("C6: Linear Law", callback_query_data='f4_c6')],
            [InlineKeyboardButton("C7: Coordinate", callback_query_data='f4_c7'), InlineKeyboardButton("C8: Vectors", callback_query_data='f4_c8')],
            [InlineKeyboardButton("C9: Differentiation", callback_query_data='f4_c9'), InlineKeyboardButton("C10: Prob. Dist", callback_query_data='f4_c10')],
            [InlineKeyboardButton("⬅️ Kembali", callback_query_data='back')]
        ]
        await query.edit_message_text("Pilih Bab Tingkatan 4:", reply_markup=InlineKeyboardMarkup(keyboard))

    # MENU FORM 5
    elif data == 'menu_f5':
        keyboard = [
            [InlineKeyboardButton("C1: Circular", callback_query_data='f5_c1'), InlineKeyboardButton("C2: Adv Diff", callback_query_data='f5_c2')],
            [InlineKeyboardButton("C3: Integration", callback_query_data='f5_c3'), InlineKeyboardButton("C4: Trigonometry", callback_query_data='f5_c4')],
            [InlineKeyboardButton("C5: P&C", callback_query_data='f5_c5'), InlineKeyboardButton("C6: Prob. Dist", callback_query_data='f5_c6')],
            [InlineKeyboardButton("C7: Kinematics", callback_query_data='f5_c7'), InlineKeyboardButton("C8: Math Prog", callback_query_data='f5_c8')],
            [InlineKeyboardButton("⬅️ Kembali", callback_query_data='back')]
        ]
        await query.edit_message_text("Pilih Bab Tingkatan 5:", reply_markup=InlineKeyboardMarkup(keyboard))

    # BACK TO MAIN
    elif data == 'back':
        keyboard = [
            [InlineKeyboardButton("📘 TINGKATAN 4", callback_query_data='menu_f4')],
            [InlineKeyboardButton("📕 TINGKATAN 5", callback_query_data='menu_f5')],
            [InlineKeyboardButton("❓ SAYA TAK TAHU TOPIK (+RM1)", callback_query_data='unknown')]
        ]
        await query.edit_message_text("Sila pilih kategori soalan anda:", reply_markup=InlineKeyboardMarkup(keyboard))

    # HARGA LOGIC
    else:
        price = 6 if data == 'unknown' else 5
        context.user_data['final_price'] = price
        await query.edit_message_text(text=f"Harga: RM{price}\n\nSila HANTAR GAMBAR soalan anda sekarang.")

# --- 3. RECEIVE PHOTO ---
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price = context.user_data.get('final_price', 5)
    await update.message.reply_text(
        f"Gambar diterima! ✅\n\nSila buat bayaran RM{price} ke:\nTNG eWallet: 01X-XXXXXXX (Nama Anda)\n\nHantar resit selepas bayar."
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    
    print("ENJIN AKTIF! Sila test /start di Telegram.")
    app.run_polling()

if __name__ == '__main__':
    main()
