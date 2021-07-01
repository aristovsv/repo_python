class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print (self.name, self.surname, self.position)

    def get_total_income(self):
        return sum(self._income.values())


a = Position("Kurt", "Cobain", "Rock Star", 600000, 1500000000)
print(a.get_full_name())
print(a.get_total_income())