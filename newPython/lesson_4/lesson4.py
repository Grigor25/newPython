#1
#copyn copi e anum miayn arachin level@ is deepCopyn inchqan leveli vor ka


#2
x = [1,2,5, [8,9,10]]
y = x.copy()
y[3] = 5
print(x,y)
#3 tuple - ('Erk','Ereq','Choreq','Hing','Urb',['Shb'])
# tuple[5].append('kiraki')

#vorovhetev tuppli arjeq chenq poxum inq@ nuyn listna mnum uxaki ira arjeqnenq poxum


#4
name,last_name,patronymic = ('My name','My last name','My father name')


#5
# karanq tuple sarqenq list() popoxenq mejy inch vor ban heto sarqenq tuple()
users_tuple = ("Lilit", "Aren", "Janna", "Samvel (Sam)", "Gohar", "Armen", "Luiza")
users_list = list(users_tuple)
users_list[0] = 'Varduhi'
users_tuple = tuple(users_list)
print(users_tuple)

#6
users_list = [
			"Lilit", "Aren", "Janna", "Samvel (Sam)", "Gohar", "Armen", "Luiza",
			[[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21]]
		]
new_users = zip(users_list[0:7],users_list[7][0],users_list[7][1],users_list[7][2])
print(new_users)


#Research
# zip() functian veradarcnum e zip typi object,parametr @ndunum e iterablener,stextsum e hertakanutyamb taplner @st trvats iterablneri indexi erkarutyun@ darnum e amenakarch iterabli erkarutyun@

