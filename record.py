class Records:

    def __init__(self, name, category, price, date):
        self.name = name
        self.category = category
        self.price = price
        self.date = date

    def __repr__(self):
        return f'{self.name} is a {self.category}: ${self.price} on {self.date}\n'
