from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# TOKEN ANDA
TOKEN = '8772520971:AAEZE27a1pRqYpIb8pjtQ3UA_Rr1gOvrMuw'

# 1. MENU UTAMA
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Tingkatan 4 (F4)", callback_query_data='f4')],
        [InlineKeyboardButton("Tingkatan 5 (F5)", callback_query_data='f5')],
        [InlineKeyboardButton("Saya Tak Tahu Topik (+RM1)", callback_query_data='unknown')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Selamat datang ke Addmath Solver USIM!\n\nSila pilih kategori topik soalan anda:",
        reply_markup=reply_markup
    )

# 2. HANDLE PILIHAN USER
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    if data == 'f4':
        text = "Topik F4: 1.Fungsi, 2.Persamaan Kuadratik, 3.Sistem Persamaan, 4.Indeks/Log, 5.Janjang, 6.Hukum Linear, 7.Geometri Koordinat, 8.Vektor, 9.Penyelesaian Segitiga, 10.Nombor Indeks."
        price = 5
    elif data == 'f5':
        text = "Topik F5: 1.Sukatan Membulat, 2.Pembezaan, 3.Pengamiran, 4.Pilih Atur/Gabungan, 5.Taburan Kebarangkalian, 6.Fungsi Trigonometri, 7.Pengaturcaraan Linear, 8.Kinematik."
        price = 5
    else: # Unknown
        text = "Anda memilih 'Tak Tahu Topik'. Surcharge RM1 dikenakan."
        price = 6

    context.user_data['final_price'] = price
    await query.edit_message_text(
        text=f"{text}\n\n**KOS: RM{price}**\n\nSila HANTAR GAMBAR soalan anda sekarang."
    )

# 3. TERIMA GAMBAR & MINTA BAYARAN
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price = context.user_data.get('final_price', 5)
    
    await update.message.reply_text(
        f"Gambar soalan diterima! ✅\n\nSila buat bayaran RM{price} ke:\n"
        "TNG eWallet: 01X-XXXXXXX (Nama Anda)\n\n"
        "Selepas bayar, sila hantar SCREENSHOT RESIT di sini untuk pengesahan."
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    print("Bot sedang aktif... Sedia menjana duit raya!")
    app.run_polling()

if __name__ == '__main__':
    main()
