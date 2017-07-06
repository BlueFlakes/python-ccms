from datetime import datetime


class SubmitAssignment:

    assignments = []

    def __init__(self, idx, link, comment, date=datetime.time()):
        self.idx = idx
        self.date = date
        self.link = link
        self.comment
