import itertools
def choose_best_sum(t,k,ls):
    combos=list(itertools.combinations(ls,k))
    sums=[sum(i) for i in combos]
    sums2=[i for i in sums if i<=t]#only the sums we care about
    if sums2==[]:
        largest=None
    else:
        largest=max([i for i in sums if i<=t])
    return largest

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print choose_best_sum(430,8,xs)