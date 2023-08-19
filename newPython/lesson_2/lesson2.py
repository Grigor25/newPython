#1
print(1 + 2.0 + 3)
#kveradarcni 6.0 qani vor tveric mek@ float e

#2 2 * 3 +4

print(2 *( 3 + 4))

#3
print(round(2.555,2))

#4
text = 'Hello World'
text = text[5:11] + ' ' + text[0:5]
print(text)

#5
#s1 = """Lorem Ipsum is  {}  dummy text of the printing and typesetting industry.
#	   Lorem Ipsum has been the industry's standard dummy text ever since the {}s,
#	   when an unknown printer took a {}  of type and scrambled it to make a type
#	   specimen book'.""".format('text',1500,'galley')

first = "text"
secont = 1500
thrid = 'galley'
# s1 = """Lorem Ipsum is  %s  dummy text of the printing and typesetting industry.
#	   Lorem Ipsum has been the industry's standard dummy text ever since the %ss,
#	   when an unknown printer took a %s  of type and scrambled it to make a type
#	   specimen book'.""" % (first,secont,thrid)

s1 = f"Lorem Ipsum is  {first}  dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the {secont}s,when an unknown printer took a {thrid}  of type and scrambled it to make a typespecimen book'."
print(s1)


#6
num = 64
print(num % 10)
print(num // 10)

#7
number = 123
print(number % 10 + round(number // 10,3) % 10 + number // 100)





#Research
#1 v= 'man'
#  print(v[len(v) - 1])

#2 strip() method@ skzbic ev verchic jnjum e parametrerov trvats arjeqn@ minch arajin chamnknum@

#3""" tuyl e talis grel m ik qnai toxi vra