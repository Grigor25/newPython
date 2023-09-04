def registracion():
    email,password,first_name,last_name = [input(f'please enter your {item}') for item in ['email','password','first_name','last_name']]

    with open('auth/users.txt','r+') as file:
        dict_keys = []
        is_keys = True
        users_list = []
        for item in file.readlines():
            if is_keys:
                dict_keys = item.split(',')
                is_keys = False
            else:
                users_list.append(item.split(',')[0:1])
        print(users_list)
        for item in users_list:
            if email in item[0]:
                raise Exception(f'User {email} alraedy regisrated')
        else:
            file.writelines(f'\n{email},{password},{first_name},{last_name}')