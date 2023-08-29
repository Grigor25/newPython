#1
#list comprehension@ veradarcnum e list  isk generator@ generator tipi object


#2

#returni poxaren gratse e yield

#3

def fib(num=0):
    fib_num_list = [1,2,3]
    if num == 25:
        while len(fib_num_list) < num:
            fib_num_list.append(fib_num_list[-1] + fib_num_list[-2])
        yield fib_num_list[-1]
    for x in fib_num_list:
        fib_num_list.append(fib_num_list[-1] + fib_num_list[-2])
        yield x
x = fib(25)
print(next(x))


#4

def range_copy(*args):
    if len(args) > 2:
        raise TypeError('argument error')
    elif len(args) == 2:
        (start,end) = args
    else:
        (start,end) = (0,*args)
    range_list = []
    while start < end:
        range_list.append(start)
        start += 1
    for step in range_list:
        yield step

#5
def is_symetric(str):
    str_length = len(str)
    step = 0
    while step < str_length // 2:
        if str[step] == str[str_length - 1 - step]:
            step += 1
            continue
        else:
            return False
    return True


#6

x = ['abcba', 'abcbca', 'abcbt', '121', '123454321', '5551555']
y = {item: is_symetric(item) for item in x}


#Research

#1 __iter__method@ tuyle talis  e objectnerin next() method@ ogtagortsel


#2#answer    dict,set,tuple,string,list


#3 list,tuple,string,range

#4

#sequence data typer@ unen voroshaki hajordakanutyun isk iterablner@ voch