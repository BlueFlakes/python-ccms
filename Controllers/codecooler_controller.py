from Models.codecooler import Codecooler
from Models.mentor import Mentor
from Models.student import Student
from Models.office_manager import OfficeManager
from Models.manager import Manager
from View import codecooler_view
from Controllers import student_controller
from Controllers import mentor_controller
from Controllers import manager_controller
from Controllers import office_manager_controller
from random import randint


def login():
    """
    Check if user of given id exist and entered correct password
    """

    found = False
    mergedlist = Student.student_list + Mentor.mentor_list + OfficeManager.office_managers_list + Manager.manager_list

    while not found:
        passes = codecooler_view.get_inputs("Please provide your login and password", ["Login", "Password"])
        idx, password = passes[0], passes[1]

        for ccooler in mergedlist:
            if idx == ccooler.idx and password == ccooler.password:
                start_controller(ccooler)
                found = True
                break

        if not found:
            codecooler_view.print_result("Wrong login or password!\n")


def start_controller(ccooler):
    """
    Start proper part of program depending on user's role

    Args:
        ccooler (:obj:): objest representing user

    Examples:
        Use can have role of Manager, Office Employee, Mentor or Student
    """

    if ccooler.__class__.__name__ == "Student":
        student_controller.start_controller(ccooler.name, ccooler.surname, ccooler.idx)
    elif ccooler.__class__.__name__ == "Mentor":
        mentor_controller.start_controller(ccooler.name, ccooler.surname, ccooler.idx)
    elif ccooler.__class__.__name__ == "Manager":
        manager_controller.start_controller(ccooler.name, ccooler.surname, ccooler.idx)
    elif ccooler.__class__.__name__ == "OfficeManager":
        office_manager_controller.start_controller(ccooler.name, ccooler.surname)
