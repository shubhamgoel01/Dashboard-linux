import pprint

cc = [('Streams', '10.30.48.178', 'Running'), ('Streams', '10.30.48.183', 'Running'), ('Streams', '10.30.48.185', 'Running'), ('Admin5', '10.30.48.153', 'Running'), ('Admin5', '10.30.48.154', 'Running'), ('Admin5', '10.30.48.192', 'Not Running')]

# Using above first method to create a
# 2D array
# for i in cc:
# rows, cols = (2, 3)
# arr = [[0 for i in range(cols)] for j in range(rows)]
# print(arr)

import numpy as np
#a = np.array([(1,2,3),(1,2,3)])
b = 2
a = np.reshape(cc,(b,3,3))
print(a)


# def ThreeD(a, b, c):
#     for i in cc:
#         lst = [[ [ i for col in range(a)] for col in range(b)] for row in range(c)]
#     return lst
	
# # Driver Code
# col1 = 3
# col2 = 3
# row = 2
# # used the pretty printed function
# pprint.pprint(ThreeD(col1, col2, row))



