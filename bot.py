from pprint import pprint
import time,os
from datetime import datetime
import telepot
from telepot.loop import MessageLoop

from bantuan import bantuan

waktu = datetime.now()
tahun = waktu.year
bulan = waktu.month
hari = waktu.day
jam = waktu.hour
menit = waktu.minute
detik = waktu.second

bot = telepot.Bot('123123123121:AAAAVVVBBGV2vchhGGSgg_vsgdvgs')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    chat_id = msg['chat']['id']
    text = msg['text']
    #sender = msg['from']['id']
    sender = msg['from']['username']
    f = open('access.log', 'a')
    f.write("{}-{}-{} {}:{}:{}".format(hari, bulan, tahun, jam, menit, detik)+" Chat-id - "+str(chat_id)+" Text - "+str(text)+" Sender - "+sender+"\n")
    f.close()
    args=text.split()
    command = args[0]

    print ('Received: %s' % command)

    print(content_type, chat_type, chat_id)

    if command == '/start':
        output = bantuan
        bot.sendMessage(chat_id, output)
    if command == '/bantuan':
        output = bantuan
        bot.sendMessage(chat_id, output)

    if command == '/malcode':
        keyword = str(args[1])
        output = os.popen("python malc0de.py --url "+keyword).read().rstrip('\n')
        bot.sendDocument(chat_id, document=open('malcode/%s' % output))

#bot.message_loop(handle)
print (bot.getMe())
MessageLoop(bot, handle).run_as_thread()

print ('Indehoiiiiii')

while 1:
    time.sleep(10)
