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
from Models.office_manager import OfficeManager
from Controllers.manager_controller import ManagerController
from Controllers.office_manager_controller import OfficeManagerController
from Controllers.mentor_controller import MentorController
from Controllers.student_controller import StudentController
import data_manager



def main():
    data_manager.load_data_setup(ManagerController, StudentController, MentorController, OfficeManagerController)

    idx = Tools.gen_idx("student")
    print(idx)
    Student.student_list.append(Student(idx, "password", "Jakub", "Janiszewski", "@cc"))

    idx = Tools.gen_idx("office")
    print(idx)
    OfficeManager.office_managers_list.append(OfficeManager(idx, "office", "Miriam", "B", "@cc"))

    idxx = Tools.gen_idx("mentor")
    print(idxx)
    mentor.Mentor.mentor_list.append(mentor.Mentor(idxx, "x", "x", "x", "@cc"))

    idx = Tools.gen_idx("manager")
    print(idx)
    Manager.manager_list.append(Manager(idx, "admin", "Kamil", "Konior", "@cc"))

    codecooler_controller.CodecoolerController.login()

if __name__ == "__main__":
    main()
