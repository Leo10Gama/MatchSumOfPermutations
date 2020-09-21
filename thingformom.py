import itertools as it

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return it.chain.from_iterable(it.combinations(s, r) for r in range(len(s)+1))

ar = []
size_of_ar = int(input("Enter size of array: "))
for i in range(0, size_of_ar):
    ar.append(int(input("Enter number {}: ".format(i))))
else:
    sum_to_find = int(input("Enter sum to find: "))
    combinations = []
    my_powerset = powerset(ar)
    for group in my_powerset:
        my_sum = 0
        for num in group:
            my_sum += num
        else:
            if my_sum == sum_to_find:
                combinations.append(group)
    else:
        print(combinations)