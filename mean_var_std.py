import numpy as np
import pprint

def main():
    myList = [*range(0,9)]
    calculate(myList)

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.") 

    # convert to np array
    arr = np.array(list)
    # reshape to 3x3
    res_arr = arr.reshape(3, 3)
    # create empty dict
    calculations = {}
    # dict with operators
    operators = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
                }
    for operator, func in operators.items():
        new_list = [[],[]]
        for i in range(3):
            new_list[0].append(func(res_arr[:, i]))  
            new_list[1].append(func(res_arr[i, :]))  
        # apply the operator to the entire array
        new_list.append(func(res_arr))
        # store the result in the calculations dictionary
        calculations[operator] = new_list
    print(calculations)

    return calculations
if __name__ == "__main__":
    main()

# {
#   'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
#   'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
#   'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
#   'max': [[6, 7, 8], [2, 5, 8], 8],
#   'min': [[0, 1, 2], [0, 3, 6], 0],
#   'sum': [[9, 12, 15], [3, 12, 21], 36]
# }