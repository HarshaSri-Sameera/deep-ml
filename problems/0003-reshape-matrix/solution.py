import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    a_shape = len(a) * len(a[0])
    new_shape_count = sum([new_shape[1] for i in range(new_shape[0])])
    if a_shape == new_shape_count:
        a = np.asarray(a)
        a = a.flatten()
        result = []
        i = 0
        while(i < len(a)):
            dum = []
            for j in range(2):
                dum.append(a[i]) 
                i += 1
            result.append(dum)
        return result
    else: 
        return []