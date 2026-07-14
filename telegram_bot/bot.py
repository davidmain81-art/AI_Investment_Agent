from dotenv import load_dotenv
import os

from telegram.ext import (
    Application,
    CommandHandler,
)

from telegram_bot.handlers import (
    start_command,
    status_command,
)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


def run_bot():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        CommandHandler(
            "start",
            start_command,
        )
    )

    app.add_handler(
        CommandHandler(
            "status",
            status_command,
        )
    )

    print("Telegram Bot Started...")

    app.run_polling()