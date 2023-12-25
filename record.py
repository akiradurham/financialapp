import datetime as dt


class Records:

    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
        self.dt = dt.datetime.now()

    def __repr__(self):
        return f"{self.name} is a {self.category}: ${self.price}\n"
