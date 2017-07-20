from View import codecooler_view
from data_manager import DataManager
from Models.submit_assignment import SubmitAssignment
from Models.grade import Grade
from time import sleep


def start_controller(position, idx):
    """
    Determines user role in Codecool. Allow user perform assign tasks.

    Args:
        position (string): user role in Codecool
        assignments (list of :obj: `SubmitAssignment`): list of assigemts
        idx (string): uniqe student id
    """
    if position == "student":
        student_side(idx)
    elif position == "mentor":
        mentor_side()


def mentor_side():
    """
    Allow mentor to grade submited assigemts. Then list of assigemts is save to csv file.

    Args:
        submited_assignments (list of :obj: `SubmitAssignment`): list of assigemts
    """
    submited_assignments = SubmitAssignment.get_submit_assignments_list()
    user_choice = codecooler_view.get_inputs("Please provide task's name", ["Task"])[0]

    for submitted_task in submited_assignments:
        if user_choice == submitted_task.name:
            codecooler_view.clear_window()
            codecooler_view.print_result("Student idx: {} | Date: {}".format(submitted_task.idx, submitted_task.date))
            codecooler_view.print_result("Assignment name: {}".format(submitted_task.name))
            codecooler_view.print_result("Link: {}\n".format(submitted_task.link))

            task_grade = _grade_assigement()
            Grade(submitted_task.idx, user_choice, task_grade)

    codecooler_view.clear_window()

def student_side(idx):
    """
    Allows student to submit assignment

    Args:
        idx (string): uniqe student id
    """
    assignments = SubmitAssignment.get_submit_assignments_list()
    assignments_available = DataManager.read_file("csv/assignments.csv")
    args = codecooler_view.get_inputs("Submit your assignment", ["Link", "Assignment name"])

    for assgn in assignments_available:
        if args[1] == assgn[0]:
            assignments.append(SubmitAssignment(idx, args[0], args[1]))
            break

    else:
        codecooler_view.print_result("Wrong assignment name!\n")
        sleep(1.5)

def _grade_assigement():
    """
    Allow mentor to eval student's assigment by Danish scale. Show menu with grades assigne to menu options
    """

    grade = 0
    eval_categories = ["Stability", "Conform to requirements", "Python basics", "Git workflow", "Teamwork"]
    possible_eval_options = ["12.0 pts", "10.0 pts", "7.0 pts", "4.0 pts", "2.0 pts", "0.0 pts", "-1.0 pts", "-3.0 pts"]

    for category in eval_categories:
        user_choice = None

        while user_choice not in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
            codecooler_view.print_menu(category, possible_eval_options, "Exit evaluation for student")
            user_choice = codecooler_view.get_inputs("Please choose a number", ["Number"])[0]
            grades_scale = {'1': 12, '2': 10, '3': 7, '4': 4, '5': 2, '6': 0, '7': -1, '8': -3}

            if user_choice in grades_scale:
                grade += grades_scale[user_choice]

            else:
                codecooler_view.print_error_message('Wrong choice!')

        if user_choice == "0":
            grade = 0
            break

    return grade
