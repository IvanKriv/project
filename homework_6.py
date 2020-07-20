from sys import argv
from itertools import cycle, count
#a)
# name, start_num, stop_num = argv
# for i in count(int(start_num)):
#     if i <= int(stop_num):
#         print(i)
#     else:
#         break


#b)
name = argv
j = 1
for i in cycle([1, 2, 3, 4, 5, 6]):
    if j <= 12:
        print(i)
        j += 1
    else:
        break




