from View.codecooler_view import CodecoolerView
from Models.assignment import Assignment
from data_manager import DataManager


class AssignmentController:
    """Contain methods to work on Assignment object"""

    @classmethod
    def start_controller(cls):
        """
        Contain main logic for AssignmentController.
        Ask user about assigemnt details and add it to assigments list
        """
        is_empty_input = True

        while is_empty_input:
            assgn_details = CodecoolerView.get_inputs("Add assignment", ["Title", "Description"])
            is_empty_input = AssignmentController.is_empty_input(assgn_details)


        Assignment.assignments.append(Assignment(assgn_details[0], assgn_details[1]))

        cls.save_assignment(assgn_details)

    @staticmethod
    def save_assignment(assgn):
        """
        Save list of assignments in csv file

        Args:
            assgn (list of :obj: `Assignment`): list with all assigmnts

        """
        DataManager.extend_file("csv/assignments.csv", assgn)

    @classmethod
    def is_empty_input(cls, assgn_details):

        for answer in assgn_details:
            if len(answer) < 1:
                CodecoolerView.print_result("You can't make assignment without title or description!")
                return True

        return False
