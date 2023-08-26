#1
users = []
users_list = []
with open('db.txt') as f:
    for index,str in enumerate(f):
        users.append(str.split(','))
        print(str)
    discr = users.pop(0)
    for elem in users:
        users_list.append(dict(zip(discr,elem)))
    print(users_list)

def add_descr(users_list,**kwargs):
    print(kwargs)
    for item in users_list:
        item.update(kwargs)


add_descr(users_list,car = 45)
print(users_list)

#2
numb = [[[[[10]]]]]


def get_item(numb):
    for item in numb:
        if type(item) == int:
            print(item)
            return item
        else:
            get_item(item[0])
    return item


get_item(numb)

##

#3.
numbers = [1, 2, [3, 4], [5, 6, [10, 19]]]
result = 0


def items_sum(numbers):
    global result
    for item in numbers:
        if type(item) == int:
            result += item
        else:
            items_sum(item)
    return result


print(items_sum(numbers))

#Research

# lambdan ananun funckcia e vor@ @ndunume cankacac qanaki parametr bayc veradarcnum mek artahaytutyan arjeq
