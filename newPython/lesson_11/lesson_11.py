#1
users = []
users_list = []
with open('db.txt') as f:
    for index, item in enumerate(f):
        users.append(item.rstrip().split(','))
    keys = users.pop(0)
    users.append(list(('Grigor','Manukyan','28','enginer','Echmiadzin','Gladiator','2Pac','Lays')))
    for elem in users:
        users_list.append(dict(zip(keys, elem)))

#1.2
def add_descr(users_list, **kwargs):
    for item in users_list:
         item.update(kwargs)


add_descr(users_list, car = 45)



#1.3
with open('db.txt','w') as file:
    file.writelines(','.join(list(users_list[0].keys())))
    for item in users:
        print(item)
        file.writelines(f"\n{','.join(item)}")



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


#aranc list

def get_item_2(numb):
    if type(numb) == int:
        print(numb)
        return numb
    else:
        return get_item(numb[0])


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
