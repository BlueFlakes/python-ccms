# imports all models
from Models import codecooler, employee, jerzy, mentor, miriam, student

# imports all view modules
from View import codecooler_view, employee_view, jerzy_view, mentor_view, miriam_view, student_view

# imports all controllers
from Controllers import codecooler_controller, employee_controller, jerzy_controller
from Controllers import mentor_controller, miriam_controller, student_controller


def main():
    codecooler_controller.CodecoolerController.login()


if __name__ == "__main__":
    main()
