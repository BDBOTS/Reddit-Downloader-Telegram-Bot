from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import Config

def create_quality_keyboard(links):
    keyboard = []
    
    # Add HD button if available
    if links.get('hd_link'):
        keyboard.append([
            InlineKeyboardButton("🎬 HD Quality", callback_data=f"quality_hd")
        ])
    
    # Add SD buttons
    for i, sd in enumerate(links.get('sd_links', []), start=1):
        keyboard.append([
            InlineKeyboardButton(f"📱 {sd['quality']}", callback_data=f"quality_{i}")
        ])
    
    # Add info and channel buttons
    keyboard.append([
        InlineKeyboardButton("ℹ️ About", callback_data="about"),
        InlineKeyboardButton("📢 Channel", url=Config.CHANNEL_LINK)
    ])
    
    return InlineKeyboardMarkup(keyboard)

def create_about_keyboard():
    keyboard = [
        [InlineKeyboardButton("👨‍💻 Owner", url=f"tg://user?username={Config.OWNER_USERNAME[1:]}")],
        [InlineKeyboardButton("📚 GitHub", url=Config.GITHUB_REPO)],
        [InlineKeyboardButton("🔙 Back", callback_data="back")]
    ]
    return InlineKeyboardMarkup(keyboard)

def format_file_size(size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} TB"
