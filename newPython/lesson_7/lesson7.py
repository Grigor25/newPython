#1 answer ktpi users exist   vorovhetev users list@ datark chi mech@ 0 indexum ka list


#2
pythonists = ["Bush", "Jarvis", "Oxxi", "Buffon", "Vardan"]

if 'Grigor' in pythonists:
    print('Grigor' in pythonists)
else:
    pythonists.append("Grigor")
    print(pythonists)

    if 5 < len(pythonists) < 7:
        print(len(pythonists))
    elif len(pythonists) < 5:
        print("append new user")
        pythonists.append('Artak')
    elif len(pythonists) > 7:
        print('user removed')
        pythonists.pop()


#3
x = 0
while x <= 21:
    if x % 2 == 0:
        print(x)
        x = x + 1
    else:
        x = x + 1

#4
x = 20

while x >= 0:
    if x == 17:
        x = x - 1
        continue
    else:
        print(x,x**2)
        x = x - 1

#5
x = 1
y = 0

while x < 50 and y < 10:
    if x % 3 == 0:
        print(x)
        y = y + 1
        x = x + 1
    else:
        x = x + 1


#Reserach
# esl@ whini het normal ashxatuma
while True:
    print('Yes')
    break
else:
    print('No')
# breaki depqum chi mtnum
while True:
    print('Yes')
    continue
else:
    print('No')
# continui depqum chi mtnum anverj loopa mtnum
while False:
    print('Yes')
    continue
else:
    print('No')

