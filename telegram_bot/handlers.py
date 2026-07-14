from telegram import Update

from telegram.ext import ContextTypes


async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(

        "🤖 AI Investment Agent\n\n"

        "Welcome.\n\n"

        "Commands:\n"

        "/status"

    )


async def status_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(

        "AI Engine Online ✅"

    )