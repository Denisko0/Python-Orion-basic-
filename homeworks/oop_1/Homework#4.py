# class Vehicle:
#     def __init__(self, mileage, max_speed):
#
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#
#
# class Bus(Vehicle):
#         def __init__(self, capacity, mileage, max_speed):
#             super().__init__(mileage, max_speed)
#             self.capacity = capacity
#
#         def seating_capacity(self):
#             print(f"Bus capacity = {self.capacity}")
#
#
# Mersedes = Bus(24, 2000, 150)
#
# print("The 'Mersedes' belongs to", type(Mersedes))
#
#
# School_Bus = Vehicle(70, 95)
#
# print(isinstance(School_Bus, Vehicle))


# class School:
#     def __init__(self, get_school_id, number_of_students):
#         self.get_school_id = get_school_id
#         self.number_of_students = number_of_students
#
# class SchoolBus(School, Bus):
#
#         def __init__(self, color, get_school_id, number_of_students, capacity, mileage, max_speed,):
#             super().__init__(get_school_id, number_of_students, capacity, mileage, max_speed)
#             self.school_bus_color = school_bus_color



# class Bear:
#     def make_sound(self):
#         print("Rawrr")
#
#
# class Wolf:
#     def make_sound(self):
#         print("Wooo")
#
# wolf = Wolf()
# bear = Bear()
#
# for animal in (wolf, bear):
#     animal.make_sound()


class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def check_population(self):
        if self.population > 1500:
            return print(f'The population of the city {self.name}, is {self.population}')
        else:
            return print(f'Your city is too small')

moscow = City("Moscow", 11000000)
vishniaki = City("Vishniaki", 1300)

moscow.check_population()
vishniaki.check_population()



















