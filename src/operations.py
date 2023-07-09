import datetime


class Operation:
    def __init__(self, state, date, amount, currency, description, recipient, destination=None):
        self.state = state
        self.date = date
        self.amount = amount
        self.currency = currency
        self.description = description
        self.destination = destination
        self.recipient = recipient


    def change_date(self):
        self.date = datetime.datetime.strptime(self.date, "%Y-%m-%dT%H:%M:%S.%f")
        return self.date

