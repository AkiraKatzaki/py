
def two_to_the_degree(x):
    count = 0
    while 2 ** count <= x:
        print(2 ** count)
        count += 1

print(two_to_the_degree(56))