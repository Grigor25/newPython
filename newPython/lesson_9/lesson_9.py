#1

def person(name, last_name, age):
    print(f'hello my name is {name}, my last name is {last_name}, I am {age} years old')

person('Grigor','Manukyan',28)

#2

def change_char(text, old_character, new_chararcter):
    new_text = ''
    for char in text:
        if char == old_character:
            new_text += new_chararcter
        else:
            new_text += char
    return  new_text

name = change_char('Manukyan','a','k')
print(name)

#3

def new_file(file_name:'text.txt', list_of_texts):
    file = open(file_name,'w')
    file.write(list_of_texts)
    file.close()

new_file('users.txt',"Manukyan,Grigor")

#4

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            return False
    else:
        return True

#Research

#anwser  """  """   erek skobkeqi mech mi qani tox karelia grel   help(func) mijocov
