class Operation:
    def __init__(self, state, date, amount, currency, description, recipient, destination=None):
        self.state = state
        self.date = date
        self.amount = amount
        self.currency = currency
        self.description = description
        self.destination = destination
        self.recipient = recipient
        