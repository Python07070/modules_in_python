#1 Write a Python program to generate a random color hex, a random alphabetical string, random value between two integers (inclusive) and a random multiple of 7 between 0 and 70. Use random.randint()
# import random
# import string
# #random color hex
# print("#{:06x}".format(random.randint(0, 0xFFFFFF)))
# #Generate a random alphabetical string
# alph_str = ""
# for i in range(random.randint(1, 10)):
#     alph_str += random.choice(string.ascii_letters)
# print(alph_str)
# #Generate a random value between two integers, inclusive:
# print(random.randint(0, 10))
# print(random.randint(-7, 7))
# print(random.randint(1, 1))
# #Generate a random multiple of 7 between 0 and 70S
# print(random.randint(0, 10) * 7)

#2 Write a Python program to select a random element from a list, set, dictionary (value) and a file from a directory. Use random.choice()
# import random
# import os
# #Select a random element from a list
# elements = [1, 2, 3, 4]
# print(random.choice(elements))
# #Select a random element from a set
# elements = set([1, 2, 3, 4])
# print(random.choice(tuple(elements)))
# #Select a random value from a dictionary
# d = {"a": 1, "b": 2, "c": 3}
# key = random.choice(list(d))
# print(d[key])
# #Select a random file from a directory
# print(random.choice(os.listdir("/")))

#3 Write a Python program to generate a random alphabetical character, alphabetical string and alphabetical string of a fixed length. Use random.choice()
# import random
# import string
# #Generate a random alphabetical character
# print(random.choice(string.ascii_letters))
# #Generate a random alphabetical string
# str1 = ""
# for i in range(random.randint(1, 100)):
#     str1 += random.choice(string.ascii_letters)
# print(str1)
# #Generate a random alphabetical string of a fixed length
# str1 = ""
# for i in range(10):
#     str1 += random.choice(string.ascii_letters)
# print(str1)

#4 Write a Python program to construct a seeded random number generator, also generate a float between 0 and 1, excluding 1. Use random.random()
# import random
# #Construct a seeded random number generator
# print(random.Random().random())
# print(random.Random(0).random())
# #Generate a float between 0 and 1, excluding 1
# print(random.random())

#5Write a Python program to generate a random integer between 0 and 6 - excluding 6, random integer between 5 and 10 - excluding 10, random integer between 0 and 10, with a step of 3 and random date between two dates. Use random.randrange()
# import random
# import datetime
# #Generate a random integer between 0 and 6
# print(random.randrange(5))
# #Generate random integer between 5 and 10, excluding 10
# print(random.randrange(start=5, stop=10))
# #Generate random integer between 0 and 10, with a step of 3
# print(random.randrange(start=0, stop=10, step=3))
# #Random date between two dates
# start_dt = datetime.date(2019, 2, 1)
# end_dt = datetime.date(2019, 3, 1)
# time_between_dates = end_dt - start_dt
# days_between_dates = time_between_dates.days
# random_number_of_days = random.randrange(days_between_dates)
# random_date = start_dt + datetime.timedelta(days=random_number_of_days)
# print(random_date)

#6 Write a Python program to shuffle the elements of a given list.
# import random
# words = ['red', 'black', 'green', 'blue']
# random.shuffle(words)
# print(words)

#7 Write a Python program to generate a float between 0 and 1, inclusive and generate a random float within a specific range. Use random.uniform()
# import random 
# print(random.uniform(0, 1))
# random_float = random.uniform(1.0, 3.0)
# print(random_float)

#8 Write a Python program to create a list of random integers and randomly select multiple items from the said list.
# import random 
# population = range(0, 100)
# nums_list = random.sample(population, 10)
# print(nums_list)
# no_elements = 4
# result_elements = random.sample(nums_list, no_elements)
# print(result_elements)
# no_elements = 8
# result_elements = random.sample(nums_list, no_elements)
# print(result_elements)

#9 Set a random seed and get a random number between 0 and 1
# import random 
# random.seed(2)
# new_random_value = random.random()
# print(new_random_value)


#Module - types

#1 Write a Python program to check if a function is a user-defined function or not. Use types.FunctionType, types.LambdaType()
# import types
# print(isinstance(lambda x: x, types.FunctionType))
# print(isinstance(abs, types.LambdaType))

#2 Write a Python program to check if a given value is a method of a user-defined class. Use types.MethodType()
# import types
# class C:
#     def x():
#         return 1
#     def y():
#         return 1            
# def b():
#     return 2
# print(isinstance(C().x, types.MethodType))
# print(isinstance(C().y, types.MethodType))
# print(isinstance(b, types.MethodType))

#3 Write a Python program to check if a given function is a generator or not. Use types.GeneratorType()
# import types
# def a(x):
#     yield x        
# def b(x):
#     return x
# print(isinstance(a(456), types.GeneratorType))
# print(isinstance(b(823), types.GeneratorType))

#4 Write a Python program to check if a given value is compiled code or not. Also check if a given value is a module or not. Use types.CodeType, types.ModuleType()
# import types
# code = compile("print('Hello')", "sample", "exec")
# print(isinstance(code, types.CodeType))
# print(isinstance("print(abs(-111))", types.CodeType))
# print(isinstance(types, types.ModuleType))

#modul decimal

#1  Write a Python program to construct a Decimal from a float and a Decimal from a string. Also represent the Decimal value as a tuple. Use decimal.Decimal
# import decimal
# pi_val = decimal.Decimal(3.14159)
# print(pi_val)
# print(pi_val.as_tuple())
# num_str = decimal.Decimal("123.25")
# print(num_str)
# print(num_str.as_tuple())

