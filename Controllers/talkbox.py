from View import talkbox_view, codecooler_view
from data_manager import DataManager
from time import sleep

def start_talkbox(name, surname):
    name = name + " " + surname
    chat = DataManager.read_file("csv/talkbox.csv")

    chat = start_chat(chat, name)
    codecooler_view.clear_window()
    DataManager.save_file("csv/talkbox.csv", chat)


def start_chat(chat, name):
    message = 1
    while not message == "0":
        talkbox_view.print_chat(chat)
        message = talkbox_view.get_message()

        if len(message) > 70:
            talkbox_view.too_long_message()
            sleep(1.5)
        elif message != "0":
            chat.append([name, message])

        chat = archive(chat)

    return chat

def archive(chat):
    if len(chat) > 20:
        chat = chat[-20:]

    return chat
