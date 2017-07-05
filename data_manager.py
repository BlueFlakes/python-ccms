import csv

class DataManager:

    @staticmethod
    def read_file(file_name):
        temp = []

        with open(file_name, 'r') as csvfile:
            data_reader = csv.reader(csvfile)

            for record in data_reader:
                temp.append(record)

        return temp

    @staticmethod
    def save_file(file_name, data):

        with open(file_name, 'w') as csvfile:
            data_writer = csv.writer(csvfile)

            for record in data:
                data_writer.writerow([record])
