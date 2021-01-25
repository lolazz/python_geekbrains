class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        string = ''
        for i in self.matrix:
            for j in i:
                string += f' {j}'
            string += '\n'
        return string

    def __add__(self, second):
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = self.matrix[i][j] + second.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


a = [[5, 55, 66], [3, 33, 44], [2, 22, 33]]
b = [[5, 45, 34], [-3, -33, -44], [8, 78, -33]]
m = Matrix(a)
mm = Matrix(b)

print("\nМатрица №1")
print(m.__str__(), "\n")

print("Матрица №2")
print(mm.__str__(), "\n")

print("Сумма матриц №1 и №2")
print(m + mm)