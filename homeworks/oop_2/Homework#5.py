
# class Laptop:
#     def __init__(self):
#         self.battery = Battery()
#
#
#
# class Battery:
#     def __init__(self):
#         pass
#
#
#     laptop = Laptop












#
# class Guitar:
#     def __init__(self, string):
#         self.string = string
#
#
# class GuitarString:
#     def __init__(self):
#         pass
#
#
# string = GuitarString()
# guitar = Guitar(string)

# class Clarc:
#
#     @staticmethod
#     def add_nums(a, b, c):
#          d = a + b + c
#          return print(f'd = {d}')
#
# Clarc.add_nums(7, 15, 20)


# class Pasta:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#
#     def __repr__(self):
#         return f'Pasta({self.ingredients})'
#
#     @classmethod
#     def carbonara(cls):
#         return cls(['forcemeat', 'tomatoes'])
#
#     @classmethod
#     def bolognaise(cls):
#         return cls(['bacon', 'parmesan', 'eggs'])
#
#
# print(Pasta.carbonara())
# print(Pasta.bolognaise())



# class Concert:
#     def __init__(self, max_visitors_num):
#         self.max_visitors_num = max_visitors_num




# import dataclasses
#
# @dataclasses.dataclass
# class AdressBookDataClass:
#     key: int
#     name: str
#     phone_number: str
#     address: str
#     email: str
#     birthday: str
#     age: int

# from collections import namedtuple
#
# AdressBookDataClass = namedtuple('AdressBookDataClass', ['key', 'name', 'phone_number', 'adress', 'email', 'birthday', 'age'])
#
# adress = AdressBookDataClass('225', 'Denis', '+380730991***', 'Strokova street', 'denis.spodin.003@gmail.com', '6 of November', 17)
#
#
# print(adress.key)
# print(adress.name)
# print(adress.phone_number)
# print(adress.adress)
# print(adress.email)
# print(adress.birthday)
# print(adress.age)




# class AdressBook:
#     def __init__(self, key, name, phone_number, adress, email, birthday, age):
#         self.key = key
#         self.name = name
#         self.phone_number = phone_number
#         self.adress = adress
#         self.email = email
#         self.birthday = birthday
#         self.age = age
#
#     def __str__(self):
#         return f'Info about us {self.key} {self.name} {self.phone_number} {self.adress} {self.email} {self.birthday} {self.age}'
#
# adress = AdressBook('225', 'Denis', '+380730991***', 'Strokova street', 'denis.spodin.003@gmail.com', '6 of November', 17)
#
# print(adress)





# 9

class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    @property
    def full_name_info(self):
        return f'{self.name} {self.age} {self.country}'


name = "John"
age = 36
country = "USA"

person = Person('John', '36', 'USA')

setattr(person,'age', '42')

print('My name is', getattr(person, 'name'), 'and my age', getattr(person, 'age'))

# print(person.full_name_info)



# Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr

#10

# class Student:
#
#     def __init__(self, id, name, email):
#         self.id = id
#         self.name = name
#         self.email = email
#
#         id = 0
#         name = ""
#         email = ""
#
#
# student = Student('0', 'Denis', 'denis@gmail.com')
#
# setattr(student, 'email', 'denis@gmail.com')
#
# print('My name is', getattr(student, 'name'), 'and my email', getattr(student, 'email'))






#11

# class Celsius:
#
#     def __init__(self, temperature=0):
#         self.temperature = temperature
#
#     @property
#     def convert(self):
#         fahrenheit = (self.temperature * 1.8) + 32
#         return f'{fahrenheit} fahrenheit'
#
# lemon = Celsius(25)
#
# print(lemon.convert)





# class Concert:
#     def __init__(self, max_visitors_num, visitors_count):
#         self.max_visitors_num = max_visitors_num
#         self.visitors_count = visitors_count
#
#     def count_count(self):
#         if self.visitors_count > self.max_visitors_num:
#             self.visitors_count = self.max_visitors_num
#         return f'{self.visitors_count} members'
#
# concert = Concert(10000, 1000)
#
# print(concert.count_count())


















