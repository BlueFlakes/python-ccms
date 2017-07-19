from prettytable import PrettyTable, ALL, NONE
from View import codecooler_view

def print_chat(chat):
    prettytable = PrettyTable(header=False, hrules=ALL, vrules=NONE)

    for message in chat:
        sentence = ': ' + message[1]
        author = message[0]
        prettytable.add_row([author, sentence])

    prettytable.align = 'l'
    print(prettytable)


def get_message():
    message = codecooler_view.get_inputs('', ['\nLeave your message Or type 0 to exit'])[0]
    return message

def too_long_message():
    print("Your message is too long!")
