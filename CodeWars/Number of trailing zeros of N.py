def zeros(n):
    numberOfZeros = 0
    i = 1
    while (n > 0) and (n/(5**i) >= 1):
        numberOfZeros += int(n/(5**i))
        i += 1
    return numberOfZeros

print(zeros(6))
print(zeros(12))
