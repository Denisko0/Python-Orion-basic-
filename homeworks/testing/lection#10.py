# import random
# import time
# class ZeroWaterException(Exception):
#     pass
#
# class ZeroBatteryCharge(Exception):
#     pass
#
#
#
#
#
#
# class WorkingVacuumCleaner:
#     def __init__(self, battery_charge, garbage, amount_of_water):
#         self.battery_charge = battery_charge
#         self.garbage = garbage
#         self.amount_of_water = amount_of_water
#
#     def move(self):
#
#
#         try:
#             self.washing()
#         except ZeroWaterException:
#             print('amount of water is not enough')
#
#
#         self.vacuum_clean()
#
#
#
#
#     def vacuum_clean(self):
#
#         self.battery_charge -= 3
#         if self.battery_charge <= 0:
#             print("i am discharged, take me to charge")
#             raise ZeroBatteryCharge
#
#         self.garbage += random.randint(0, 10)
#
#         if self.garbage >= 120:
#             print('leather bastards empty my trash can')
#
#
#
#     def washing(self):
#
#         self.amount_of_water -= 7
#         if self.amount_of_water <= 20:
#             print('Please, add some water')
#         if self.amount_of_water <= 0:
#             raise ZeroWaterException
#
#
#
#
#
#
#
# cleaner = WorkingVacuumCleaner (100, 0, 100)
#
# while True:
#     print('Cleaner amount of water:')
#     print(cleaner.amount_of_water)
#     cleaner.move()
#
#     time.sleep(0.5)
#
#     print('Cleaner charge:')
#     print(cleaner.battery_charge)
#
#
#     print('Cleaner garbage:')
#     print(cleaner.garbage)

                                                # CALCULATOR





import math
import logging

logging.basicConfig(level=logging.DEBUG, filename="info.log", filemode="a")



def add(n, m):
         return n + m

def subtract(n, m):
         return n - m

def multiplay(n, m):
         return n * m

def divide(n, m):
         return n / m

def exponentiation(n, m):
        return n ** m

def root(n):
         return math.sqrt(n)

def percentage(n, m):
        return n / 100 * m


while True:
    num1 = float(input("Enter first number: "))
    logging.info("Input nub1")

    print('Choice one of operations')
    print('1.Add')
    print('2.Subtracting')
    print('3.Multiplaying')
    print('4.Dividing')
    print('5.Exponentiating')
    print('6.Rooting')
    print('7.Percentaging')
    choice = input('Select (1/2/3/4/5/6/7): ')
    logging.info('Input choice')


    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        num2 = float(input('Enter second number: '))
        logging.info('Input nub2')
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            logging.info('start of addition')

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            logging.info("start substraction")

        elif choice == '3':
            print(num1, "**", num2, "=", multiplay(num1, num2))

        elif choice == "4":
            logging.info('start dividing')
            try:
                print(num1, "/", num2, "=", divide(num1, num2))
            except:
                print('float division by zero')
                logging.error("zero division error")

        elif choice == "5":
            print(num1, "<>", num2, "=", exponentiation(num1, num2))
            logging.info('start exponentiation')

        elif choice == "6":
            try:
                print("root from ", num1, '=', root(num1))
                logging.info('start rooting')
            except:
                print('error')
                logging.info("there can be no zero under the root")

        elif choice == "7":
            print(num1, "%", num2, "=", percentage(num1, num2))
            logging.info('starting percentage process')

        else:

            print("Invalid input")



