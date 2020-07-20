from sys import argv

name, hours, salary, prize = argv
hours = int(hours)
salary = int(salary)
prize = int(prize)

print('Ваша заработная плата с учётом премии составит:', hours * salary + prize)