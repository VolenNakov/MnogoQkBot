from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
import os
from os.path import join, dirname
import json

load_dotenv("./.env")
BOT_TOKEN = os.environ.get("BOT_TOKEN")


def check(update, context):
    macs = os.popen('sudo arp-scan -l --plain | cut -f 2').read()
    macs.splitlines()
    path = join(dirname(__file__), 'macs.json')
    with open(path) as f:
        devices = json.load(f)
    people = []
    for mac in macs:
        try:
            people.append(devices[mac])
        except KeyError:
            continue
    peopleFiltered = list(set(people))
    message = "Сеаг в Стаичката са:"
    for person in peopleFiltered:
        message += "\n"+"    -"+person
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=message)


def gay(update, context):
    chat_id = update.message.chat_id
    if update.message.text == "gay":
        context.bot.send_message(chat_id=chat_id, text="no u")


def start(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(
        chat_id=chat_id, text='За да проверите кой е в Стаичката, изпратете командата /check')


def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('check', check))
    dp.add_handler(CommandHandler('gay', gay))
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), gay))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
