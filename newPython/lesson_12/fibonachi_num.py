
def fib(n):
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
