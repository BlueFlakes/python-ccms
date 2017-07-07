from View.codecooler_view import CodecoolerView
from data_manager import DataManager
from Models.submit_assignment import SubmitAssignment
from time import sleep


class SubmitAssignmentController:
    """Contain logic to perform task on SubmitAssignment object"""

    @classmethod
    def start_controller(cls, position, assignments, idx):
        """
        Determines user role in Codecool. Allow user perform assign tasks.

        Args:
            position (string): user role in Codecool
            assignments (list of :obj: `SubmitAssignment`): list of assigemts
            idx (string): uniqe student id
        """

        if position == "student":
            cls.student_side(assignments, idx)
        elif position == "mentor":
            cls.mentor_side(assignments)

    @staticmethod
    def mentor_side(assignments):
        """
        Allow mentor to grade submited assigemts. Then list of assigemts is save to csv file.

        Args:
            assignments (list of :obj: `SubmitAssignment`): list of assigemts
        """
        task = CodecoolerView.get_inputs("Please provide task's name", ["Task"])
        task = task[0]

        for assgn in assignments:
            if task == assgn[2]:

                CodecoolerView.print_result("Student idx: {} | Date: {}".format(assgn[0], assgn[3]))
                CodecoolerView.print_result("Assignment name: {}".format(assgn[2]))
                CodecoolerView.print_result("Link: {}".format(assgn[1]))

                grade = CodecoolerView.get_inputs("Grade this assignment: ", [""])
                grade = grade[0]
                DataManager.extend_file("csv/grades.csv", [assgn[0], task, grade])

    @staticmethod
    def student_side(assignments, idx):
        """
        Allows student to submit assignment

        Args:
            idx (string): uniqe student id
        """

        assignments_available = DataManager.read_file("csv/assignments.csv")
        args = CodecoolerView.get_inputs("Submit your assignment", ["Link", "Assignment name"])

        for assgn in assignments_available:
            if args[1] == assgn[0]:
                assignments.append(SubmitAssignment(idx, args[0], args[1]))
                break
        else:
            CodecoolerView.print_result("Wrong assignment name!")
            sleep(1.5)
