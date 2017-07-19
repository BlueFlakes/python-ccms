from prettytable import PrettyTable

def print_chat(chat):

    print('\n {:-<88}'.format(''))
    for message in chat:
        print("| {:>15}: {:<70}|".format(message[0], message[1]))
        print('|{:-<88}|'.format(''))


def get_message():
    message = input("""\nLeave your message
Or type 0 to exit: """)

    return message

def too_long_message():
    print("Your message is too long!")
