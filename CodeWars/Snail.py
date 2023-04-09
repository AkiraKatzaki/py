def snail(matrix):
    arr = []
    while len(matrix) > 0:
        # go right
        arr += matrix[0]
        del matrix[0]
        if len(matrix) > 0:
            # go down
            for i in matrix:
                arr += [i[-1]]
                del i[-1]
            # go left
            if matrix[-1]:
                arr += matrix[-1][::-1]
                del matrix[-1]
            # go top
            for i in reversed(matrix):
                arr += [i[0]]
                del i[0]
    return arr

data = [[1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]]
print(snail(data))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

data2 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
print(snail(data2))  # [1, 2, 3, 6, 9, 8, 7, 4, 5]
