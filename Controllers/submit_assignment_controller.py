from View.codecooler_view import CodecoolerView
from data_manager import DataManager

class SubmitAssignmentController:

    def start_controller(self, position):

        if position == "student":
            args = CodecoolerView.get_inputs("Submit your assignment", ["Your idx", "Link", "Comment"])
            SubmitAssignment(args[0], args[1], args[2])

            SubmitAssignment.assignments.append(SubmitAssignment(args[0], args[1], args[2]))

        elif position == "mentor":
            
