class Date:
    def __init__(self, str_data):
        self.extract(str_data)
        self.validate(self.day, self.month, self.year)

    @classmethod
    def extract(cls, str):
        cls.day, cls.month, cls.year = map(int,str.split('-'))

    @staticmethod
    def validate(day, month, year):
        if month > 12:
            raise ValueError("oh no!")


date = Date('1-1-12')

print(date.day)
print(date.month)
print(date.year)

date = Date('1-13-12')