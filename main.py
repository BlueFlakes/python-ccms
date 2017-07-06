# imports all models
from Models import codecooler, employee, manager, mentor, office_manager, student

# imports all view modules
from View import codecooler_view, employee_view, manager_view, mentor_view, office_manager_view, student_view

# imports all controllers
from Controllers import codecooler_controller, employee_controller, manager_controller
from Controllers import mentor_controller, office_manager_controller, student_controller

from Controllers.tools import Tools
from Models.student import Student
from Models.manager import Manager

def main():
    idx = Tools.gen_idx("student")
    print(idx)
    Student.student_list.append(Student(idx, "password", "Jakub", "Janiszewski", "@cc"))

    idxx = Tools.gen_idx("mentor")
    print(idxx)
    mentor.Mentor.mentor_list.append(mentor.Mentor(idxx, "x", "x", "x", "@cc"))

    idx = Tools.gen_idx("manager")
    print(idx)
    Manager.manager_list.append(Manager(idx, "admin", "Kamil", "Konior", "@cc"))

    codecooler_controller.CodecoolerController.login()


if __name__ == "__main__":
    main()
