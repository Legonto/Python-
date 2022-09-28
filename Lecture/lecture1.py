from re import S


# print ('hello')
# Типы данных и переменная
# int, float, boolean, str, list, None
# value = None # присваиваем ничего, потом можем использовать
# # print(type(value))
# a = 123
# print(a)
# print(type(a)) # пишем type чтобы узнать тип переменной
# b = 1.23
# print(b)
# # print(type(b))
# value = 12345
# print(value)
# # print(type(value))
# s = 'hello'
# print(s)
# # print(type(s))
# print(a,b,s)
# разные способы вывода
# print(a,'-',b,'-',s)
# print('{} - {} - {}'.format(a,b,s)) # можно поменять порядок вывода,
# # для этого в {} мы пишем цыфры от 0 в том порядке который нужен а=0,b=1,s=2
# print(f'{a} - {b} - {s}')

# f = True
# t = False
# print(f)
# print(t)

# list = [1,2,3, 'hello', 1.23, 3.56] # массив
# print(list)

# print() - отвечает за вывод данных
# input() - отвечает за ввод данных

# print('Введите а')
# a = input()  #12
# print('Введите б')
# b = input()   #56
# print(a,b)
# print(f'{a} {b}')
# print('{} {}'.format(a,b))
# print(a,'+',b,'=', a+b) # вывод будет в строку например 1256

# чтобы программа понимала что мы ввели число, нужно добавить int
# print('Введите а')
# a = int(input())  #12
# print('Введите б')
# b = int(input())   #56
# print(a,b)
# print(f'{a} {b}')
# print('{} {}'.format(a,b))
# print(a,'+',b,'=', a+b) # вывод уже будет 68

# для вещественных чисел пишем float
# print('Введите а')
# a = float(input())  #1.2
# print('Введите б')
# b = float(input())   #5.6
# print(a,b)
# print(f'{a} {b}')
# print('{} {}'.format(a,b))
# print(a,'+',b,'=', a+b) # вывод уже будет 6.8

#Арифметические операции
# +, -,*, /, %, //,**
# Приоритет операций
# **, ⊕, ⊖,*, /, //, %, +, -
# ( ) Скобки меняют приоритет

# a = 6
# b = 4 # -4 унарный минус, обычное отрицательное число
# c = a+b
# print(c) #10
# n = a-b
# print(n) #2
# g = a*b
# print(g) # 24, если какое то число вещественное а = 1.234 то лучше написать так 
# # g = round(a*b, 5) через , ставим количество цифр после запятой
# d = a/b
# print(d) #1.5
# f = a//b 
# print(f) # 1 два знака деления также делят, только в выводе число округляется до целого
# o = a%b
# print(o) # 2 показывает остаток от деления
# s = a**b
# print(s) # 1296 a возводит в степень b

#  Сокращенные операции
# a = 4
# # a = a + 3
# a += 3 # так же и для других ари фметических операций
# print(a)

# Логические операции
# >, >=, <, <=, == равенство, != неравенство
# not, and, or – не путать с &, |, ^
# is, is not, in, not in

# a = 1 > 3
# print(a) # будем получать True или False

# можно сравнить строки
# a = 'qwe'
# b = 'qwe'
# print(a == b)

# можно сравнить списки, сравнение идет поэлементно
# a = [1,2]
# b = [1,2]
# print(a == b)

# можно сравнивать тройные неравенства или более
# a = 1 < 3 < 6
# print(a)

# f = 1 > 2 or 4 < 6
# print(f) # будет true тк хотя бы одно утверждение верно

# f = [1,2,3]
# print(f)
# # print(2 in f)
# # print(not 2 in f)

# # проверим является ли число четным
# # is_odd = f[0] % 2 == 0 # можно и так но лучше по другому 
# is_odd = not f[0] % 2
# print(is_odd) 

# Управляющие конструкции: if, if-else, elif

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else: 
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Ура, это же Марина!')
# elif username == 'Ильнар':
#     print('Ура, это же Ильнар!')    
# else:
#     print('Привет, ', username)

# Управляющие конструкции: while
# Цикл позволяет выполнить блок операторов какоето количество раз
# while condition:
 # operator 1
 # operator 2
 # . . .
 # operator n

# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# print(inverted)

# Управляющие конструкции: while-else
# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# else:
#  print('Пожалуй')
#  print('хватит )')
# print(inverted)

# Управляющие конструкции: for
# Когда мы знаем, что хотим
# for i in enumeration:
 # operator 1
 # operator 2
 # . . .
 # operator n

# for i in 1, -2, 3, 14, 5:
#     print(i)  
  
# list = [1, -2, 3, 14, 5]
# for i in list:
#      print(i) 

# r = range(10)
# for i in r:
#     print(i)

# for i in range(5):
#      print(i)

# for i in range(1, 5): # выдаст числа от 1 до 4
#      print(i)

# for i in range(1, 10, 2): # выдаст числа от 1 до 9, с шагом 2
#      print(i)

# for i in 'qwer - ty': # строки мы тоже можем разбить по знаково
#      print(i) 

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39, сколько символов
# print('ещё' in text) # True, ищем нужное слово
# print(text.isdigit()) # False, является ли числами
# print(text.islower()) # True, буквы нижнего регистра
# print(text.replace('ещё','ЕЩЁ')) # замена
# for c in text:
#  print(c)

# подсказка, если забыл что означает какая то функция то можно написать:
# help(str) # чтобы выйти в терминале из этого режима, нужно нажать q

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text) от 0 до последнего
# print(text[:2]) # съ от 0 до 2
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...
# print(text)

# Список – пронумерованная, изменяемая коллекция
# объектов произвольных типов

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

# Функции
# Это фрагмент программы, используемый многократно
# def function_name(x):
# body line 1
# . . .
# body line n
 # optional return

def f(x):
    if x == 1:
        return 'Целое'
    elif x ==2.3:
        return 23
    else:
        return

arg = 1
print(f(arg))
print(type(f(arg)))