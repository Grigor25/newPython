import re
names = 'S.Paloyan Vardan Vardanyan Miqayel_Abrahamyan H.Stepanyan P.Petrosyan_5 J.Blade'


name_reg = r'[A-Z][.][A-Z][a-z]*'
correct_names = re.findall(name_reg,names)
print(correct_names)


#2

text = '''There are many variations of passages of Lorem Ipsum available, but the $6700 majority have suffered alteration in some form,
			by injected humour, or randomised words which don't look even slightly  believable. If you are going to use a passage $3,200
			of Lorem Ipsum, 8,200 you need to be sure there isn't anything embarrassing hidden in the middle of text. All $5,200 the Lorem Ipsum
			generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator  $3,200.00 on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of $5200  model sentence structures, to generate Lorem Ipsum which looks reasonable.
			The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.'''

reg_exx = r'[$][0-9][,][0-9]*'
match = re.findall(reg_exx,text)
print(match)


match_sum = [int(item.strip("$,").replace(',','')) for item in match]
print(sum(match_sum))


#3

links = 'https://www.youtube.com http://translate.google.ru www.github.com https://www.w3schools.com https://www.python.org'

links_reg = r'[a-z]{5}'
links_reg2 = r'[a-z]{5}[:][/]{2}[a-z]{3}[.][a-z]*[.][a-z]{3}'

correct_links = re.findall(links_reg2,links)
print(correct_links)

#4

email = input('please insert your email')

email_reg = r'[a-z]{5}[@][a-z]{2,4}[.]ru'

if  re.match(email_reg,email):
    print('Valid email')
else:
    print("Invalid email")


#Reasearch

#re.coplier@ maket e stextsum reg expresioni  i hamar vor kodi mech amen angam chkanchenq