class Employee:

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def __str__(self):
        return f"{self.name}, ${self.pay:.2f}"

    def __gt__(self, other):
        return self.pay > other.pay

    def __lt__(self, other):
        return self.pay < other.pay
