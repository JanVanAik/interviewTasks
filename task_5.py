# [1,4,5,7,8,9,2,3,10] -> "1-3, 4-5, 7-10", only ints, no repetitions

def intToString(array):
    intArray = sorted([int(i) for i in array])
    pivot = min(array)
    res = ''
    for num in intArray:
        upperBorder = pivot
        if num == pivot + 1:
            upperBorder = num
        elif num == pivot:
            pass
        else:
            res += f'{pivot}-{upperBorder},'
            pivot = num
            upperBorder = num
    return res

print(intToString([1, 4, 5, 7, 8, 9, 2, 3, 10]))




