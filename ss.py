from xml.dom.minidom import Document
from telegram.ext import CommandHandler,Updater,Dispatcher,MessageHandler,Filters,CallbackContext,CallbackQueryHandler
import logging

token = "2016260844:AAGwWwI6ZLA7cLUNNcAbbFz2W84wkJebZyo"

def start(update, context):
    update.message.reply_text("wellcom")

def download(update, context):
    update.message.reply_text("the file is downloading")
    context.bot.sendPhoto(update.effective_chat.id, "./1.png")

def echo(update, context):
    update.message.reply_text(update.message.text)    

def main():
    updater = Updater(token, use_context=True)
    db = updater.dispatcher

    db.add_handler(CommandHandler("start", start))
    db.add_handler(CommandHandler("download", download))

    db.add_handler(CommandHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()