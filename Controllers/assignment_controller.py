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

        assgn = CodecoolerView.get_inputs("Add assignment", ["Title", "Description"])
        Assignment.assignments.append(Assignment(assgn[0], assgn[1]))

        cls.save_assignment(assgn)

    @staticmethod
    def save_assignment(assgn):
        """
        Save list of assignments in csv file

        Args:
            assgn (list of :obj: `Assignment`): list with all assigmnts

        """
        DataManager.extend_file("csv/assignments.csv", assgn)
