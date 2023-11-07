
# WS 06.11.2023

# class Point():
#     def __new__(cls, *args, **kwargs):
#         print('method new')
#         return super().__new__(cls)
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p = Point(2,8)
# print(p.x)

# class DataBase:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self, user, password, port):
#         self.user = user
#         self.password = password
#         self.port = port
#
#     def __del__(self):
#         print('hbgr')
#         DataBase.__instance = None
#
#     def connect(self):
#         print(f'Соединение с БД: {self.user}, {self.password}, {self.port}')
#
#     def close(self):
#         print('Соединение разорвано')
#
#     def read(self):
#         print('Чтение данных')
#
#     def write(self, data):
#         print(f'Записываем данные {data}')
#
#
# db = DataBase('user1', 'psw1', '8000')
# db2 = DataBase('user1', 'psw1', '8000')
# print(db)
# print(db2)


# class Test:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Test string'
#
#
# t = Test('comp')
# t2 = Test('phone')
# print(t.name)
# print(t2)


# class Clock:
#     __DAY = 86400
#
#     def __init__(self, seconds : int):
#         if not isinstance(seconds, int):
#             raise TypeError('Нужно ввести целое число')
#         self.seconds = seconds % self.__DAY
#
#     def get_time(self):
#         s = self.seconds % 60
#         b = self.seconds // 60 % 60
#         h = self.seconds // 3600 % 24
#         return f'{s}:{b}:{h}'
#
#     def __eq__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise TypeError('Нужно ввести целое число')
#         # if isinstance(other, int):
#         #     other = other
#         # else:
#         #     other = other.seconds
#         sc = other if isinstance(other, int) else other.seconds
#         return self.seconds == sc
#
#     def __lt__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise TypeError('Type error')
#         sc = other if isinstance(other, int) else other.seconds
#         return self.seconds <= sc
#
#     def __add__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError('не можем сложить')
#
#     def __iadd__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError('не можем сложить')
#
#         sc = other if isinstance(other, int) else other.seconds
#         return Clock(self.seconds + sc)
#
#
# cl = Clock(86400)
# cl2 = Clock(54)
# cl3 = Clock(155)
# print(cl.get_time())
# cl = cl + cl2 + cl3
# print(cl.get_time())


# class Passport:
#
#     def __init__(self, first_name, last_name, country, data_at_birth, num_of_passport):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.country = country
#         self.date_at_birth = data_at_birth
#         self.num_of_passport = num_of_passport
#
#     def printinfo(self):
#         print(f'''
# Full name: {self.first_name} {self.last_name}
# Date of birth: {self.date_at_birth}
# Country: {self.country}
# Passport: {self.num_of_passport}''')
#
#
# class ForeignPassport(Passport):
#
#     def __init__(self, first_name, last_name, country, data_at_birth, num_of_passport, VISA):
#         super().__init__(first_name, last_name, country, data_at_birth, num_of_passport)
#         self.VISA = VISA
#
#     def printinfo(self):
#         super().printinfo()
#         print('VISA', self.VISA)
#
#     def __repr__(self):
#         return f'Name: {self.first_name} {self.last_name} \n Passport: {self.num_of_passport}'
#
# MFC = []
# p = Passport('Ivan', 'Ivanov', 'Russia', '30.05.2007', '9221 948888')
# MFC.append(p)
# fp = ForeignPassport('Petr', 'Petrov', 'Russia', '30.05.2006', '9221 948886', 'China')
# MFC.append(fp)
# print(MFC)
# for item in MFC:
#     item.printinfo()


# class Equipment:
#
#     def __init__(self, name, nake, year):
#         self.name = name
#         self.nake = nake
#         self.year = year
#
#     def action(self):
#         return 'не определено'
#
#     def __str__(self):
#         return f'{self.name}, {self.nake}, {self.year}. Умеет {self.action()}'
#
#     def __le__(self, other):
#         if not isinstance(other, Equipment):
#             raise TypeError
#         return self.year <= other.year
#
# class Printer(Equipment):
#
#     def __init__(self, series, name, nake, year):
#         super().__init__(name, nake, year)
#         self.series = series
#
#     def action(self):
#         return 'печатает'
#
#     def __str__(self):
#         return f'{self.series}, {self.name}, {self.nake}, {self.year}'
#
#
#
#
# class Scaner(Equipment):
#
#     def __init__(self, name, nake, year):
#         super().__init__(name, nake, year)
#
#     def action(self):
#         return 'сканирует'
#
# class Xerox(Equipment):
#
#     def __init__(self, name, nake, year):
#         super().__init__(name, nake, year)
#
#     def action(self):
#         return 'сканирует в комп'
#
# def allitems(sklad):
#     for item in sklad:
#         if isinstance(item):
#             print(item)
#
# def get_items (sklad, ename):
#     for item in sklad:
#         if isinstance(item, ename):
#             print(item)
#
# sklad = []
# e = Equipment('ЧыК-ЧырыК', 'X', 2345)
# sklad.append(e)
# s = Printer('Попугей', 'Xhfgd', 'sdfvd', 2545)
# sklad.append(s)
# x = Xerox('Путин', 'X', 2565)
# sklad.append(x)
# e = Equipment('ЧыК-ЧырыК', 'X', 2345)
# sklad.append(e)
# s = Printer('Попугей', 'X', 'Xhfgd', 2545)
# sklad.append(s)
# x = Xerox('Путин', 'X', 2565)
# sklad.append(x)
# # allitems(sklad)
# get_items(sklad, Equipment)


