1


# Mutable баъд аз сохтан тағйир додан мумкин аст масалан list
# Immutable тағйир намеёбад масалан int, str ва tuple


# numbers = [1, 2]
# numbers.append(3)  
# word = "салом"
# word = word + "!"  
# print(word)
# print(numbers)


2


# try блоки кодеро месанҷад; except истиснои муайянро коркард мекунад
# finally новобаста аз кор карданаш он иҷро мешавад


# try:
# 	number = int(input("Enter number: "))
# 	a = int(input("Enter second number: "))
# 	print(f"{number} % {a} = {number % a}")
# except ValueError:
# 	print("Invalid input")
# finally:
# 	print("Finshed")



3

# list бо индекс кор мекунад ва тагиребанда ва тартиб дорад  
# tuple ҳам индекс дорад тартиб дорад вале тагирнопазир аст
# tuple бфрои маълумоти собит кардан аст ва онро мо метавонем калиди дикшнири истифидо барем


# fruits = ["себ", "нок"]
# point = (3, 5)
# print(fruits[1])
# print(point)



4


# Тағйирёбанда номест ки ба объект ишора мекунад 
# int  адади бутун,
# float — адади касрӣ
# str — матн
# bool — True ё False.

# age = 20
# temperature = 36.6
# name = "Али"
# is_student = True




5


# def fibonacci(n):
#     a = []
#     a, b = 1, 1

#     for i in range(n+1):
#         a.append(a)
#         a, b = b, a + b

#     return a


# print(fibonacci(5))





6

# even = [i for i in range(1, 51) if i % 2 == 0 and i % 3 == 0]
# print(even)


7


# with open("text.txt", "r") as file:
#     lines = file.readlines()
# print("lines:", len(lines))

8


# def word_count(text):
#     text = text.lower()
#     for i in ".,!?":
#         text = text.replace(i, "")
#     words = text.split()
#     dicts = {}
#     for i in words:
#         if i in dicts:
#             dicts[i] += 1
#         else:
#             dicts[i] = 1

#     return dicts


# print(word_count("Hello, hello! Python is great. Python is fun."))


9



# class BankAccount:
# 	def __init__(self, owner, balance=0):
# 		self.owner = owner
# 		self.balance = balance

# 	def deposit(self, amount):
# 		self.balance += amount

# 	def withdraw(self, amount):
# 		if amount <= self.balance:
# 			self.balance -= amount
# 		else:
# 			print("Your pure")

# 	def __str__(self):
# 		return f"Owner: {self.owner}, Balance: {self.balance}"

# Alice = BankAccount("Alice" , 1000)
# Alice.deposit(500)
# Alice.withdraw(2000)
# print(Alice)


10



# import time

# def timing_decorator(func):
#     def inner(*args, **kwargs):
#         s_t = time.time()
#         result = func(*args, **kwargs)
#         e_t = time.time()
#         print(f"Start at: {s_t} Second and End at: {e_t} second")
#         return result
#     return inner

# @timing_decorator
# def calculate_sum():
#     total = 0
#     for i in range(1, 1000000):
#         total += i
#     print("Sum:", total)
# calculate_sum()




11

# экстра эгзамин 

