import logging
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
from telegram import Update, InlineQueryResultGame
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# 1. PEGA TU TOKEN AQUÍ (El de BotFather)
TOKEN = "8272294302:AAGwu8-5pRClyeTbuHXbMw0QpdOJIyS8MFU"

# 2. TU LINK DE JUEGO
GAME_URL = "https://venecorun-stack.github.io/venecorun/"

# 3. EL NOMBRE CORTO QUE ELEGISTE EN BOTFATHER
GAME_SHORT_NAME = "venecorun_game"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- ESTO ES PARA QUE RENDER NO APAGUE EL BOT ---
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive")

def run_health_check():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    server.serve_forever()
# -----------------------------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_game(game_short_name=GAME_SHORT_NAME)

async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query.game_short_name == GAME_SHORT_NAME:
        await query.answer(url=GAME_URL)

if __name__ == '__main__':
    # Iniciar el servidor de salud en un hilo separado
    threading.Thread(target=run_health_check, daemon=True).start()
    
    # Iniciar el Bot
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(callback))
    
    print("Bot encendido con servidor de salud...")
    application.run_polling()
