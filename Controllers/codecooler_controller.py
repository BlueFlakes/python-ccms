from codecooler import Codecooler
from codecooler_view import CodecoolerView
from mentor import Mentor
from student import Student


class CodecoolerController:

    def login(self):
        passes = CodecoolerView.get_inputs("Please provide your login and password", ["Login", "Password"])
        login, password = passes[0], passes[1]
        mergedlist = Student.student_list + Mentor.mentor_list

        found = False
        for ccooler in mergedlist:
            if login == ccooler.name and password == ccooler.surname:
                ccooler.print_menu()
                found = True
                break

        if not found:
            print("Wrong login or password!")
