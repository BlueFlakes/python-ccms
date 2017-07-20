from Models.attendance import AttendanceModel
from Models.student import Student
from View import codecooler_view
from datetime import date, datetime
from time import sleep
from data_manager import DataManager


def start_controller(students_displayable_formated_data):
    """
    Contain main logic for AttendanceController.
    """
    students = Student.get_students_list()
    students_attendance = AttendanceModel.get_attendance_list()
    user_choice = None
    menu_options = ["Check attendnace", "View student attendance"]

    while user_choice != "0":
        codecooler_view.clear_window()

        codecooler_view.print_menu("Student's attendance menu", menu_options, "Exit")
        user_choice = codecooler_view.get_inputs("Please choose a number", ["Number"])[0]


        if user_choice == "1":
            _check_attendance(students_attendance, students)

        elif user_choice == "2":
            display_student_list(students_displayable_formated_data)
            choosen_student = codecooler_view.get_inputs("Student attendance detail", ["Student idx"])
            attendance_student_list = _get_attendnace_list(students_attendance, choosen_student[0])
            _calculate_attendnace(students_attendance, choosen_student[0])

    codecooler_view.clear_window()


def _calculate_attendnace(students_attendance, given_student_idx):
    """
    Print attendnace for student with given idx in percent

    Args:
        students_attendance (list of :obj: `AssigementModels`): list with detail of attendance for all students
        student_idx (str): uniqe id number of student
    """
    attendance_sum = 0
    max_possible_attendance = 0

    for student in students_attendance:
        if student.student_idx == given_student_idx:
            attendance_sum += float(student.state)
            max_possible_attendance += 1

    try:
        attendance_procent = round(((attendance_sum/max_possible_attendance)*100), 2)

    except ZeroDivisionError:
        print("This student have no attendance")
        sleep(1.5)

    else:
        print("Student attendance {}%\n".format(attendance_procent))
        codecooler_view.state_locker()

def _check_attendance(students_attendance, students):
    """
    Add AttendanceModel object to proper list.

    Args:
        students_attendance (list of :obj: `AssigementModels`): list with detail of attendance for all students
        students (list of :obj: `StudentModels`):list with detail of all students
    """
    current_date = date.today()
    for student in students:

        try:
            _vaildate_correct_date(current_date, student, students_attendance)
        except ValueError as err:
            print(err)
            codecooler_view.state_locker()
            continue

        user_choice = None
        attendance_state = None
        check_attendance_person = "Check attendance for {} {}".format(student.name, student.surname)

        while user_choice not in ["0", "1", "2", "3"]:
            codecooler_view.print_menu(check_attendance_person, ["Present", "Not presaent", "Late"], "Exit")
            user_choice = codecooler_view.get_inputs("Please choose a number", ["Number"])[0]
            attendance_values = {'1': 1, '2': 0.0, '3': 0.8}

            if user_choice in attendance_values:
                attendance_state = attendance_values[user_choice]

            else:
                codecooler_view.print_error_message('Wrong option!')

        if attendance_state:
            student_attendance = AttendanceModel(student.idx, current_date, attendance_state)
            students_attendance.append(student_attendance)


def _get_attendnace_list(students_attendance, student_idx):
    """
    Create list of attendnace detail for student with given idx

    Args:
        students_attendance (list of :obj: `AssigementModels`): list with detail of attendance for all students
        student_idx (str): uniqe id number of student

    Returns:
        list of list: str: list of attendnace detail for student with given idx
    """
    attendance_student_list = []
    for attendance in students_attendance:
        if attendance.student_idx == student_idx:
            attendance_student_list.append(attendance)

    return attendance_student_list


def display_student_list(students):
    """
    Call functions to display formatted table with Student object details
    """
    titles = ["Idx", "Password", "Name", "Surname", "Email"]
    codecooler_view.print_table(titles, students)


def _vaildate_correct_date(current_date, student, students_attendance):
    """
    Check if student's attendance wasn't check today jet

    Args:
        current_date (datetime :obj:): today date as year, month, day
        student (Student :obj:): object representation of student person
        students_attendance (list of datetime :obj:): all students attendance list
    """
    for attendance in students_attendance:
        if attendance.student_idx == student.idx:
            if attendance.date == current_date:
                error_msg = "Attendance for {} {} was check today".format(student.name, student.surname)
                raise ValueError(error_msg)
