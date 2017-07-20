from Data import tools

class Grade:
    grades_list = []
    _file_name = 'csv/grades.csv'

    def __init__(self, idx, title, grade):
        self.idx = idx
        self.title = title
        self.grade = grade

    @classmethod
    def get_grades_list(cls):
        return cls.grades_list

    @classmethod
    def add_grade(cls, idx, title, grade):
        cls.grades_list.append(Grade(idx, title, grade))

    @classmethod
    def load_grades(cls):
        cls.grades_list = tools.get_data_from_file(cls._file_name, Grade)

    @classmethod
    def get_records_from_objects(cls):
        temp = []

        for task in cls.grades_list:
            temp.append([task.idx, task.title, task.grade])

        return temp

    @classmethod
    def save_grades(cls):
        grades_data_records = cls.get_records_from_objects()
        tools.save_data_to_file(cls._file_name, grades_data_records)
