

def riddle_with_numbers(sum, mul):
    for i in range(sum):
        for j in range(mul):
            if sum == i + j and mul == i * j:
                return [i, j]

print(riddle_with_numbers(11, 30))