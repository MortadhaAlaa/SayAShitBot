from telegram.ext import MessageHandler, CommandHandler, Filters, Updater
import os, logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

chat_ids = {]

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, 
                     text='''مرحبا بك عزيزي {} 😃🖐🏼.

هلااوو شلونككك اخبارك زين لو مو زين ضمصوب . 
المهم اَي هذا بوت تكدر تتواصل بي وي كل ادمنز قناة متت .'''.format(update.message.from_user.first_name))

def message(bot, update):
    m = bot.send_message(chat_id='-1001399878813', text=update.message.text)
    bot.send_message(chat_id=update.message.chat_id,
                     text='''شكرًا على ارسالك المسج حنرد عليك لمن نفتح 💙💙''')
    chat_ids[m.message_id] = update.message.chat_id
    #bot.forward_message(chat_id='-253860529', from_chat_id=update.message.chat_id, message_id=update.message.message_id)

def reply(bot, update):
    if update.message.chat_id != '-1001399878813':
        return
    original_m = update.message.reply_to_message
    original_chat = chat_ids[original_m.message_id]
    bot.send_message(chat_id=original_chat, text=update.message.text)
    
def error(bot, update, error):
     logging.warning('Update "%s" caused error "%s"' % (update, error))    
u = Updater(os.environ['TELEGRAM_TOKEN'])
d = u.dispatcher
d.add_handler(CommandHandler('start', start))
d.add_handler(MessageHandler(Filters.text&Filters.private, message))
d.add_handler(MessageHandler(Filters.text&Filters.reply, reply))
d.add_error_handler(error)

u.start_polling()
u.idle()
