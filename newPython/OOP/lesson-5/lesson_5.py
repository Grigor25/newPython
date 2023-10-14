import re

#3
class FilterText:
    text = '055-445-789 E.Mask 124.06.2014 093-587-135 Nemo 1.09.1887 E.Auditore 24.17.2020 096-2288-987 R.Rocknrolla'

    def __getattr__(self, item):
        if item == 'names':
            return re.findall(r'[A-Z][.][A-Z][a-z]*',self.text)
        elif item == 'dates':
            return re.findall("[0-9]{1,2}$.[0-9]{2}.[0-9]{4}" ,self.text)
        elif item == 'phone_numbers':
            return re.findall(r'[0-9]{3}[-][0-9]{3}[-][0-9]{3}',self.text)
        else:
            return True

    def __getitem__(self, item):
        return self.text.split(' ')[item]

    def __setitem__(self, key, value):
        result = self.text.split(' ')
        result[key] = value
        self.text = result


x = FilterText()

print(x.names)
print(x.dates)
print(x.phone_numbers)
print(x[1])
print(x[1:3])
x[0] = 'G.Ritchie'
print(x.text)









#Research


#__bool__ methodi veradacrats arjeq@  classi True kam false linelne cuyc talis
#__len__ method@ veradzrcnume objecti erkarutyun@ vori vra vor kanchel enq


#skzbic ashxatume __bool__ @ ete ayn chka ashxatacnum e __len__@


#