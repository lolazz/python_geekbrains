class Worker:
    def __init__(self, name, surname, position, income, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income
        self.__wage_bonus = {"wage": wage, "bonus": bonus}

    def get_wage(self):
        return self.__wage_bonus["wage"]

    def get_bonus(self):
        return self.__wage_bonus["bonus"]


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.income + self.get_wage() + self.get_bonus()


pos = Position("Ivan", "the Great", "lol", 100, 50, 200)
print(pos.get_full_name())
print(pos.get_total_income())
