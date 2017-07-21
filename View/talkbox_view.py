from prettytable import PrettyTable, ALL, NONE
from View import codecooler_view


def print_chat(chat):
    """
    Print Talkbox in formatted way

    Args:
        chat (:obj: Talkbox): object with all users masseges
    """

    prettytable = PrettyTable(header=False, hrules=ALL, vrules=NONE)

    for message in chat:
        author, sentence = message.compilated_message()
        prettytable.add_row([author, ': ' + sentence])

    prettytable.align = 'l'
    print(prettytable)


def get_message():
    """
    Get user massage to chat
    """
    message = codecooler_view.get_inputs('', ['\nLeave your message Or type 0 to exit'])[0]
    return message


def too_long_message():
    """
    Error massage
    """

    codecooler_view.print_error_message("Your message is too long!")
