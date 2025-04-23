🔴 Reddit Video Downloader Telegram Bot | BDBOTS
=======================================

![BDBOTS Logo](https://i.imgur.com/J8hqZ2W.png)

A stylish Telegram bot for downloading Reddit videos with multiple quality options

🌟 Features
-----------

*   🚀 **Instant Reddit video downloads**
*   🎥 **Multiple quality options** (HD + various SD resolutions)
*   📊 **Beautiful progress bar** during downloads
*   💫 **Elegant UI** with interactive buttons
*   ⚡ **Fast downloads** using BDBOTS API
*   📱 **Mobile-friendly** interface
*   🔄 **Cross-post support** for shared videos
*   📢 **Built-in promotion** for BDBOTS channels

🛠️ Setup
---------

### Prerequisites

*   Python 3.8+
*   Telegram bot token from [@BotFather](https://t.me/BotFather)

### Installation

    # Clone the repository
    git clone https://github.com/BDBOTS/Reddit-Downloader-Telegram-Bot.git
    cd Reddit-Downloader-Telegram-Bot
    
    # Install dependencies
    pip install -r requirements.txt
    
    # Create environment file
    echo "BOT_TOKEN=your_bot_token_here" > .env

### Running the Bot

    python bot.py

🖥️ For Production
------------------

For 24/7 operation, consider using:

    # Using PM2 process manager
    pm2 start bot.py --name "reddit-dl-bot" --interpreter python3

📸 Screenshots
--------------

![Start Message](https://i.imgur.com/example1.jpg)

Start Message

![Quality Selection](https://i.imgur.com/example2.jpg)

Quality Menu

![Download Progress](https://i.imgur.com/example3.jpg)

Progress Bar

![About Section](https://i.imgur.com/example4.jpg)

About Info

⚙️ Configuration
----------------

Edit `config.py` to customize:

    # Bot appearance and behavior
    START_MESSAGE = "Your custom welcome message..."
    
    # API endpoint (use your BDBOTS API)
    API_URL = "https://reddit.bdbots.xyz/dl?url=" 
    
    # Branding information
    OWNER_USERNAME = "@blackmax_it"
    CHANNEL_LINK = "https://t.me/BDBOTS"

🌐 API Reference
----------------

The bot uses the BDBOTS Reddit Downloader API:

    GET https://reddit.bdbots.xyz/dl?url={reddit_video_url}

Example Response:

    {
      "hd_link": "https://...",
      "sd_links": [
        {"quality": "720p", "url": "https://..."},
        {"quality": "480p", "url": "https://..."}
      ]
    }

🤝 Contributing
---------------

We welcome contributions! Please follow these steps:

1.  Fork the repository
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

📜 License
----------

Distributed under the MIT License. See `LICENSE` for more information.

📌 Credits
----------

*   **Developed by**: [BDBOTS Team](https://t.me/BDBOTS)
*   **Owner**: [@blackmax\_it](https://t.me/blackmax_it)
*   **API Provider**: [reddit.bdbots.xyz](https://reddit.bdbots.xyz)
*   **GitHub Repository**: [BDBOTS/Reddit-Downloader-Telegram-Bot](https://github.com/BDBOTS/Reddit-Downloader-Telegram-Bot)

🔗 Important Links
------------------

*   [Telegram Bot](https://t.me/YourBotUsername)
*   [BDBOTS Channel](https://t.me/BDBOTS)
*   [Owner Contact](https://t.me/blackmax_it)
*   [API Documentation](https://github.com/iSabbir/Reddit-Video-Downloader)

Built with ❤️ by [BDBOTS](https://t.me/BDBOTS)
