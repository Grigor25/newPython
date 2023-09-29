class Car:
    headlights_count = 4

    def __init__(self, horsepower, weight, engine_type, wheels_count):
        self.horsepower = horsepower
        self.weight = weight
        self.engine_type = engine_type
        self.wheels_count = wheels_count

    def max_speed(self):
        return self.horsepower / self.weight * 1500

    @staticmethod

    def weight_change(self, weigth):
        self.weight = weigth
    # @classmethod
    # def weight_change(new_weight):
    #     weight = new_weight


class Bus(Car):
    def __init__(self, horsepower, weight, engine_type, wheels_count, max_seats, busy_seats=0):
        self.horsepower = horsepower
        self.weight = weight
        self.engine_type = engine_type
        self.wheels_count = wheels_count
        self.max_seats = max_seats
        self.busy_seats = busy_seats

    def add_busy_sets(self):
        self.busy_seats += 1

    def free_seats(self):
        return self.max_seats - self.busy_seats


bmw = Car(1500, 200, 8, 4)
opel = Car(400, 50, 20, 4)
busm = Bus(500, 20, 20, 20, 40)

print(busm.free_seats())
busm.add_busy_sets()
print(dir(busm))
print(busm.free_seats())
print(busm.max_speed())

print(bmw.max_speed(), opel.max_speed())

# Reasearch


# __dict__ @ cuyc e talis objecti atributner@ __initov__trvats  isk dir funcian cuyc e talis classi ev objecti
# @ndhanur bolor atributner@ ev methodner@
