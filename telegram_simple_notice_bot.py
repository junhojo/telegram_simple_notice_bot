from apscheduler.schedulers.background import BackgroundScheduler
from telegram.ext import Updater, CommandHandler
import sched

#pip install apscheduler
#http://apscheduler.readthedocs.io/en/3.0/modules/triggers/cron.html#module-apscheduler.triggers.cron

def notiMessage(bot, update):
    update.message.reply_text('[공지] 주간업무를 공유해 주세요')

def start(bot, update):
    # sched.add_job(notiMessage, 'cron', second='*/5', id="test_1", args=[bot, update])
    #sched.add_job(notiMessage, 'cron', second='0 30 13 ? * WED *', id="test_1", args=[bot, update])
    sched.add_job(notiMessage, 'cron', day_of_week='wed', hour="13", minute='03', second='00', id="notice", args=[bot, update])

sched = BackgroundScheduler()
sched.start()
updater = Updater('11111111111:222222222222233333-6o7jnf8')
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
updater.idle()

