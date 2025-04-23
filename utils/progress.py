from telegram import Update
from telegram.ext import CallbackContext
from tqdm import tqdm
import time

class DownloadProgressBar:
    def __init__(self, update: Update, context: CallbackContext):
        self.update = update
        self.context = context
        self.last_update_time = 0
        self.progress_message = None
        
    def __call__(self, chunk_number, chunk_size, total_size):
        if total_size == -1:
            return
        
        percent = (chunk_number * chunk_size) / total_size * 100
        
        # Update every 1 second to avoid spamming
        current_time = time.time()
        if current_time - self.last_update_time > 1 or percent >= 100:
            self.last_update_time = current_time
            
            bar_length = 20
            filled_length = int(bar_length * percent / 100)
            bar = '⬢' * filled_length + '⬡' * (bar_length - filled_length)
            
            message = (
                f"📥 Downloading: {percent:.1f}%\n"
                f"{bar}\n"
                f"🔄 {self._format_size(chunk_number * chunk_size)} / {self._format_size(total_size)}"
            )
            
            if not self.progress_message:
                self.progress_message = self.update.message.reply_text(message)
            else:
                try:
                    self.context.bot.edit_message_text(
                        chat_id=self.update.effective_chat.id,
                        message_id=self.progress_message.message_id,
                        text=message
                    )
                except:
                    pass
    
    @staticmethod
    def _format_size(size):
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"
