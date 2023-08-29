def registracion():
    email,password,first_name,last_name = [input(f'please enter your {item}') for item in ['email','password','first_name','last_name']]

    with open('auth/users.txt','r+') as file:
        dict_keys = []
        check = True
        users_list = []
        for item in file.readlines():
            if check:
                dict_keys = item.split(',')
                check = False
            else:
                users_list.append(item.split(',')[0:1])
            print(dict_keys,users_list)
            print(email in users_list)
        if email in users_list:
            raise Exception(f'User {email} alraedy regisrated')
        else:
            file.writelines(f'\n{email},{password},{first_name},{last_name}')