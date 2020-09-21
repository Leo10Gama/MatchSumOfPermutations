import itertools as it

def powerset(iterable):
    s = list(iterable)
    return it.chain.from_iterable(it.combinations(s, r) for r in range(len(s)+1))

ar = []
try:
    size_of_ar = int(input("Enter size of array: "))
    for i in range(0, size_of_ar):
        num = input("Enter number {}: ".format(i))
        if float(num) % 1 == 0: 
            ar.append(int(num))
        else: 
            ar.append(float(num))
    else:
        sum_to_find = float(input("Enter sum to find: "))
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
            for item in combinations:
                print(item)
except:
    print("Something went wrong, please try again")