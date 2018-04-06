from telegram.ext import MessageHandler, CommandHandler, Filters, Updater
import os, logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, 
                     text='''هلا بيكم ببوت ARZ 🌻
دز اي شي و حيوصل للادمنية بصورة مجهولة''')

def message(bot, update):
    bot.send_message(chat_id='-1001343883321', text=update.message.text)
    bot.send_message(chat_id=update.message.chat_id,
                     text='''هلاو برو 
رسالتك وصلت لمقر القيادة حيجاوبون عليها من يشوفوها 🌻''')
    #bot.forward_message(chat_id='-253860529', from_chat_id=update.message.chat_id, message_id=update.message.message_id)

def error(bot, update, error):
     logging.warning('Update "%s" caused error "%s"' % (update, error))    
u = Updater(os.environ['TELEGRAM_TOKEN'])
d = u.dispatcher
d.add_handler(CommandHandler('start', start))
d.add_handler(MessageHandler(Filters.text&Filters.private&(~Filters.reply), message))
d.add_error_handler(error)

u.start_polling()
u.idle()
