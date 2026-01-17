import logging
from telegram import Update, InlineQueryResultGame
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# 1. PEGA TU TOKEN AQUÍ (El que te dio BotFather)
TOKEN = "8578596978:AAHBSRapx8-FJiJseZ5V5x8gX8FXSi6gp_w"

# 2. TU LINK DE JUEGO
GAME_URL = "https://venecorun-stack.github.io/venecorun/"

# 3. EL NOMBRE CORTO QUE ELEGISTE EN BOTFATHER
GAME_SHORT_NAME = "venecorun_game"

# Configuración de errores para ver si algo falla
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Envía el mensaje con el botón para jugar cuando alguien pone /start"""
    await update.message.reply_game(game_short_name=GAME_SHORT_NAME)

async def play_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Esta función abre el link del juego cuando el usuario toca 'Play venecorun_game'"""
    query = update.callback_query
    if query.game_short_name == GAME_SHORT_NAME:
        await query.answer(url=GAME_URL)
    else:
        await query.answer(text="Juego no encontrado")

if __name__ == "__main__":
    # Crear la aplicación del bot
    app = Application.builder().token(TOKEN).build()
    
    # Comandos
    app.add_handler(CommandHandler("start", start))
    
    # Manejador del botón de jugar
    app.add_handler(CallbackQueryHandler(play_button_handler))
    
    print("Bot encendido... ve a Telegram y pon /start")
    app.run_polling()
