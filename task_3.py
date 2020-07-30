class Cell:
    def __init__(self, cell_count):
        self.cell_count = cell_count

    def __add__(self, other):
        return self.cell_count + other.cell_count

    def __mul__(self, other):
        return self.cell_count * other.cell_count

    def __sub__(self, other):
        sub = self.cell_count - other.cell_count
        if sub > 0:
            return sub
        else:
            return 'Разность должна быть положительным числом'

    def __truediv__(self, other):
        return round(self.cell_count / other.cell_count)

    def make_order(self, row):
        cells = []
        for _ in range(self.cell_count):
            cells.append('*')
        while len(cells) >= row:
            print(f"{''.join(cells[:row])}")
            del cells[:row]
        else:
            print(''.join(cells))


cell_1 = Cell(12)
cell_2 = Cell(15)
print(cell_1 + cell_2)
print(cell_1 * cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print('\ncell 1:')
cell_1.make_order(5)
print('\ncell 2:')
cell_2.make_order(4)
