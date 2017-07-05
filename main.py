# imports all models
from Models import codecooler, employee, manager, mentor, office_manager, student

# imports all view modules
from View import codecooler_view, employee_view, manager_view, mentor_view, office_manager_view, student_view

# imports all controllers
from Controllers import codecooler_controller, employee_controller, manager_controller
from Controllers import mentor_controller, office_manager_controller, student_controller

from Models.student import Student


def main():
    codecooler_controller.CodecoolerController.login()


if __name__ == "__main__":
    main()
