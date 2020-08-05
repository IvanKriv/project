class ComplexNum:
    def __init__(self, num):
        self.num = num
        self.num = self.num.split(' ')
        del self.num[1]
        if self.num != 'i':
            self.num[1] = self.num[1][:1]
        if self.num[1] == 'i':
            self.num[1] = 1

    def __add__(self, other):
        return f'Result "+": {int(self.num[0]) + int(other.num[0])} + {int(self.num[1]) + int(other.num[1])}i'

    def __mul__(self, other):
        return f'Result "*": {int(self.num[0]) * int(other.num[0]) - int(self.num[1]) * int(other.num[1])} + ' \
               f'{int(self.num[0]) * int(other.num[1]) + int(self.num[1]) * int(other.num[0])}i'


num_1 = ComplexNum('5 + 3i')
num_2 = ComplexNum('4 + 2i')
print(num_1 + num_2)
print(num_1 * num_2)
