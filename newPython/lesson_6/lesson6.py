#1
x = {1,2,4,5,6}
y = {5,6,7,8,9}

z = x.intersection(y)
d = x.difference(y)
print(d)

#2
x = x.difference(z)
print(x)

#3
#@ndunum e'r'   read

#4

file1 = open('../file1.txt', 'w')
file1.write("file1")
file1.close()
file2 = open('../file2.txt', 'w')
file2.write("file2")
file2.close()

file1 = open('../file1.txt', 'a')
file2 = open('../file2.txt', 'a')
file2.write("newfile2")
file1.write("newfile1")
file1.close()
file2.close()


file_name = input('which file do you want to read?')#answeri depqun grel aysper 'file1.txt
file = open(file_name)
print(file.read())
file.close()



#5
users = [
				  	{
					  'first_name': 'Jorj',
					  'last_name' : 'Bush',
					  'age':55
					},

					{
					  'first_name': 'James',
					  'last_name' : 'Bond',
					  'age':100
					}
				]

file = open('../users.txt', 'w')
file.write(f'user1: first_name = Jorj, last_name = Bush, age = 55\nusers: first_name = James, last_name = Bond, age = 100')
file.close()

#Reserach

#isdisjoint() cuyc e talis ka hatum te che
#remove error kta ete elemnt@ chari seri mech isk discard@ che