class Matrix:
    def __init__(self, matrx):
        self.matrx = matrx

    def __str__(self):
        for i in self.matrx:
            for k in i:
                k = str(k)
                print("{:4s}".format(k), end="\t")
            print('\n')
        return '\n'

    def __add__(self, other):
        new_matrix = []
        m = []
        for i in range(len(self.matrx)):
            for k in range(len(self.matrx[i])):
                m.append(other.matrx[i][k] + self.matrx[i][k])
            new_matrix.append(m.copy())
            m.clear()
        return new_matrix



mt_1 = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
mt_2 = Matrix([[3, 3, 2], [4, 1, -6], [1, 6, -3], [13, 2, -1]])
print('Первая матрица:')
print(mt_1)
print('Вторая матрица:\n')
print(mt_2)
mt_3 = mt_1 + mt_2
print('Результат сложения матриц:\n')
print(Matrix(mt_3))
