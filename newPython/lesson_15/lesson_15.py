from functools import reduce


#1
simetric_wors = ['abcba', 'abcbca', 'abcbt', '121', '123454321', '5551555']


def is_symetric_func(str):
    str_length = len(str)
    step = 0
    while step < str_length // 2:
        if str[step] == str[str_length - 1 - step]:
            step += 1
            continue
        else:
            return False
    return True



si_simetric = list(filter(is_symetric_func,simetric_wors))

print(si_simetric)


#2

li = [1,2,3,4,5,6,7]

def custom_map(func,iter):
    result = list()
    for item in iter:
        res = func(item)
        result.append(res)
    if type(iter) == list:
        return  zip(result)
    elif type(iter) == tuple:
        return zip(result)
    elif type(iter) == set:
        return zip(result)


print(list(custom_map(lambda x: x +10,li)))

#3


numbs = [1, 2, 5, 70, 4, 8, 50, 44]

max_num = numbs[0]
for item in numbs:
    if max_num < item:
        max_num = item


max_num2 = reduce(lambda x,y: y if  (x < y) else x,numbs,0)
