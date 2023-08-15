#1
users_list = ['Vardan', 'Vazgen', 'Jarviz']
print(users_list)
users_list[0] = 'Grigor'

#2
x = [1,2,3,4,5,6]
z = [7,8,9,10,11]
print(len(x) + len(z))


#3

# len() -> cuyc e erkarutyun@
# list() -> stextsum e nor@
# copy() -> copi e anum hajordakanutyun@
# sorted() -> sortavorum e hajordakanutyun
# remove() ->jnjum e hajordakanutyuniic trvats element@
# append() -> add e anum element
# reverse() -> shrjum e hajordakanutyun@



#4
count = input('how many words do you want to type?')
word = input('write a word')
print(word*int(count))

#5
users_list = ["Vazgen", "Chris Tacker", "Nikola Tesla"]
new_users_list = users_list.copy()
new_users_list.append(input('add new user'))
print(users_list,new_users_list)

#6
users_list = ["Vazgen", "Chris Tacker", "Nikola Tesla"]
remove_user = input(
    """Your users ["Vazgen", "Chris Tacker", "Nikola Tesla"]'
    'who do you want to remove ?""")
users_list.remove(remove_user)

print(f"""User {remove_user.upper()} is removed'
       'Your users {users_list}""")


#7
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(numbers_list[1::2]))

#Research
#1 list.index()
#remove-ov karex enq jnjel mek element isk delov nayev amboxch list@,remov@ vorpes parametr @ndunum e element@ isk del@ index@