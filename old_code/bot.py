from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
import subprocess

command = 'ssh root@192.168.1.1 /etc/config/show_wifi_clients.sh'
device_types = ('tel', 'lap')

def get_known_macs():
    '''
    Parses ./known_macs.txt and returns it as a map
    '''
    known_macs = []
    with open('./known_macs.txt') as kn:
        for line in kn.readlines():
            mac, name = line.strip().split(' ')[:2]
            #known_macs[mac] = name.split('-')

            known_macs.append((mac, name))

    return known_macs

def check(bot, update):
    '''connected_macs = subprocess.getoutput(command).split()
    known_macs = get_known_macs()
    found_devices = set()
    ''''''
    A person can have multiple devices connected to the network.
    We should print his name in the list of those inside when his smartphone is connected,
    and print his name in the list of those outside when only his laptop is connected.
    ''''''

    for addr in connected_macs:
        if addr in known_macs:
            found_devices.add(known_macs[addr])
        else:
            print(f'Unknown mac address:{addr}', flush=True)

    inside_names = set(map(lambda n: n[0], filter(lambda n: n[1]=='tel', found_devices)))
    outside_names = set(map(lambda n: n[0], filter(lambda n: n[1]=='lap', found_devices))) - inside_names

    if len(found_namesiiikkk) == 0:
        message = 'Няма никой в Стаичката :<'
    else:
        message = 'Сега в Стаичката са:\n'
        for name in inside_names:
            message += f'- {name}\n'

        message += '\n'

        message = 'Do magazina sa:\n'
        for name in outside_names:
            message += f'- {name}\n'

    bot.send_message(chat_id=update.message.chat_id, text=message)
'''
    known_macs = get_known_macs();
    connected_macs = subprocess.getoutput(command).split()
    connectedNames = [];
    result = "В стаичката са: \n"
    for mac in connected_macs:
        test_print(mac)
        for macNamePair in known_macs:
            test_print("\t" + macNamePair[0] + ":" + macNamePair[1])
            if(mac == macNamePair[0]):
                connectedNames.append(macNamePair[1])
                test_print("bingo")
        test_print("\n")

    connectedNames.sort()
    connectedNamesUnique = []
    for el in connectedNames:
        if not el in connectedNamesUnique:
            connectedNamesUnique.append(el)
            result += "\t- " + el + "\n"

    bot.send_message(chat_id=update.message.chat_id, text=result)

test_logging_enable = False
def test_print(str):
    if(test_logging_enable):
        print(str)

def gay(bot, update):
    chat_id = update.message.chat_id
    if update.message.text == "gay":
        bot.send_message(chat_id=chat_id, text="no u")


def start(bot,update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text='За да проверите кой е в Стаичката, изпратете командата /check')
    
def main():
    updater = Updater('1366589208:AAFi2IXUhT3qLwN3nmYbTB3Qci5B0wrFcN4')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('check', check))
    dp.add_handler(CommandHandler('gay', gay))
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), gay))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
