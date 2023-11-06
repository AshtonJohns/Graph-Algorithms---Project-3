import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np



list_test = ["A","B"]
list_test_1 = ["B","A"]
list_test_1.sort()
list_without_brackets = ','.join(list_test)
dfs = []
dfs.append(list_test)
dfs.append(list_test_1)

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

message = "Test my list concatenate: " + str(list_test)

print(message)
size = len(dfs)

# dfs.insert(size-1,[dfs.index()])
# print(dfs)

test_2d_list = [["A","B"],["B","A"]]

dfs.clear()

dfs.extend(["a","b"])
dfs.extend(["c","d"])
dfs.extend(["e","f"])
dfs.extend(["g","h"])
dfs.extend(["i","j"])

dfs.insert(dfs.index(dfs[-2]),dfs[-3])
dfs.insert(dfs.index(dfs[-2]),dfs[-2])

print(dfs)
#last_index_to_size = dfs.index(dfs[-1])
size = len(dfs)


print(size)

dfs_to_2d = np.array(dfs).reshape(size//2,2)

print(dfs_to_2d.flatten())
