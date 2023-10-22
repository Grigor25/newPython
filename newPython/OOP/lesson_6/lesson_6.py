#polimorfizm@ tuyl e talis pyhonum nuyn  method@ operator@ objectner@ ogtagortsel tarber scanarnerov

class TeslaMotors:
    names = ['Model S', 'Roadster', 'Model 3', 'Cybertruck', 'Model Y', 'Model X']
    body_types = ['Sedan', 'Coupe', 'Sedan', 'Truck', 'SUVS', 'SUVS']
    engine_types = ['Electric', 'Electric', 'Electric', 'Electric', 'Electric']
    value = 0
    default_var = names
    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.value < len(self.default_var):
            self.value += 1
            return self.default_var[self.value - 1]
        else:
            raise StopIteration

    def __contains__(self, item):
        return item in self.default_var

    def set_iter_by(self,name):
        if name == 'body_types':
            self.default_var = self.body_types
        elif name == 'names':
            self.default_var = self.names
        elif name == 'engine_types':
            self.default_var = self.engine_types




tes = TeslaMotors()

tes.set_iter_by('body_types')

for item in tes:
    print(item)

print("Sedan" in tes)
tes.set_iter_by('names')
print('Coupe' in tes)
print('Model S' in tes)



#Reasearch


#__call__ method@ hnaravorutyun@ tasli clasic stextsvats object@ kanchel sovorakan funciayi naman

# <  >  metsi ev poqri nshannernen