from telegram import Chat, Update,ReplyKeyboardMarkup,ReplyKeyboardRemove,Bot,InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,CallbackQuery,ParseMode
from telegram.ext import CommandHandler,Updater,Dispatcher,MessageHandler,Filters,CallbackContext,CallbackQueryHandler
import logging
# from mutagen.mp3 import MP3
# from mutagen.id3 import ID3, APIC, error

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

tkn = "2016260844:AAGwWwI6ZLA7cLUNNcAbbFz2W84wkJebZyo"
updater = Updater(tkn, use_context=True)
bot = Bot(tkn)
dispatcher : Dispatcher = updater.dispatcher

def start(update:Update, context:CallbackContext):
    # file = context.bot.get_file(update.message.document.file_id)
    # file.download(update.message.document.file_name)
    # doc = update.message.document

    firstname = update.effective_message.from_user.first_name
    chtiD = update.effective_message.chat_id
    username = update.effective_message.from_user.username
    txt = update.effective_message.text
    # اینجا یک متغییر تعریف کردیم برای ساخت دکمه شیشه ای
    # زمانی که کاربر بر روی هر کدام از دکمه های زیر کلیک میکن
    # متن داخل بعنوان یک تکست برای ربات ارسال شده و شرط مورد نظر 
    # انجام میشود
    keyboard = [
        [KeyboardButton('Start')],
        [KeyboardButton('Contact us')],
        [KeyboardButton('Help')], 
        [KeyboardButton('File')]
    ]
    key = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)

    if txt == "Contact Us":
        bot.send_message(
            chat_id = chtiD,
            text = "سلام حالتون چطوره", 
            reply_to_message_id=update.effective_message.message_id,
        )
    elif txt == "Help":
        bot.send_message(
            chat_id = chtiD,
            text="How to Deploy Your Telegram bot on Heroku\n\nچگونه ربات خود را در Heroku راه اندازی کنید",
            reply_to_message_id=update.effective_message.message_id,
        )
    elif txt == "Start":
        bot.send_message(
            chat_id = chtiD,
            text="<u>سلام</u>\n\n<i>Telegram : </i>خوبی",
            reply_to_message_id=update.effective_message.message_id,
            parse_mode=ParseMode.HTML
        )
    # elif txt == "File":
    #     bot.send_message(
    #         chat_id = chtiD,
    #         text = f"{file}",
    #         reply_to_message_id=update.effective_message.message_id,
    #     )
    else:
        bot.send_message(
            chat_id=chtiD,
            text=f"نام کاربری شما {firstname}" + f"\n\nیوزرنیم شما : {username}" + f"\n\nآیدی عددی شما : {str(chtiD)}" + "سلام مصطفی حالت چطوره",
            reply_to_message_id=update.effective_message.message_id,
            reply_markup=key


        )

def main():

    # برای مدیریت پیام های غیر دستوری از کلاس
    # MessageHandler
    # استفاده میکنیم منظور پیام هایی که بتعرفشان نکردیم
    dispatcher.add_handler(MessageHandler(Filters.text,start))

    # متد زیر برای ران کردن بات است
    updater.start_polling()


if __name__ == '__main__':
    main()
