import os
import uuid
import logging
import requests
from telegram import Update, InputMediaVideo
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes
)
from config import Config
from utils.progress import DownloadProgressBar
from utils.helpers import create_quality_keyboard, create_about_keyboard, format_file_size

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when the command /start is issued."""
    await update.message.reply_text(
        Config.START_MESSAGE.format(channel_link=Config.CHANNEL_LINK),
        parse_mode='HTML',
        disable_web_page_preview=True
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a help message when the command /help is issued."""
    await update.message.reply_text(
        Config.HELP_MESSAGE.format(
            owner=Config.OWNER_USERNAME,
            github_repo=Config.GITHUB_REPO
        ),
        parse_mode='HTML',
        disable_web_page_preview=True
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming messages with Reddit URLs."""
    message = update.message
    text = message.text.strip()

    if "reddit.com" not in text and "v.redd.it" not in text:
        await message.reply_text(
            "❌ Please send a valid Reddit video URL.",
            parse_mode='HTML'
        )
        return

    try:
        logger.info(f"User {update.effective_user.id} sent URL: {text}")

        processing_msg = await message.reply_text(
            "🔍 <i>Fetching video information...</i>",
            parse_mode='HTML'
        )

        api_url = f"{Config.API_URL}{text}"
        response = requests.get(api_url, timeout=10)
        data = response.json()

        if not data.get('hd_link') and not data.get('sd_links'):
            await processing_msg.edit_text(
                "❌ No downloadable video found in this URL.",
                parse_mode='HTML'
            )
            return

        await processing_msg.edit_text(
            "🎥 <b>Available Qualities:</b>\n\n"
            "⬇️ Please choose a quality option below:",
            parse_mode='HTML',
            reply_markup=create_quality_keyboard(data)
        )

        context.user_data['links'] = data

    except Exception as e:
        logger.error(f"Error processing URL: {e}")
        await processing_msg.edit_text(
            "⚠️ An error occurred while processing your request. Please try again later.",
            parse_mode='HTML'
        )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button callbacks."""
    query = update.callback_query
    await query.answer()

    user_data = context.user_data
    links = user_data.get('links', {})

    if query.data == 'about':
        await query.edit_message_text(
            "🌟 <b>BDBOTS Reddit Video Downloader</b> 🌟\n\n"
            "🔹 <i>Powered by BDBOTS API</i>\n"
            "🔹 <i>Fast and reliable downloads</i>\n\n"
            f"👨‍💻 <b>Owner:</b> {Config.OWNER_USERNAME}\n"
            f"📢 <b>Channel:</b> {Config.CHANNEL_LINK}\n"
            f"💻 <b>Source Code:</b> {Config.GITHUB_REPO}",
            parse_mode='HTML',
            reply_markup=create_about_keyboard(),
            disable_web_page_preview=True
        )
    elif query.data == 'back':
        await query.edit_message_text(
            "🎥 <b>Available Qualities:</b>\n\n"
            "⬇️ Please choose a quality option below:",
            parse_mode='HTML',
            reply_markup=create_quality_keyboard(links)
        )
    elif query.data.startswith('quality_'):
        quality = query.data.split('_')[1]

        if quality == 'hd':
            video_url = links['hd_link']
            quality_name = "HD"
        else:
            index = int(quality) - 1
            if index >= len(links.get('sd_links', [])):
                await query.edit_message_text("⚠️ Invalid video quality selection.")
                return
            video_url = links['sd_links'][index]['url']
            quality_name = links['sd_links'][index]['quality']

        await query.edit_message_text(
            f"⏳ <i>Preparing {quality_name} video for download...</i>",
            parse_mode='HTML'
        )

        try:
            progress = DownloadProgressBar(update, context)
            response = requests.get(video_url, stream=True, timeout=15)

            if response.status_code != 200:
                raise Exception("Failed to download video")

            file_size = int(response.headers.get('content-length', 0))
            file_path = f"temp_{update.effective_user.id}_{uuid.uuid4()}.mp4"

            with open(file_path, 'wb') as f:
                if file_size == 0:
                    logger.warning("Missing Content-Length header. Skipping progress bar.")
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                else:
                    downloaded = 0
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            progress(downloaded, 1024, file_size)

            with open(file_path, 'rb') as video_file:
                await context.bot.send_video(
                    chat_id=update.effective_chat.id,
                    video=video_file,
                    caption=f"🎥 <b>Reddit Video</b> ({quality_name})\n\n"
                            f"📢 <a href='{Config.CHANNEL_LINK}'>Join our channel</a>",
                    parse_mode='HTML'
                )

            os.remove(file_path)

        except Exception as e:
            logger.error(f"Error downloading video: {e}")
            await query.edit_message_text(
                "⚠️ Failed to download the video. Please try again later.",
                parse_mode='HTML'
            )

def main():
    """Start the bot."""
    try:
        from pytz import utc  # Ensure pytz is available
    except ImportError:
        print("❗ Missing 'pytz' package. Install it using: pip install pytz")
        return

    application = Application.builder().token(Config.BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CallbackQueryHandler(button_callback))

    logger.info("Bot started. Waiting for messages...")
    application.run_polling()

if __name__ == '__main__':
    main()
