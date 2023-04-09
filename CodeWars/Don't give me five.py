def dont_give_me_five(start, end):
    arr = []
    for i in range (start, end + 1):
        if '5' not in str(i):
            arr.append(i)
    return len(arr)

print(dont_give_me_five(4,11))
