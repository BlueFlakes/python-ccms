from View import codecooler_view
from data_manager import DataManager
from Models.submit_assignment import SubmitAssignment
from time import sleep
import os


def start_controller(position, assignments, idx):
    """
    Determines user role in Codecool. Allow user perform assign tasks.

    Args:
        position (string): user role in Codecool
        assignments (list of :obj: `SubmitAssignment`): list of assigemts
        idx (string): uniqe student id
    """

    if position == "student":
        student_side(assignments, idx)
    elif position == "mentor":
        mentor_side(assignments)


def mentor_side(submited_assignments):
    """
    Allow mentor to grade submited assigemts. Then list of assigemts is save to csv file.

    Args:
        submited_assignments (list of :obj: `SubmitAssignment`): list of assigemts
    """
    task = codecooler_view.get_inputs("Please provide task's name", ["Task"])
    task = task[0]

    for student_submit in submited_assignments:
        if task == student_submit[2]:

            codecooler_view.print_result("Student idx: {} | Date: {}".format(student_submit[0], student_submit[3]))
            codecooler_view.print_result("Assignment name: {}".format(student_submit[2]))
            codecooler_view.print_result("Link: {}\n".format(student_submit[1]))

            grade = _grade_assigement()
            DataManager.extend_file("csv/grades.csv", [student_submit[0], task, grade])


def student_side(assignments, idx):
    """
    Allows student to submit assignment

    Args:
        idx (string): uniqe student id
    """

    assignments_available = DataManager.read_file("csv/assignments.csv")
    args = codecooler_view.get_inputs("Submit your assignment", ["Link", "Assignment name"])

    for assgn in assignments_available:
        if args[1] == assgn[0]:
            assignments.append(SubmitAssignment(idx, args[0], args[1]))
            break
    else:
        codecooler_view.print_result("Wrong assignment name!")
        sleep(1.5)


def _grade_assigement():
    """
    Allow mentor to eval student's assigment by Danish scale. Show menu with grades assigne to menu options
    """

    grade = 0
    eval_categories = ["Stability", "Conform to requirements", "Python basics", "Git workflow", "Teamwork"]
    possible_eval_options = ["12.0 pts", "10.0 pts", "7.0 pts", "4.0 pts", "2.0 pts", "0.0 pts", "-1.0 pts", "-3.0 pts"]

    for category in eval_categories:
        option = None

        while option not in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
            codecooler_view.print_menu(category, possible_eval_options, "Exit evaluation for student")
            option = codecooler_view.get_inputs("Please choose a number", ["Number"])[0]

            if option == "1":
                grade += 12
            elif option == "2":
                grade += 10
            elif option == "3":
                grade += 7
            elif option == "4":
                grade += 4
            elif option == "5":
                grade += 2
            elif option == "6":
                grade += 0
            elif option == "7":
                grade -= 1
            elif option == "8":
                grade -= 3
            elif option == "0":
                break
            else:
                print("Wrong option")

    os.system("clear")
    return grade
