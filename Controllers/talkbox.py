from View import talkbox_view, codecooler_view
from Models.talkbox import TalkBox
from Models.message import Message
from data_manager import DataManager
from time import sleep


def start_talkbox(name, surname):
    """
    Start talkbox

    Args:
        name (string): user name
        surname (string): user surname
    """

    name = name + " " + surname
    start_chat(name)


def start_chat(name):
    """
    Contain logic for talkbox. Call function to print previous 20 massages
    and add new write by user. Also validate if new masseg isn't too long.
    """

    received_message = None

    while received_message != "0":
        talkbox_view.print_chat(TalkBox.get_talkbox()[::-1])
        received_message = talkbox_view.get_message()
        codecooler_view.clear_window()

        if len(received_message) > 70:
            talkbox_view.too_long_message()
            sleep(1.5)

        elif received_message != "0":
            TalkBox.add_message(name, received_message)
