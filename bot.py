from telegram import Update,ReplyKeyboardMarkup,ReplyKeyboardRemove,Bot,InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,CallbackQuery,ParseMode
from telegram.ext import CommandHandler,Updater,Dispatcher,MessageHandler,Filters,CallbackContext,CallbackQueryHandler
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

tkn = "2016260844:AAGwWwI6ZLA7cLUNNcAbbFz2W84wkJebZyo"
updater = Updater(tkn,use_context=True)
bot = Bot(tkn)
dispatcher : Dispatcher = updater.dispatcher

def start(update:Update, context:CallbackContext):
    firstname = update.effective_message.from_user.first_name
    chtiD = update.effective_message.chat_id
    username = update.effective_message.from_user.username
    txt = update.effective_message.text
    keyboard = [
        [KeyboardButton('Help')],
        [KeyboardButton('Contact us')]
    ]
    key = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)


    if txt=="Help":
        bot.send_message(
            chat_id=chtiD,
            text="How to Deploy Your Telegram bot on Heroku\n\nچگونه ربات خود را در Heroku راه اندازی کنید",
            reply_to_message_id=update.effective_message.message_id,
        )
    elif txt=="Contact us":
        bot.send_message(
            chat_id=chtiD,
            text="<u>سلام</u>Rexxar.ir\n\n<i>Telegram : </i>خوبی",
            reply_to_message_id=update.effective_message.message_id,
            parse_mode=ParseMode.HTML
        )
    else:
        bot.send_message(
            chat_id=chtiD,
            text=f"نام کاربری شما {firstname}" + f"\n\nیوزرنیم شما : {username}" + f"\n\nآیدی عددی شما : {str(chtiD)}",
            reply_to_message_id=update.effective_message.message_id,
            reply_markup=key


        )

def main():

    dispatcher.add_handler(MessageHandler(Filters.text,start))
    updater.start_polling()


if __name__ == '__main__':
    main()
