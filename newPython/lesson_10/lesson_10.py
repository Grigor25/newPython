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
    defoul_list = [1,2,3]
    if num in defoul_list:
        return num
    else:
        while len(defoul_list) < num:
            defoul_list.append(defoul_list[-1] + defoul_list[-2])
    return defoul_list[-1]
print(fib(14))


#Research
#	1.	Python Function Annotations

# avelacnum e functioayi argumentneri masin informacia



#	2.
#answer args u kwarg@ tuyl en talis grel ansman qanaki argumentneric functiayi hamar
#*args grvum e sovorakan argumentneric ev default argumentneric heto ev veradarcum e avel argumentr@ tupli tesqov
#**kwargs@ grvum e verchum ev veradarcnum dictionalri drvats argumetnerov