import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

async def start(update, context):
    await update.message.reply_text("Hi! I'm your bot. Send me anything and I'll echo it back.")

async def echo(update, context):
    await update.message.reply_text(update.message.text)

app = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("Bot is running...")
app.run_polling()
