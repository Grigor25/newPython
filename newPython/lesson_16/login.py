import time
def login(email,password):

    with open('users.txt','r+') as file:
        is_keys = True
        users_list = []
        for item in file.readlines():
            if is_keys:
                is_keys = False
            else:
                users_list.append(item.split(','))
    return users_list


def dec_login(login):
    def wrap(email,password):
        start = time.time()
        users_list = login(email,password)
        end = time.time()
        print(end - start)
        for item in users_list:
            if email == item[2] and password == item[3]:
                if item[5] == 'super_admin':
                    print(users_list)
                elif item[5] == 'user':
                    print(item)
                else:
                    for user in users_list:
                        if user[5] != 'super_admin':
                            print(user)

    return wrap
log_dec = dec_login(login)
log_dec('bushjr@gmail.com','bush1234')
