class DivisionByZeroMy(Exception):
    text = "Can't divide by zero"

    def __str__(self):
        return self.text


class Number(float):
    def __truediv__(self, other):
        if other == 0:
            raise DivisionByZeroMy

        return Number(float(self) / float(other))


while True:
    try:
        number, divider = map(Number, input("Enter numbers ").split())
        print(number / divider)
    except DivisionByZeroMy as e:
        print(e)
    except ValueError as e:
        print(e)
        break
