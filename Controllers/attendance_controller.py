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
    students = Student.student_list
    students_attendance = _create_students_attendance_list()
    option = 0
    menu_options = ["Check attendnace", "View student attendance"]
    while not option == "0":
        codecooler_view.clear_window()

        codecooler_view.print_menu("Student's attendance menu", menu_options, "Exit")
        options = codecooler_view.get_inputs("Please choose a number", ["Number"])
        option = options[0]

        if option == "1":
            _check_attendance(students_attendance, students)
        elif option == "2":
            display_student_list(students_displayable_formated_data)
            choosen_student = codecooler_view.get_inputs("Student attendance detail", ["Student idx"])
            attendance_student_list = _get_attendnace_list(students_attendance, choosen_student[0])
            _calculate_attendnace(students_attendance, choosen_student[0])


    codecooler_view.clear_window()
    _save_attendance(students_attendance)


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

        attendance_option = None
        attendance_state = None
        check_attendance_person = "Check attendance for {} {}:".format(student.name, student.surname)
        while attendance_option not in ["0", "1", "2", "3"]:
            codecooler_view.print_menu(check_attendance_person, ["Present", "Not presaent", "Late"], "Exit")
            attendance_options = codecooler_view.get_inputs("Please choose a number", ["Number"])
            attendance_option = attendance_options[0]

            if attendance_option == "1":
                attendance_state = 1.0
            elif attendance_option == "2":
                attendance_state = 0.0
            elif attendance_option == "3":
                attendance_state = 0.8
            else:
                print("Wrong option")

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


def _create_students_attendance_list():
    """
    Convert data from csv file to AttendanceModel object and add it to list
    """
    students_attendance = []
    attendance_list = DataManager.read_file("csv/attendance.csv")

    try:
        if attendance_list:
            for attendance_detail in attendance_list:
                student_idx = attendance_detail[0]
                attendance_date = datetime.strptime(attendance_detail[1], "%Y-%m-%d").date()
                attendance_state = attendance_detail[2]

                attendnace = AttendanceModel(student_idx, attendance_date, attendance_state)
                students_attendance.append(attendnace)

    except IndexError:
        pass

    return students_attendance

def display_student_list(students):
    """
    Call functions to display formatted table with Student object details
    """
    titles = ["Idx", "Password", "Name", "Surname", "Email"]
    codecooler_view.print_table(titles, students)


def _save_attendance(students_attendance):
    """
    Save list of attendance of all students in csv file

    Args:
        students_attendance (list of :obj: `AssigementModels`): list with detail of attendance for all students
    """
    for i in range(len(students_attendance)):
        students_attendance[i] = [students_attendance[i].student_idx, students_attendance[i].date,
                                  students_attendance[i].state]

    DataManager.save_file("csv/attendance.csv", students_attendance)


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
