def login():
    email,password = [input(f'please write your {item}') for item in  ['email','password']]
    with open('auth/users.txt','r+') as file:
        users_list = []
        for item in file.readlines():
                users_list.append(item.split(','))
        for item in users_list:
            if email == item[0] and password == item[1]:
                print(f'Hello {item[2]} {item[3]}')
                break
        else:
            raise Exception('User not found')
