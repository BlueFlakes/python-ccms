from datetime import datetime


class SubmitAssignment:

    assignments = []

    def __init__(self, idx, link, name, date=None):
        self.idx = idx
        self.link = link
        self.name = name

        if type(date) == str:
            self.date = date
        else:
            date = datetime.today()
            self.date = "{}.{}.{} - {}:{}".format(date.day, date.month, date.year, date.hour, date.minute)
