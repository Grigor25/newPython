#1
user = {
				'name':'Jarviz',
				'age' : '100',
				'professions':['robot', 'dancer'],
				'test_result':[14,5,8,99,12,2,3,5,4]
			}
print(user['professions'][0])
user['professions'][1] = 'not dancer'
user['test_result'].sort(reverse=True)

#2
fruits = {
				"banana": 4,
				"apple": 2,
				"orange": 1.5,
				"pear": 3
			}

sum(list(fruits.values()))

fruits['watermelon'] = 5


#3
users = [
			{'first_name':'', 'last_name':'', 'age':'', 'phone':{'brend':'', 'number':'', 'is_5g':''}}, # user 1
			{'first_name':'', 'last_name':'', 'age':'', 'phone':{'brend':'', 'number':'', 'is_5g':''}}  # user 2
		]


users[0] = dict(zip(users[0],['Hayk','Baghdasaryan',28,dict(zip(users[0]['phone'],['Samsung',"+37494404442",False]))]))
users[1] = dict(zip(users[0],['Hamlet','Hovakimyan',28,dict(zip(users[0]['phone'],['Iphone',"+37498452236",True]))]))

users[0]['car'] = {'model': 'ford','type': 'mustang','max_speed': '280 km/h'}
users[1]['car'] = {'model': 'mercedes','type': 'e320','max_speed': '220 km/h'}

print(users[0]['phone']['is_5g'],users[1]['phone']['is_5g'])

x = users[0]['age'] > 18 and users[0]['phone']['is_5g'] == True or 'bill' not in users[0]['first_name'] and 'gates' not in users[0]['last_name']
print('chipavorvats e',x)


#4

name = 'Grigor'
new_list = list(name)
new_list_copy = new_list.copy()
new_list.reverse()
result = dict(zip(new_list_copy,new_list))

print(result)

#Research

 #1 set default funkcian veradarcnum e vorpes arachin parametr trvats arjin key-i arjeq@,erkord paramer @ndunum e default arjeq ev veradarcnum ayn key chunenalu depqum
#2 functian veradarcnum e dictionari vori keyern en arachin parametr trvats arjeq@ karog elinel nayem iterable isk erkrod arjeqov stanum ayd keyeri valuner@.arjeqner@ chlinelu depqum arjeq@ darnum e None
# 3. Փորձեք կիրառել մեր անցած ֆունկցիաները dict-ի համար և գրեք արդյունքներիը
# len(dict)
# zip(dict)
# type({})