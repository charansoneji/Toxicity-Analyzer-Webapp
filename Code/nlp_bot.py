import logging

from predict import prediction
from telegram.ext import Updater, MessageHandler, Filters


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def my_func(bot, update):
    pass
    if not update.effective_message.text:
            update.effective_message.reply_text(text = "Cannot handle given format, getting aware now")
    else:
        msg = update.effective_message.text
        update.effective_message.reply_text(text = prediction(msg))
        
def main():
    updater = Updater('1076597208:AAH8whDdXKhF9xgSMj1P50EzZ-3JATLuaLs')
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.all, my_func))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
