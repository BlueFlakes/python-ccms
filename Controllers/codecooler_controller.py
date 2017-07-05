from Models.codecooler import Codecooler
from View.codecooler_view import CodecoolerView
from Models.mentor import Mentor
from Models.student import Student


class CodecoolerController:

    @classmethod
    def login(self):
        passes = CodecoolerView.get_inputs("Please provide your login and password", ["Login", "Password"])
        login, password = passes[0], passes[1]
        mergedlist = Student.student_list + Mentor.mentor_list

        found = False
        for ccooler in mergedlist:
            if login == ccooler.name and password == ccooler.surname:
                self.start_controller(ccooler)
                found = True
                break

        if not found:
            print("Wrong login or password!")

    def start_controller(self, ccooler):
        if ccooler.__class__.__name__ == "Student":
            StudentController.start_controller(ccooler.name, ccooler.surname)
        elif ccooler.__class__.__name__ == "Mentor":
            MentorController.start_controller(ccooler.name, ccooler.surname)
        elif ccooler.__class__.__name__ == "Manager":
            ManagerController.start_controller(ccooler.name, ccooler.surname)
        elif ccooler.__class__.__name__ == "OfficeManager":
            OfficeManagerController.start_controller(ccooler.name, ccooler.surname)
