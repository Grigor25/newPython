from auth import login
from auth import registracion
chosse = input('login or registracion')

if chosse == 'login':
    login()
elif chosse == 'registracion':
    registracion()