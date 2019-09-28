from pprint import pprint
import telepot
from telepot.loop import MessageLoop
import time



def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    #should work thanks to Winston
    if msg['from']['id'] != 824389035:
        bot.sendMessage(chat_id, "Sorry this is a personal bot. Access Denied!")
        exit(1)
    print(command)
    if command == '/yes':
        bot.sendMessage(chat_id, "Calling Police")
    if command == '/no':
        bot.sendMessage(chat_id, "Ok ignoring now, send /cancel to stop monitoring")
    if command == '/cancel':
        bot.sendMessage(chat_id, "Aborted Monitoring. Click /start to start again")


