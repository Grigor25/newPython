#1
last_names = ['Adams','Allen','Brooks','Davidson','Sargsyan','Jenkins']
armenian_last_names = []
x = len(last_names) - 1
while x >= 0:
    if last_names[x][-3:] == 'yan':
        print(last_names[x])
        armenian_last_names.append(last_names[x])
        x -= 1
    else:
        x -= 1
print(armenian_last_names)

#2
long_word = 'arevachachapaylatakum'
count = 0
for char in long_word:
    if char == 'a':
        count += 1
    else:
        continue
print(count)


#3
alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numeric_alpabet = {}
x = 1
for item in alpabet:
   numeric_alpabet[item] = x
   x += 2
print(numeric_alpabet)

#4
x = 10
result = 1
while x:
    result *= x
    x -= 1
print(result)


#5
alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpabet_length = len(alpabet)
x = 0
while x < alpabet_length / 2:
    alpabet[x],alpabet[alpabet_length - x - 1] = alpabet[alpabet_length - x - 1],alpabet[x]
    print(alpabet[x],alpabet[alpabet_length - 1])
    x += 1
print(alpabet)

#Research
#enumerate() functian stextsum e enumarate tipi object tuplic kam ayl colectic,vori keyer@ tver en sksats 0-ic,erkrord paramtrov karogh enq tal skzbnakan index@