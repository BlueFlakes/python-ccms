import csv


class DataManager:
    """This class represents utilites to load data from csv file and save them to it ."""

    @staticmethod
    def read_file(file_name):
        """
        Reads given file and returns list of lists, where every list is a line of csv file.

        Args:
            file_name (string): name of csv file

        Returns:
            temp (list of lists): data read from csv file to further use
        """
        temp = []

        try:
            with open(file_name, 'r') as csvfile:
                data_reader = csv.reader(csvfile)

                for row in data_reader:
                    temp.append(row)

        except FileNotFoundError:
            open(file_name, 'w').close()

        finally:
            return temp

    @staticmethod
    def save_file(file_name, data):
        """
        Save data to csv file.

        Args:
            file_name (string): name of csv file
            data (list of strings): data that will be save in csv file
        """

        with open(file_name, 'w') as csvfile:
            data_writer = csv.writer(csvfile)

            for i in range(len(data)):
                data_writer.writerow(data[i])

    @staticmethod
    def extend_file(file_name, data):
        """
        Extend csv file wit new data.

        Args:
            file_name (string): name of csv file
            data (list of strings): data that will be save in csv file
        """

        with open(file_name, 'a') as csvfile:
            data_writer = csv.writer(csvfile)

            data_writer.writerow(data)

    @staticmethod
    def get_person_details(idx, file_name):
        """
        Returns list of lists, where every nested list is one line in csv file.
        Lines which are in list are determined on given idx.

        Args:
            idx (string): uniqe person id
            file_name (string): name of csv file

        Returns:
            temp (list of lists): data read from csv file to further use
        """

        temp = []
        people_info = DataManager.read_file(file_name)

        for info in people_info:
            if idx in info[0]:
                temp.append(info)

        return temp


def load_data_setup(Manager, Student, Mentor, OfficeManager):
    Manager.load_managers(DataManager.read_file("csv/managers.csv"))
    Mentor.load_mentors(DataManager.read_file("csv/mentors.csv"))
    Student.load_students(DataManager.read_file("csv/students.csv"))
    OfficeManager.load_office_managers(DataManager.read_file("csv/officemanagers.csv"))
