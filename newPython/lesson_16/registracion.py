
def registracion(first_name,last_name,email,password,age,country,countrys):
    if len(first_name) < 4 or len(first_name) > 30:
        raise Exception(f'{first_name} length error')
    elif len(last_name) < 4 or len(last_name) > 30:
        raise Exception(f'{last_name} length error')
    elif email[-10:] != '@gmail.com':
        raise Exception('email error')
    elif len(password) <= 8:
        raise Exception('password eeror')
    elif type(age) != int or age > 112 or age < 0:
        raise Exception('age error')
    elif len(country) < 3 or len(country) > 25 or country not in countrys:
        raise Exception('country error')







def registacionj_dec(registracion,countrys):
    def wrap(*args):
        registracion(*args,countrys)
    return wrap

reg_dec = registacionj_dec(registracion,['Armenia'])
reg_dec('Smbat','Paloyan','smbatpaloyan@gmail.com','smbat1234',23,'Armenia')

