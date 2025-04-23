import os

class Config:
    # Telegram Bot Token
    BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")
    
    # API Configuration
    API_URL = "https://reddit.bdbots.xyz/dl?url="
    
    # Owner Information
    OWNER_USERNAME = "@blackmax_it"
    CHANNEL_LINK = "https://t.me/BDBOTS"
    GITHUB_REPO = "https://github.com/BDBOTS/Reddit-Downloader-Telegram-Bot"
    
    # Messages
    START_MESSAGE = """🌟 <b>Welcome to BDBOTS Reddit Video Downloader!</b> 🌟

Send me any Reddit video link and I'll download it for you in HD quality.

🔹 <i>Supported links:</i>
- Reddit video posts
- v.redd.it links
- Crossposted videos

📢 <a href="{channel_link}">Join our channel</a> for updates!
"""
    
    HELP_MESSAGE = """🆘 <b>How to use this bot:</b>

1. Simply send a Reddit video URL
2. The bot will fetch available qualities
3. Choose your preferred quality
4. Download the video directly!

📌 <b>Examples:</b>
- https://www.reddit.com/r/...
- https://v.redd.it/...
- https://reddit.com/r/.../comments/...

🔹 <b>Credits:</b>
- Developed by {owner}
- Powered by BDBOTS API
- Source code: {github_repo}
"""
