from View.table import Table
import getpass
import os


def get_inputs(title, questions_list):
    """
    Get imput form user

    Args:
        title (str): menu title
        questions_list (list): list of questions

    Return:
        temp (list): list with user inputs
    """

    temp = []

    if title:
        print('\033[92m' + title + ':' + '\033[0m')

    for question in questions_list:
        if question == "Password":
            temp.append(getpass.getpass())

        else:
            user_input = input(question + ': ')
            temp.append(user_input)

    if title:
        print()

    return temp


def print_menu(title, available_options, exit_message):
    """
    Show menu to user

    Args:
        title (str): menu title
        available_options (list): possible ways to operate in app
        exit_message (str): exit message
    """

    print(title+':')

    for i, option in enumerate(available_options):
        print("{}{}) {}".format('\t', str(i+1), option))

    else:
        print('{}{}) {}'.format('\t', '0', exit_message), end=2 * '\n')


def clear_window():
    os.system("clear")

def print_result(result):
    """
    Show results of action

    Args:
        result (str): print message with result to user
    """

    print(result)

def print_error_message(error_msg):
    """
    Print error message

    Args:
        error_msg (str):

    """
    print('\033[91m' + error_msg + '\033[0m', end=2*'\n')


def state_locker():
    import sys, tty, termios

    print('\nEnter anything to exit')
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def print_table(titles, data):
    """
    Print formatted table

    Args:
        title (string): title of table
        data (list of lists): list that contains details about persons as inner list
    """
    print(Table.table_creator(titles, data))
