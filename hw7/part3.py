class Cell:
    def __init__(self, quantity):
        self.quantity = quantity  # количество клеток quantity cell

    def __add__(self, other):
        return self.quantity + other

    def __sub__(self, other):
        if self.quantity > other:
            return self.quantity - other
        else:
            raise ValueError('We cant remove more cells than there is')

    def __mul__(self, other):
        return self.quantity * other

    def __truediv__(self, other):
        return round(self.quantity / other)

    def make_order(self, cells_in_row):
        num_of_rows = self.quantity // cells_in_row
        last_row_cells = self.quantity % cells_in_row
        return ("*" * cells_in_row + "\n") * num_of_rows + "*" * last_row_cells


cell1 = Cell(10)

print(cell1.make_order(3))
print("\n")
print(cell1.make_order(5))
print("\n")
print(cell1.make_order(10))
print("\n")
print(cell1.make_order(1))
print("\n")

