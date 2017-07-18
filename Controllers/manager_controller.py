from View import codecooler_view


def start_controller():
    """
    Allow manager user perform assign tasks

    Args:
        name (string): name of user
        surname (string): surname of user
        idx (string): unique user's id
    """
    # user_welcome = "Welcome {} {}".format(name, surname)
    start_main_menu()


def start_main_menu():
    """
    Call functions that get user input and show menu
    """
    user_welcome = 'main menu'
    main_menu = ['List mentors', 'Edit mentors', 'List Students']
    user_request = None

    while user_request != "0":
        # os.system("clear")
        codecooler_view.print_menu(user_welcome, main_menu, "Exit")
        user_request = codecooler_view.get_inputs("Please choose a number", ["Number"])[0]

        handle_main_menu_requests(user_request)


def handle_main_menu_requests(user_request):
    """
    Call function that perform task from menu choosen by user: see list of students, mentors,
    edit mentors

    Args:
        user_request (string): option choosen by user
    """
    if user_request == '1':
        # get_mentors_list
        pass

    elif user_request == '2':
        # start_mentor_edit_menu
        pass

    elif user_request == '3':
        # get_students_list
        pass

    elif user_request == '0':
        # MentorController.save_mentors_data
        exit()


def start_mentor_edit_menu():
    """
    Call functions that get user input and show inner menu
    """
    mentor_edit_menu = ['Add mentor', 'Delete mentor', 'Modify mentor name',
                        'Modify mentor surname', 'Modify mentor password',
                        'Modify mentor email']
    user_request = None

    while user_request != "0":
        os.system("clear")
        codecooler_view.print_menu(user_welcome, mentor_edit_menu, "Exit")
        user_request = codecooler_view.get_inputs("Please choose a number", ["Number"])[0]

        handle_mentor_edit_requests(user_request)


def handle_mentor_edit_requests(user_request):
    """
    Call function that perform task from inner menu choosen by user: add mentor, remove mentor,
    chenge mentros details

    Args:
        user_request (string): option choosen by user
    """

    if user_request == '1':
        # MentorController.add_mentor
        pass

    elif user_request == '2':
        # MentorController.remove_mentor
        pass

    elif user_request == '3':
        # MentorController.change_mentor_name
        pass

    elif user_request == '4':
        # MentorController.change_mentor_surname
        pass

    elif user_request == '5':
        # MentorController.change_mentor_password
        pass

    elif user_request == '6':
        # MentorController.change_mentor_email
        pass


def get_mentors_list():
    # titles = ["Idx", "Password", "Name", "Surname", "Email"]
    # mentors = InstancesList.prepare_data_to_visualize(Mentor.mentor_list)
    # codecooler_view.print_table(titles, mentors)
    pass

def get_students_list():
    # titles = ["Idx", "Password", "Name", "Surname", "Email"]
    # students = InstancesList.prepare_data_to_visualize(Student.student_list)
    # CodecoolerView.print_table(titles, students)
    # get_students_grades()
    pass

def get_students_grades():
    # check_grades = CodecoolerView.get_inputs("Do you want to see grades of any student?",
    #                                          ["Yes/no"])
    # check_grades = check_grades[0].lower()
    # if check_grades == "yes":
    #     idx = CodecoolerView.get_inputs("Please provide idx of the student", ["Idx"])[0]
    #     StudentController.view_grades(idx)
    pass

def load_managers(data):
    # Manager.manager_list = InstancesList.convert_data_to_object('manager', data)
    pass

def save_managers_data():
    # data = InstancesList.prepare_data_to_visualize(Manager.manager_list)
    # DataManager.save_file('csv/managers.csv', data)
    pass



def main():
    start_controller()



if __name__ == "__main__":
    main()
