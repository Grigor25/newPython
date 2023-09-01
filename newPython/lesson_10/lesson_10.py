#1

my_name = 'name'
def f1():
    global my_name
    my_name = 'Grigor'

f1()
print(my_name)

#2

users = ["Lilit", "Aren", "Janna", "Samvel", "Gohar", "Armen", "Luiza", "Janna", "Armen", "Lilit"]
long_word = 'dzaynaskavarakavacharanoc' # google եմ արել :)
last_names = ("Watson", "Richards", "Richardson", "Saunders", "Watson", "Young", "Saunders")

def dub_items(seq):
    if type(seq) == int:
        return 'please send sequence object'
    result_check = []
    result = set()
    for item in seq:
        if item in result_check:
            result.add(item)
        else:
            result_check.append(item)
    return list(result)

print(dub_items(long_word))

#3

def sum_num(num):
    number = num
    sum = 0
    while number:
        sum += (number % 10)
        number = number // 10
    return sum

print(sum_num(65))


#4

def is_prime(n):
    if n < 2:
        return False
    li = []
    for j in range(2,n):
        for i in range(2, int(j ** 0.5 + 1)):
            if j % i == 0:
                break
        else:
            li.append(j)
    return li
print(is_prime(100))


#5

def fib(num):
    default_list = [1,2,3]
    if num in default_list:
        return num
    else:
        while len(default_list) < num:
            default_list.append(default_list[-1] + default_list[-2])
    return default_list[-1]
print(fib(14))

def fib_2(n):
    x = 1
    y = 2
    fib_number = 2
    while fib_number != n:
        if n < 2:
            return n
        else:
            print(fib_number)
            x,y = y,x + y
            print(x,y)
            fib_number += 1
    return y

print(fib_2(1),'fib2')




#Research
#	1.	Python Function Annotations

# avelacnum e functioayi argumentneri masin informacia



#	2.
#answer args u kwarg@ tuyl en talis grel ansman qanaki argumentneric functiayi hamar
#*args grvum e sovorakan argumentneric ev default argumentneric heto ev veradarcum e avel argumentr@ tupli tesqov
#**kwargs@ grvum e verchum ev veradarcnum dictionalri drvats argumetnerov