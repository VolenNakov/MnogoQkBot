from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import subprocess
 
sudoPassword = 'PASSWORD'
command = 'sudo arp-scan --interface=eth0 --plain 192.168.0.0/24 | cut -f 2'
p = 'echo %s|sudo -S %s' % (sudoPassword, command)

macs = {}


def check(bot, update):
    macs_rn = subprocess.getoutput(p)
    macs_array = macs_rn.split()
    chat_id = update.message.chat_id
    for i in macs_array:
        if macs.get(i):
            bot.send_message(chat_id=chat_id, text=macs[i])
        else:
            print("This is retarded: ", i)


def main():
    updater = Updater('API-TOKEN')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('check', check))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
