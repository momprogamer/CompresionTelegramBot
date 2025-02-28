import time
import os
import logging
from urllib.parse import quote
from asyncio import sleep
from shutil import rmtree

# Apps de Terceros
from pyrogram import Client, filters
import tgcrypto
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from convopyro import Conversation
import nest_asyncio
from aiohttp import web, ClientSession
import gdown

# Módulos locales
from utils import *
from progreso import progressub, progressddl, progressytdl, progresswget
from downloader.youtubedl import YoutubeDL
from downloader.wget import download as downloadwget
from server import download_file
from downloader.mediafire import get

# Configuración para Render
nest_asyncio.apply()
logging.basicConfig(level=logging.INFO)

# =========== Variables Globales ===========
yturls = []
API_ID = int(os.environ.get('API_ID', 0))
API_HASH = os.environ.get('API_HASH', '')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
BOT_URL = os.environ.get('BOT_URL', '')
TIME_WAKE = int(os.environ.get('TIME_WAKE', 10))
MESSAGE_COMPRIMIDO = "**Seleccione el tipo de compresión:**"
MESSAGE_COMPRIMIDO_BOTTON = [[
    InlineKeyboardButton("💾 ZIP", callback_data="z1"),
    InlineKeyboardButton("🗜 7Z", callback_data="z2"),
    InlineKeyboardButton("🎞 MKV", callback_data="z3")
]]

# =========== Cliente del Bot ===========
bot = Client(
    'CompresionWachu',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)
Conversation(bot)

# =========== Handlers ===========
@bot.on_message(filters.command('start') & filters.private)
def Bienvenido(client, message):
    reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton('⚙️Soporte', url='https://t.me/Wachu985'),
        InlineKeyboardButton('💻GITHUB', url='https://github.com/Wachu985/CompresionTelegramBot')
    ]])
    message.reply(
        f'✉️**Bienvenido {message.chat.first_name}**\n\n'
        '__📱Bot de Compresión y Descargas con File to Link📱__',
        reply_markup=reply_markup
    )

@bot.on_message(filters.media & filters.private)
def media_telegram(client, message):
    try:
        save_dir = f'./{message.chat.username}/'
        filename = get_filename_media(message)
        
        msg = message.reply("📡**Descargando...**", quote=True)
        start = time.time()
        
        bot.download_media(
            message,
            save_dir,
            progress=progressddl,
            progress_args=(msg, bot, filename, start)
        )
        
        msg.delete()
        message.reply('✅ Descargado Correctamente', quote=True)
    except Exception as e:
        message.reply(f'❌ Error: {e}', quote=True)

# [Todos los demás handlers (ls, link, rm, etc.)...]
# ... (Pega aquí el resto de tus handlers exactamente como los tenías)

# =========== Servidor Web ===========
async def wakeup_task():
    while True:
        async with ClientSession() as session:
            await session.get(f'{BOT_URL}/wakeup')
        await sleep(TIME_WAKE * 60)

async def run_server():
    await bot.start()
    logging.info('Bot iniciado ✅')
    
    # Configurar servidor web
    app = web.Application()
    app.router.add_get('/file/{route}/{file_name}', download_file)
    app.router.add_get('/wakeup', lambda r: web.Response(text="OK"))
    
    runner = web.AppRunner(app)
    await runner.setup()
    
    port = int(os.environ.get('PORT', 8000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    
    logging.info(f'Servidor iniciado en puerto {port} ✅')
    await wakeup_task()

if __name__ == '__main__':
    bot.loop.run_until_complete(run_server())
