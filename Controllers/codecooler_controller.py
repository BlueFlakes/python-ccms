import os
from Models.codecooler import Codecooler
from View.codecooler_view import CodecoolerView
from Models.mentor import Mentor
from Models.student import Student
from Controllers.student_controller import StudentController
from Controllers.mentor_controller import MentorController
from Controllers.manager_controller import ManagerController
from Controllers.office_manager_controller import OfficeManagerController
from random import randint


class CodecoolerController:

    @classmethod
    def login(cls):
        found = False
        mergedlist = Student.student_list + Mentor.mentor_list

        while not found:
            passes = CodecoolerView.get_inputs("Please provide your login and password", ["Login", "Password"])
            login, password = passes[0], passes[1]

            for ccooler in mergedlist:
                if login == ccooler.login and password == ccooler.password:
                    os.system("clear")
                    cls.start_controller(ccooler)
                    found = True
                    break

            if not found:
                CodecoolerView.print_result("Wrong login or password!\n")

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

    @staticmethod
    def gen_idx(position):
        types_dict = {"student": "st", "mentor": "mt", "office": "ofc", "manager": "mgr"}
        random_numbers = [str(randint(0, 9)) for number in range(4)]

        if position in types_dict:
            idx = types_dict[position] + random_numbers[0] + random_numbers[1] + random_numbers[2] + random_numbers[3]
            return idx
