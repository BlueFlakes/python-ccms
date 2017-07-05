from Models.codecooler import Codecooler
from View.codecooler_view import CodecoolerView
from Models.mentor import Mentor
from Models.student import Student
from Controllers.student_controller import StudentController
from Controllers.mentor_controller import MentorController
from Controllers.manager_controller import ManagerController
from Controllers.office_manager_controller import OfficeManagerController


class CodecoolerController:

    @classmethod
    def login(cls):
        passes = CodecoolerView.get_inputs("Please provide your login and password", ["Login", "Password"])
        login, password = passes[0], passes[1]
        mergedlist = Student.student_list + Mentor.mentor_list

        found = False
        for ccooler in mergedlist:
            if login == ccooler.name and password == ccooler.surname:
                cls.start_controller(ccooler)
                found = True
                break

        if not found:
            print("Wrong login or password!")

    @classmethod
    def start_controller(cls, ccooler):
        if ccooler.__class__.__name__ == "Student":
            StudentController.start_controller(ccooler.name, ccooler.surname)
        elif ccooler.__class__.__name__ == "Mentor":
            MentorController.start_controller(ccooler.name, ccooler.surname)
        elif ccooler.__class__.__name__ == "Manager":
            ManagerController.start_controller(ccooler.name, ccooler.surname)
        elif ccooler.__class__.__name__ == "OfficeManager":
            OfficeManagerController.start_controller(ccooler.name, ccooler.surname)
