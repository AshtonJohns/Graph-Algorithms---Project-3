import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np



list_test = ["A","B"]
list_test_1 = ["B","A"]
list_test_1.sort()
list_without_brackets = ','.join(list_test)

print(list_without_brackets)
print(len(list_test))
building_list = []
if len(list_without_brackets) == 3:
    print("True")
    print(list_without_brackets)
    test = "("+list_without_brackets+")"
    building_list.append([list_without_brackets])
    print(building_list)

test = "("+list_without_brackets+")"

# if len(list_test) % 2 == 0:
#     list_without_brackets = ','.join(list_test)
#     test = "("+list_without_brackets+")"
