# imports all models
from Models import codecooler, manager, mentor, office_manager, student

# imports all view modules
from View import codecooler_view, employee_view

# imports all controllers
from Controllers import codecooler_controller, employee_controller, manager_controller
from Controllers import mentor_controller, office_manager_controller, student_controller

from Controllers.tools import Tools
from Controllers.manager_controller import ManagerController
from Controllers.office_manager_controller import OfficeManagerController
from Controllers.mentor_controller import MentorController
from Controllers.student_controller import StudentController
import data_manager


def main():
    data_manager.load_data_setup(ManagerController, StudentController, MentorController, OfficeManagerController)
    codecooler_controller.CodecoolerController.login()


if __name__ == "__main__":
    main()
