# imports all models
from Models import codecooler, manager, mentor, office_manager, student

# imports all view modules
from View import codecooler_view, employee_view

# imports all controllers
from Controllers import codecooler_controller, employee_controller, manager_controller
from Controllers import mentor_controller, office_manager_controller, student_controller

from Controllers import tools
from Controllers import manager_controller
from Controllers import office_manager_controller
from Controllers import mentor_controller
from Controllers import student_controller
import data_manager


def main():
    data_manager.load_data_setup(manager_controller, student_controller, mentor_controller, office_manager_controller)
    codecooler_controller.login()


if __name__ == "__main__":
    main()
