import sys
users = "Lilit", "Aren", "Janna", "Samvel", "Gohar", "Armen", "Luiza"
print('true')
if(sys.argv[1] == 'list'):
    print(list(users))
elif(sys.argv[1]  == 'tuple'):
    print(tuple(users))
elif(sys.argv[1]  == 'set'):
    print(set(users))