#2 Write a Python program to configure the rounding to round up and round down a given decimal value. Use decimal.Decimal
# import decimal
# decimal.getcontext().prec = 1
# decimal.getcontext().rounding = decimal.ROUND_UP
# print(decimal.Decimal(30) / decimal.Decimal(4))
# decimal.getcontext().prec = 3
# decimal.getcontext().rounding = decimal.ROUND_DOWN
# print(decimal.Decimal(30) / decimal.Decimal(4))

#3 Write a Python program to round a Decimal value to the nearest multiple of 0.10, unless already an exact multiple of 0.05. Use decimal.Decimal
# from decimal import Decimal
# def round_to_10_cents(x):
#     remainder = x.remainder_near(Decimal('0.10'))
#     if abs(remainder) == Decimal('0.05'):
#         return x
#     else:
#         return x - remainder
# for x in range(80, 120):
#     y = Decimal(x) / Decimal('1E2')
#     print("{0} rounds to {1}".format(y, round_to_10_cents(y)))

#4 Configure the rounding to round to the floor, ceiling
# import decimal
# decimal.getcontext().prec = 4
# decimal.getcontext().rounding = decimal.ROUND_FLOOR
# print(decimal.Decimal(20) / decimal.Decimal(6))
# decimal.getcontext().prec = 4
# decimal.getcontext().rounding = decimal.ROUND_CEILING
# print(decimal.Decimal(20) / decimal.Decimal(6))

#5
# import decimal
# decimal.getcontext().prec = 1
# decimal.getcontext().rounding = decimal.ROUND_HALF_DOWN
# print(decimal.Decimal(10) / decimal.Decimal(4))
# decimal.getcontext().prec = 1
# decimal.getcontext().rounding = decimal.ROUND_HALF_UP
# print(decimal.Decimal(10) / decimal.Decimal(4))

#6 Write a Python program to configure the rounding to round to the nearest, with ties going to the nearest even integer. Use decimal.ROUND_HALF_EVEN
# import decimal
# decimal.getcontext().prec = 1
# decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN
# print(decimal.Decimal(10) / decimal.Decimal(4))  

#7 Write a Python program to display a given decimal value in scientific notation. Use decimal.Decimal
# import decimal
# def format_e(n):
#     a = '%E' % n
#     return a.split('E')[0].rstrip('0').rstrip('.') + 'E' + a.split('E')[1]
# print(format_e(decimal.Decimal('40800000000.00000000000000')))

#module copy

#1 Write a Python program to create a shallow copy of a given list. Use copy.copy
# import copy
# nums = [1, 2, 3]
# nums_copy = copy.copy(nums)
# # print(nums_copy)

# #2 Write a Python program to create a deep copy of a given list. Use copy.copy
# import copy
# nums = [1, 2, 3, 4]
# nums_deepcopy = copy.deepcopy(nums)
# print(nums_deepcopy)

# #3 Write a Python program to create a shallow copy of a given dictionary. Use copy.copy
# import copy
# nums = {"a":1, "b":2, "c":3}
# nums_copy = copy.copy(nums)
# print(nums_copy)

# #4 Write a Python program to create a deep copy of a given dictionary. Use copy.copy
# import copy
# nums = {"a":1, "b":2, "c":3}
# nums_copy = copy.deepcopy(nums)
# print(nums_copy)

#module csv

#1 Write a Python program to read and display the content of a given CSV file. Use csv.reader
# import csv
# reader = csv.reader(open("for_csv.csv"))
# for i in reader:
#     print(i)

#2 Write a Python program to count the number of lines in a given CSV file. Use csv.reader
# import csv
# reader = csv.reader(open("for_csv.csv"))
# len_of_csv_lines = len(list(reader))
# print(len_of_csv_lines)

#3 Write a Python program to parse a given CSV string and get the list of lists of string values. Use csv.reader
# import csv
# csv_string = """1,2,3
# 4,5,6
# 7,8,9
# """
# lines = csv_string.splitlines()
# reader = csv.reader(lines)
# parsed_csv = list(reader)
# print("\nList representation of the CSV file:")
# print(parsed_csv)

#4  Write a Python program to read the current line from a given CSV file. Use csv.reader
# import csv
# f = open("for_csv.csv", newline='')
# csv_reader = csv.reader(f)
# print(next(csv_reader))

#5 Write a Python program to skip the headers of a given CSV file. Use csv.reader
# import csv
# f = open("for_csv.csv", "r")
# reader = csv.reader(f)
# next(reader)
# for i in reader:
#     print(i)

#6 Write a Python program to write (without writing separate lines between rows) and read a CSV file with specified delimiter. Use csv.reader
# import csv     
# csv_opener = open("test.csv", "w", newline='')
# writer = csv.writer(csv_opener, delimiter = ",")
# writer.writerow(["a","b","c"])
# writer.writerow(["d","e","f"])
# writer.writerow(["g","h","i"])
# csv_opener.close()
# csv_redact = open("test.csv", "r")
# csv = csv.reader(csv_redact, delimiter = ",")
# for i in csv:
#   print(i) 
# csv_redact.close()

#7 Write a Python program to write dictionaries and a list of dictionaries to a given CSV file. Use csv.reader
# import csv
# fw = open("test.csv", "w", newline='')
# writer = csv.DictWriter(fw, fieldnames=["Name", "Class"])
# writer.writeheader()
# writer.writerow({"Name": "Jasmine Barrett", "Class": "V"})
# writer.writerow({"Name": "Garry Watson", "Class": "V"})
# writer.writerow({"Name": "Courtney Caldwell", "Class": "VI"})
# fw.close()
# fr = open("test.csv", "r")
# csv = csv.reader(fr, delimiter = ",")
# for i in csv:
#   print(i) 
# fr.close()