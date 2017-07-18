from Models.attendance import AttendanceModel
from View.codecooler_view import CodecoolerView
from datetime import date

from Models.student import Student
from data_manager import DataManager


def start_controller():
    """
    Contain main logic for AttendanceController.
    """
    students = Student.student_list
    students_attendance = _create_students_attendance_list()
    option = 0
    menu_options = ["Check attendnace", "View student attendance"]
    while not option == "0":

        CodecoolerView.print_menu("Student's attendance menu", menu_options, "Exit")
        options = CodecoolerView.get_inputs("Please choose a number", ["Number"])
        option = options[0]

        if option == "1":
            _check_attendance(students_attendance, students)
        elif option == "2":
            choosen_student = CodecoolerView.get_inputs("Student attendance detail", ["Student idx"])
            attendance_student_list = _get_attendnace_list(students_attendance, choosen_student[0])
            _calculate_attendnace(students_attendance, choosen_student[0])

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
        pass

    else:
        print("Student attendance {}%\n".format(attendance_procent))


def _check_attendance(students_attendance, students):
    """
    Add AttendanceModel object to proper list.

    Args:
        students_attendance (list of :obj: `AssigementModels`): list with detail of attendance for all students
        students (list of :obj: `StudentModels`):list with detail of all students
    """
    current_date = date.today()
    for student in students:
        attendance_option = None
        attendance = None
        check_attendance_person = "Check attendance for {} {}:".format(student.name, student.surname)
        while attendance_option not in ["0", "1", "2", "3"]:

            CodecoolerView.print_menu(check_attendance_person, ["Present", "Not presaent", "Late"], "Exit")
            attendance_options = CodecoolerView.get_inputs("Please choose a number", ["Number"])
            attendance_option = attendance_options[0]

            if attendance_option == "1":
                attendance = 1.0
            elif attendance_option == "2":
                attendance = 0.0
            elif attendance_option == "3":
                attendance = 0.8
            else:
                print("Wrong option")

        if attendance:
            student_attendance = AttendanceModel(student.idx, current_date, attendance)
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

    if attendance_list:
        for attendance_detail in attendance_list:
            attendnace = AttendanceModel(attendance_detail[0], attendance_detail[1], attendance_detail[2])
            students_attendance.append(attendnace)

    return students_attendance


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
