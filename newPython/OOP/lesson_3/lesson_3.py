class Animal:
    """Main Class"""
    def __init__(self, eyes, hands, lags, color, runing_speed=45):
        self.eyes = eyes
        self.hands = hands
        self.lags = lags
        self.color = color
        self.runing_speed = runing_speed

    def voice(self):
        return 'dzayn em hanum'

    def run(self):
        print(f'vazum em {self.runing_speed} aragutyamb')

    def __str__(self):
        return 'Animal'


class Cat(Animal):
    def __init__(self, *args):
        super().__init__(*args)

    def voice(self):
        return f'mlavelu {super().voice()}'

    def cat_run_voice(self):
        super().voice()
        print(self.run())

    def __str__(self):
        return 'Cat'



mumu = Cat(5, 2, 2, 2)
print(mumu.voice())
print(mumu.__dict__)



class Lion(Cat):
    def human_eat(self):
        print('human eat')

    def __str__(self):
        return 'Lion'
print(Animal.__doc__)
simba = Lion(4, 4, 4, 4)
print(simba.human_eat())

print(Animal.__bases__)
print(Cat.__bases__)


print(issubclass(Cat, Lion))
print(issubclass(Lion, Animal))

#Research

#__doc__   informacia e talis classi veraberyal
#__basse__ cuyc e talis clasi tsnox class@ te vor clasice jarangvum
#issubclass@ stugum e te arajin parametrov trvats object@ jarangum e erkrordic te voch