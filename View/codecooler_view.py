import getpass
from Controllers.table import Table

class CodecoolerView:

    @staticmethod
    def get_inputs(title, questions_list):
        """Get imput form user

        Args:
            title (str): menu title
            questions_list (list): list of questions

        Return:
            temp (list): list with user inputs

        """
        temp = []
        print('\033[92m' + title + ':' + '\033[0m')

        for question in questions_list:
            if question == "Password":
                temp.append(getpass.getpass())
            else:
                user_input = input(question + ': ')
                temp.append(user_input)

        else:
            print()

        return temp

    @staticmethod
    def print_menu(title, available_options, exit_message):
        """Show menu to user

        Args:
            title (str): menu title
            available_options (list): possible ways to operate in app
            exit_message (str): exit message

        Return:
            None

        """
        print(title+':')

        for i, option in enumerate(available_options):
            print("{}{}) {}".format('\t', str(i+1), option))

        else:
            print('{}{}) {}'.format('\t', '0', exit_message), end=2 * '\n')

    @staticmethod
    def print_result(result):
        """Show results of action

        Args:
            result (str): print message with result to user

        Return:
            None

        """
        print(result)

    @staticmethod
    def print_table(titles, data):
        print(Table.table_creator(titles, data))
        option = CodecoolerView.get_inputs("Enter anything to exit", [""])
