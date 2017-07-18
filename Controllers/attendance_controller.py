from Models.attendance import AttendanceModel
from Models.student import Student
from View import codecooler_view
from data_manager import DataManager
from datetime import date
import os


def start_controller():
    """
    Contain main logic for AttendanceController.
    """
    students = Student.student_list
    students_attendance = create_students_attendance_list()
    option = 0
    while not option == "0":
        # os.system("clear")

        codecooler_view.print_menu("", ["Check attendnace", "View student attendance"], "Exit")
        options = codecooler_view.get_inputs("Please choose a number", ["Number"])
        option = options[0]

        if option == "1":
            check_attendance(students_attendance, students)
        elif option == "2":
            choosen_student = codecooler_view.get_inputs("Student attendance detail", ["Student idx"])
            attendance_student_list = get_attendnace_list(students_attendance, choosen_student[0])

            calculate_attendnace(students_attendance, choosen_student[0])

    save_attendance(students_attendance)


def calculate_attendnace(students_attendance, given_student_idx):
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
        print("Student attendance {}%".format(attendance_procent))


def check_attendance(students_attendance, students):
    """
    Add AttendanceModel object to proper list.

    Args:
        students_attendance (list of :obj: `AssigementModels`): list with detail of attendance for all students
        students (list of :obj: `StudentModels`):list with detail of all students
    """
    current_date = date.today()
    for student in students:
        question = "Check attendance for {} {}".format(student.name, student.surname)
        student_detail = None

        while student_detail not in ['0', '1']:
            student_detail = codecooler_view.get_inputs(question, ["Attendance state (1 or 0)"])[0]

            if student_detail not in ['0', '1']:
                print('Wrong value!')

        attendance = AttendanceModel(student.idx, current_date, float(student_detail))
        students_attendance.append(attendance)


def get_attendnace_list(students_attendance, student_idx):
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


def create_students_attendance_list():
    """
    Convert data from csv file to AttendanceModel object and add it to list
    """
    students_attendance = []
    attendance_list = DataManager.read_file("csv/attendance.csv")
    print(attendance_list)
    if attendance_list:
        for attendance_detail in attendance_list:
            attendnace = AttendanceModel(attendance_detail[0], attendance_detail[1], attendance_detail[2])
            students_attendance.append(attendnace)

    return students_attendance


def save_attendance(students_attendance):
    """
    Save list of attendance of all students in csv file

    Args:
        students_attendance (list of :obj: `AssigementModels`): list with detail of attendance for all students
    """
    for i in range(len(students_attendance)):
        students_attendance[i] = [students_attendance[i].student_idx, students_attendance[i].date,
                                  students_attendance[i].state]

    DataManager.save_file("csv/attendance.csv", students_attendance)
