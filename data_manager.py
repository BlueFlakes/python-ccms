import csv

class DataManager:

    @staticmethod
    def read_file(file_name):
        """Reads given file and returns list of lists, where every list is a line of csv file.

           Args:
                file_name: string
           Returns:
                temp: list of lists
        """

        temp = []

        with open(file_name, 'r') as csvfile:
            data_reader = csvfile.readlines()
            for row in data_reader:
                row =   row.replace('\n', '')
                temp.append(row.split(","))

        return temp

    @staticmethod
    def save_file(file_name, data):

        with open(file_name, 'w') as csvfile:
            data_writer = csv.writer(csvfile)

            for i in range(len(data)):
                data_writer.writerow(data[i])

    @staticmethod
    def extend_file(file_name, data):

        with open(file_name, 'a') as csvfile:
            data_writer = csv.writer(csvfile)

            data_writer.writerow(data)

    @staticmethod
    def get_person_details(idx, file_name):
        """Returns list of lists, where every nested list is one line in csv file.
           Lines which are in list are determined on given idx.

           Args:
                idx: string
                file_name: string
           Returns:
           temp: list of lists
        """
        temp = []
        people_info = DataManager.read_file(file_name)

        for info in people_info:
            if idx in info[0]:
                temp.append(info)

        return temp
