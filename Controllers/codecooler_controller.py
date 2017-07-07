from Models.codecooler import Codecooler
from View.codecooler_view import CodecoolerView
from Models.mentor import Mentor
from Models.student import Student
from Models.office_manager import OfficeManager
from Models.manager import Manager
from Controllers.student_controller import StudentController
from Controllers.mentor_controller import MentorController
from Controllers.manager_controller import ManagerController
from Controllers.office_manager_controller import OfficeManagerController
from random import randint


class CodecoolerController:
    """This class contain logic to proper user login and start his/her part of program"""

    @classmethod
    def login(cls):
        """
        Check if user of given id exist and entered correct password
        """

        found = False
        mergedlist = Student.student_list + Mentor.mentor_list + OfficeManager.office_managers_list + Manager.manager_list

        while not found:
            passes = CodecoolerView.get_inputs("Please provide your login and password", ["Login", "Password"])
            idx, password = passes[0], passes[1]

            for ccooler in mergedlist:
                if idx == ccooler.idx and password == ccooler.password:
                    cls.start_controller(ccooler)
                    found = True
                    break

            if not found:
                CodecoolerView.print_result("Wrong login or password!\n")

    @classmethod
    def start_controller(cls, ccooler):
        """
        Start proper part of program depending on user's role

        Args:
            ccooler (:obj:): objest representing user

        Examples:
            Use can have role of Manager, Office Employee, Mentor or Student
        """

        if ccooler.__class__.__name__ == "Student":
            StudentController.start_controller(ccooler.name, ccooler.surname, ccooler.idx)
        elif ccooler.__class__.__name__ == "Mentor":
            MentorController.start_controller(ccooler.name, ccooler.surname, ccooler.idx)
        elif ccooler.__class__.__name__ == "Manager":
            ManagerController.start_controller(ccooler.name, ccooler.surname, ccooler.idx)
        elif ccooler.__class__.__name__ == "OfficeManager":
            OfficeManagerController.start_controller(ccooler.name, ccooler.surname)