# from random import randint
# class Soldier:
#     def __init__(self,name='Noname', health=100):
#         self.name = name
#         self.health = health
#     def set_name(self, name):
#         self.name = name
#     def make_kick(self, enemy):
#         enemy.health -= 20
#         if enemy.health < 0 :
#             enemy.health = 0
#             self.health += 10
#             print(self.name, "бьет", enemy.name)
#             print('%s = %d' % (enemy.name, enemy.health))
#
# class Battle:
#     def __init__(self,u1,u2):
#         self.u1 = u1
#         self.u2 = u2
#         self.result = "Сражения не было"
#     def battle(self):
#         while self.u1.health > 0 and self.u2.health > 0:
#             n = randint(1, 2)
#             if n == 1:
#                 self.u1.make_kick(self.u2)
#             else:
#                 self.u2.make_kick(self.u1)
#             if self.u1.health > self.u2.health:
#                 self.result = self.u1.name + " ПОБЕДИЛ"
#             elif self.u2.health > self.u1.health:
#                 self.result = self.u2.name + " ПОБЕДИЛ"
#     def who_win(self):
#         print(self.result)
#
#
# first = Soldier('Алкаш',140)
# second = Soldier()
# second.set_name('Бомж')
# b = Battle(first,second)
# b.battle()
# b.who_win()



# import random
# class Card():
#     NumsList = ["Джокер",'2','3','4','5','6','7','8','9','10',"Валет","Дама","Король","Туз"]
#     MastList = ["пик","крестей","бубей","червей"]
#
#     def __init__(self, i, j):
#         self.Mastb = self.MastList[i-1]
#         self.Num = self.NumsList[j-1]
#
#
# class DeckOfCards():
#     def __init__(self):
#         self.deck = [None] * 56
#         k = 0
#         for i in range(1, 4 + 1):
#             for j in range(1, 14 + 1):
#                 self.deck[k] = Card(i, j)
#                 k += 1
#
#     def shuffle(self):
#         random.shuffle(self.deck)
#
#     def get(self, i):
#         if 0 <= i <= 55:
#             answer = self.deck[i].Num
#             answer += " "
#             answer += self.deck[i].Mastb
#         else:
#             answer = "В колоде только 56 карт"
#         return answer
#
#
# deck = DeckOfCards()
# deck.shuffle()
# print('Выберите карту из колоды в 56 карт:')
# n=int(input())
# if n <= 56 :
#     card = deck.get(n-1)
#     print('Вы взяли карту: ', card, end='.\n')
# else :
#     print("В колоде только 56 карт")


# import math
#
#
# class Triangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def increase_side(self, num, p):
#         if num == 1:
#             self.a += self.a * (p / 100)
#         elif num == 2:
#             self.b += self.b * (p / 100)
#         else:
#             print("Error")
#
#     def decrease_side(self, num, p):
#         if num == 1:
#             self.a -= self.a * (p / 100)
#         elif num == 2:
#             self.b -= self.b * (p / 100)
#         else:
#             print("Error")
#
#     def radius(self):
#         return (self.a * self.b * math.sqrt(self.a ** 2 + self.b ** 2)) / (
#                     self.a + self.b + math.sqrt(self.a ** 2 + self.b ** 2))
#
#     def perimeter(self):
#         return self.a + self.b + math.sqrt(self.a ** 2 + self.b ** 2)
#
#     def angles(self):
#         angle1 = math.degrees(math.atan(self.a / self.b))
#         angle2 = math.degrees(math.atan(self.b / self.a))
#         return angle1, angle2
#
#
# triangle = Triangle(int(input()), int(input()))
# triangle.increase_side(int(input()), int(input()))
# triangle.decrease_side(int(input()), int(input()))
# print("Радиус описанной окружности:", triangle.radius())
# print("Периметр:", triangle.perimeter())
# print("Углы:", triangle.angles())

