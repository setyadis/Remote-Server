import subprocess
import os
import time
import telegram

from telegram.ext import Updater
from telegram.ext import CommandHandler
from subprocess import Popen

h = os.popen('hostname')
nama = h.read()

p = os.popen('pwd')
direk = p.read()

l = os.popen('ls -lrt')
isi = l.read()

t = subprocess.Popen(["ls", "-lrt"], stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
lihat = t.stdout.read()

df = os.popen('df -kh')
memori = df.read()

def mulai(bot, update):
    update.message.reply_text('Welcome {}'.format(update.message.from_user.first_name))
    update.message.reply_text('Silahkan berikan command linux = /hostname, /pwd, /ls, /tail, /space ')

def hostname(bot, update):
        update.message.reply_text(
        nama
        )

def pwd(bot, update):
        update.message.reply_text(
        direk
        )

def ls(bot, update):
        update.message.reply_text(
        isi
        )

def tail(bot, update):
        update.message.reply_text(
        lihat
        )

def space(bot, update):
        update.message.reply_text(
        memori
        )

def exec(bot, update, args):
    commands = ' '.join(args)
    print(commands)
    user = update.message.from_user.username
    mesin = args[0]
    perintah = args[1]
    #pesanku = ' '.join(commands.split()[1:])
    pesan = ' '.join(commands.replace("$","\$").split()[1:])
    
    userlist = [line.strip() for line in open("/root/allblue/listAccessUser.txt", 'r')]
    list = [line.strip() for line in open("/root/allblue/listCommandBanned.txt", 'r')]
    if (user in userlist):
       if (perintah in list):
          p='command tidak boleh digunakan'
          print(p)
          update.message.reply_text(p)
       else:
          if len(mesin.split('.')) == 4:
             cek=1
             while cek==1:
               try:
                 perintah = 'ssh {} {}'.format(mesin, pesan)
                 print(perintah)
                 hasil = os.popen(perintah)
                 texting = hasil.read()
                 update.message.reply_text(texting)
                 print("command berhasil....")
                 cek =2
               except:
                 print("ssh not successfull"+mesin)
                 update.message.reply_text("ssh not successfull"+mesin)
                 cek =2
          else:
             hasil = os.popen(commands)
             print(hasil)
             textting = hasil.read()
             update.message.reply_text(textting)
    else:
       pi='Kau tak bisa pakai bot ini'
       print(pi)
       update.message.reply_text(pi)
cek=1

updater = Updater('314762661:AAHA2a-LKZvnrFPevaR-u5X7JeidjZxotks')

updater.dispatcher.add_handler(CommandHandler('mulai', mulai))
updater.dispatcher.add_handler(CommandHandler('hostname', hostname))
updater.dispatcher.add_handler(CommandHandler('pwd', pwd))
updater.dispatcher.add_handler(CommandHandler('ls', ls))
updater.dispatcher.add_handler(CommandHandler('tail', tail))
updater.dispatcher.add_handler(CommandHandler('space', space))
updater.dispatcher.add_handler(CommandHandler('exec', exec, pass_args=True))

updater.start_polling()
updater.idle()
