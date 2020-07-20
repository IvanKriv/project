from functools import reduce
my_list = [el for el in range(100, 1000) if el % 2 == 0]
def mult(prev_el, el):
    return prev_el * el
print(reduce(mult, my_list))
