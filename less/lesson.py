# def plus(a, b):
#     return a + b
#
#
# def minus(a, b):
#     return a - b
#
# def delenie(a, b):
#     return a / b
# if __name__ == '__main__':
#     print(plus(2, 5))
#     print(minus(2, 5))
#     print(delenie(2, 5))

# a = list(map(int, input()))
# print(a)
#
# if sum(a[:3]) == sum(a[-3:]):
#     print('Nice')
# else:
#     print('Ass')


# print(73 // 10) # сколько раз правая часть входит в левую  = 7
# print(73 % 10) # делится 73/10 и пишется остаток  = 3
# print(7 % 10) #если первая часть меньше второй, будет ответ первая часть
# print(2 % 10) #если первая часть меньше второй, будет ответ первая часть
# print(abs(-7 * 2)) # убирает минсу
# print(min(2, 8, 58, 1)) # мин значение
# print(max(2, 8, 58, 1)) # мах значение
# print(pow(2, 3)) # возводит 1ое значение во 2ое
# print(round(2.6)) # округяет
# print(round(2.6587, 3)) # округяет по 3 цифру после запятой

# a = int(input())
# b = int(a / 3)
# c = b * 2
# k = int((a - c)/2)
# s = int(k)
# print(k,c,s)

# print('Гвидо', 'Ван', 'Россум', sep='*', end='-')
# print('Основатель', 'Питона', sep='_', end='!')

# a = list(input())

# for i in range(len(a)):
# print(i, a[i])

# print(a, len(a))

# a = list((map(int, input().split())))

# print(sum((a[-3:])))

# n = int(input())
# k = n // 100
# l = n % 100 // 20
# m = n % 100 % 20 // 10
# x = n % 100 % 20 % 10 // 5
# y = n % 100 % 20 % 10 % 5 // 1
# print(k + l + m + x + y)

# input
# a, b, c = map(int, input().split())
# print(sum ((a, b, c), 0))

# s = int(input())
# a = s //6
# print(a, a * 4, a)

# a, b, c = map(int, input().split())
# su = (a * 3) + (b * 5) + (c * 12)
# print(su)

# n, a, b = map(int, input().split())
# print(a*b*n*2)

# g,l = map(int, input().split())
# ng = l-1
# nl = g-1
# print(ng, nl)

# h = int(input())
# m = int(input())
# s = int(input())
# h2 = int(input())
# m2 = int(input())
# s2 = int(input())
#
# print((h2 * 3600 + m2 * 60 + s2) - (h * 3600 + m * 60 + s))

# n = int(input())
# h = n // 3600 % 24
# m = n // 60 % 60
# s = n % 60
# print(f'{h}:{m//10}{m%10}:{s//10}{s%10}')

# n = int(input())
# k = 0
# for i in [100, 20, 10, 5]:
#     k = k + n // i
#
#     n = n % i
#
#
# print(k + n)

# n = int(input())
# print(n - n % 2 + 2)

# n = int(input())
# print(n > 0)

# n = int(input())
# print(n % 10 == 2)

# n, m = map(int,input().split())
# print(n % 7 == 0 and m % 7 == 0)

# a, b, c = map(int,input().split())
# print(a == b == c)

# n = int(input())
# print( 5 < n <= 19)

# a = str(input())
# b = str(input())
# print(a == 'awesome' or b == 'awesome')

# a, b, c = map(int,input().split())
# print(a == c  or b == a  or c == b)

# n = int(input())
# print(10 <= n < 100)

# y = float(input())
# print(y)
# print(int(y))
# print(str(y))
# n = isinstance(y, float)
# print(n)

# Округление вверх и округление вниз trunc, floor, ceil!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# import math
#
# print(math.trunc(82.55))
# или
# print(int(82.55))
#
# print(math.floor(32.8)) #округление вниз
# print(math.floor(-32.8)) #округление вниз -33, т.к. меньше
# print(math.ceil(32.8)) #округление вверх 33
# print(math.ceil(-32.2)) #округление вверх -32, т.к. больше

# import math
#
# a = int(input())
# b = int(input())
# c = int(input())
# print(int(((a % 2 + a) + (b % 2 + b) + (c % 2 + c))/2))
#
# или
#
# a = int(input())
# b = int(input())
# c = int(input())
# print(math.ceil(a/2) + math.ceil(b/2) + math.ceil(c/2))


# import math
#
# n = int(input())
# n = n / 10
# print(math.ceil(n))

# import math
# #
# # l, w, h = map(int,input().split())
# # n = (((l * 2) + (w * 2)) * h) / 16
# # print(math.ceil(n))

# СТРОКИ ОПРАЦИИ НАД НИМИ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# a = '«Лев Николаевич Толстой написал "Война и мир"»'
# print(a.replace('«', '').replace('»', ''))
# print(len(a))

# a = '«Лев Николаевич Толстой написал "Война и мир"»'
# print(a[1:-1])

# a = '«Лев Николаевич Толстой написал "Война и мир"»'
# print(a.lstrip('«').rstrip('»'))

# СТРОКИ И СТРЕЗЫ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# a = 'Hello hi'
# print(a[-1])
# print(a[1:-2])
# print(a[:-1:2])
# print(a[::-1])
# print(a[::-2])

# a = input()
# print(a[-1] + a[:-1])

# МЕТОДЫ СТРОК!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# a = 'Fuck you'
# a = a.lower()
# b = a.upper()
# c = a.count('u', 1, 8) # поиск символа, начинаем с и заканичаем по индкес
# v = a.index('u') #ищет индекс на котором находится смвол, если нет, то ошибка и выкидывает
# g = a.replace('u', 'uuu') # заменяет символ на любой другой включая и пробел
# print(a)
# print(b)
# print(c)
# print(a.find('k')) # исчет позицию на которой находиться символ, если нет, то указывает -1 и не выкидывает
# print(a.rfind('k')) # исчет позицию на которой находиться символ начиная справа
# print(v)
# print(g)
# print(a.isalpha())# если есть пробел или символы, то Fals)
# print('1235879'.isdigit())# если есть цифры
#
# e = '111'
# print(e.rjust(8, '0'))
# print(e.ljust(8, '/'))
#
# f = 'Buy a car'
# print(f.split('a'))# делает список по пробелу, в () можно указать по чем разбивать текст
# print('-'.join(f))
# n = '    join me \n'
# print(n.strip())# удаляет пробелы и переносы lstrip(удаляет слева знаки), rstrip(справа)

# a = input().upper().replace('A', '').replace('O', '').replace('Y', '').replace('E', '').replace('U', '').replace('I', '').lower().replace('', '.')
# print(a.rstrip('.'))

# print('/\_/\ \n>^,^< \n / \  \n(|_|)_/')
# print('  /~~~\   \n //^ ^\\\  \n(/(_*_)\) \n')

# print('Здравствуйте,{surname} {name}'.format(name = input(), surname = input()))
# name = input()
# age = int(input())
# print(f'{name}, вам исполнится 77 лет в {age + 77}')

# sex = {'m': 'Mister', 'f': 'Miss'}
#
# a = [
#     ['Vector', 'Semionov', 26, 'm'],
#     ['Bold', 'Ass', 36, 'm'],
#     ['Helen', 'Brook', 21, 'f'],
# ]
#
# for name, sername, age, gender in a:
#     print(f'Dear {sex[gender]} {name} {sername} your balance is {age}')

# print(f'Hello {input().upper()}. You are {int(input())} years old.')
# a = int(input())
# b = int(input())
# print(f'{a} / {b} = {a/b}',
#       f'{a} // {b} = {a//b}',
#       f'{a} % {b} = {a%b}', sep='\n')

# Списки!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# my_list = list(map(int, input().split()))
# print(777 in my_list)

# t_july = [30, 50, 60, 10, 15]
#
# for i in range(len(t_july)):
#     print(t_july[i], i + 1)

# a = input().split()
# print('777' in a)

# top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
# top[-1] = 'Сверхъестественное'
# top[2] = 'Настоящий детектив'
# print(top)

# a = list(map(int, input().split()))
# print(sum(a) / len(a))

# a = list(map(int, input().split()))
# print(a[1])

# Списки и их методы!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# a = [2, 50, 10, 15]
# a.append('hello')
# print(a)
# a.clear() # список пуст
# print(a)
# a = [2, 50, 10, 15]
# b = a.copy()
# print(b)
# print(b.count(2))
# b.append(2)
# print(b.count(2))
# print(b.index(10, 1, 3)) # ищет индекс 10 в интервале от 1 до 3и только первый найденный
# b.insert(2, 1000)# вставляем в список индекс, через запятую значение, остальное все смещается вправо
# print(b)
# с = b.pop(1) # удаляет с конца списка значение и показвает его или можно в скобках указать индекс удаляемого значения
# print(с, b)
# b.remove(1000) #удаляет из списка по значению
# print(b)
# b.reverse()
# print(b)
# b.sort() # если нужно перевернуть список, revers = True
# print(b)

# a = list(map(int, input().split()))
# print(a.count(999))

# mas = ['45.5', 'True', 'Привет', '11', '8']
# mas.reverse()
# print(*mas) # * распаковывает список и приводит к строке: 8 11 Привет True 45.5

# a = input().upper().split()
# b = a.copy()
# a = '-'.join(a[0])
# b = '-'.join(b[1])
# print(a, b)

# a = input().split()
# print('\n'.join(a))

# a = input().split()
# print(f'{a[2]} {a[0][0]}.{a[1][0]}.')

# a = input().split()
# n = a.pop(-1)
# c = a.pop(0)[0] + '.'
# d = a.pop(0)[0] + '.'
# print(n, c, d)

# Цыклы!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# a = input().lower()
# b = input().lower()
#
# if a == b[::-1]:
#     print('YES')
# else:
#     print('NO')

# a = list(map(int, input().rjust(6, '0')))
#
# if sum(a[:3]) == sum(a[-3:]):
#     print("YES")
# else:
#     print('No')

# a = int(input())
#
# if a % 2 == 0:
#     print(int(a/2))
# else:
#     print(int((a + 1)/-2))


# a = int(input())
# b = int(input())
# c = a
# if b > a:
#     c = b
# print(c)

# a = input()
# b = a[::-1]
#
# if int(a) == int(b):
#     print('YES')
# else:
#     print('NO')

# a, b, c = map(int, input().split())
#
# if a + b == c:
#     print('YES')
# else:
#     print('NO')

# a = input()
# a = a.rjust(6, '0')
# a = list(map(int, a))
# if sum(a[:3]) == sum(a[-3:]):
#     print('YES')
# else:
#     print('No')


# a = sum(map(ord, input()))
# b = sum(map(ord, input()))
# if (a + b)%2 ==0:
#     print('YES')
# else:
#     print('NO')

# a = input()
# b = input()
# if (ord(a[0]) + int(a[1]) + ord(b[0]) + int(b[1])) % 2 == 0:
#     print('YES')
# else:
#     print('NO')

# s = map(ord, input().upper())
# print(list(s))
# if sum(s) % 2 == 0:
#     print('Целое')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
# if a > b:
#     print('>')
# if a < b:
#     print('<')
# else:
#     print('=')

# a = int(input())
#
# if a % 2 == 0:
#     print(int(a / 2))
# else:
#     print(a)


# a, b, c = map(int, input().split())
#
# if b < a > c:
#     if b > c:
#         print(a - c)
#     else:
#         print(a - b)
#
# if a < b > c:
#     if a > c:
#         print(b - c)
#     else:
#         print(b - a)
#
# if a < c > b:
#     if a > b:
#         print(c - b)
#     else:
#         print(c - a)
# if a == c == b:
#     print('0')

# a = int(input())
#
# if a % 3 ==0 and a % 5 == 0:
#     print('FizzBuzz')
# elif a % 3 == 0:
#     print('Fizz')
# elif a % 5 == 0:
#     print('Buzz')
# else:
#     print(a)

# N = int(input())
#
# if N == 1:
#     print('0')
# else:
#     if N % 2 == 0:
#         print(N // 2)
#     else:
#         print(N)

# a, b, c = map(int, input().split())
# z = []
# k = []
# if c < a > b:
#     z.append(a)
# else:
#     if a < b > c:
#         z.append(b)
#     else:
#         z.append(c)
# if c > a < b:
#     k.append(a)
# else:
#     if a > b < c:
#         k.append(b)
#     else:
#         k.append(c)
# d = z + k
# print(d[0] - d[1])

# a, b, c = map(int, input().split()) # 100 500 1000
# if a < b:
#     a, b = b, a # 100 500 = 100 500
#     print(b, a)
# if b < c: #100 < 1000
#     b, c = c, b # 100 1000 = 100 1000
#     print(c, b)
# if a < b: # 500 < 1000
#     a, b = b, a # 500 1000 = 500 1000
#     print(b, a)
# print(a - c)

# a = map(ord, input().lower())
# b = map(ord, input().lower())
# print(list(a), list(b))
#
# if sum(a) > sum(b):
#     print('-1')
# else:
#     if sum(a) < sum(b):
#         print('1')
#     else:
#         print('0')

# city = input().lower()
# town = input().lower()
#
# if city[-1] == 'ь' and city[-2] == town[0] or city[-1] == town[0]:
#     print('Good')
# else:
#     print('Bad')

# a = int(input())
# b = int(input())
# c = int(input())
#
# if a == b == c:
#     print('3')
# elif a == b or b == c or a == c:
#     print('2')
# else:
#     print('0')

# mounce = [0, 'januery', 'fabryri', 'mart', 'april', 'may', 'july']
# print(mounce[int(input())])

# a = int(input())
#
# if 0 < a < 2 :
#     print('Младенец')
# elif 2 < a < 4:
#     print('Малыш')
# else:
#     print('Кандибобр')

# a = float(input())
# b = float(input())
# c = input()
# if c == '+' or '-' or '/' or '*':
#     if c == '+':
#         print(int(a + b))
#     elif  c == '-':
#         print(int(a - b))
#     elif  c == '/' and b == 0:
#         print('Неизвестно')
#     elif c == '/':
#             print(a / b)
#     elif  c == '*':
#         print(int(a * b))
#     else:
#         print('Неизвестно')

# a, b = input(), input()
#
# if len(a) < 7:
#     print('Short')
# elif a != b:
#     print('Difference')
# else:
#     print('OK')

# ps = input()
# print('Short' if len(ps) < 7 else 'Difference' if ps != input() else 'OK')

# print((lambda p1=input(), p2=input(): int(p1) + int(p2))())

# i = int(input())
# while i <= 10:
#     if i%2 == 0:
#         print(i)
#     i += 1
# a = input()
# password = 'qwerty'
# count = 0
# while a != password:
#     count += 1
#     print('введите пароль')
#     a = input()
# print('You lose all variety', count, 'times')

# a = [1, 2, 3, 4, 5] * 3
# c = []
# while 3 in a:
#     a.remove(3)
#     c.append(3)
#     print(a)
# print(c)

# a = input()
# while len(a) > 0:
#     letter = a[0]
#     if letter >= 'a' and letter <= 'z':
#         print(letter, 'min letter')
#     elif letter >= 'A' and letter <= 'Z':
#         print(letter, 'Big letter')
#     elif letter.isdigit():
#         print(letter, 'Fasilici')
#     else:
#         print(letter, 'Other')
#     a = a[1:]

# a, b = map(int, input().split())
# count = 0
# while a <= b:
#     a *= 3
#     b *= 2
#     count += 1
# print(count)

# a = list(input())
# print("".join(a))
# while len(a) > 1:
#     a.pop() and a.pop(0)
#     print("".join(a))

# a = input()
# while len(a) > 0:
#     print(a)
#     a = a[1:]

# N = int(input())
# i = 1
# while N > i**2:
#     print(i**2)
#     i = i + 1


# def multiply(a, b):
#     return a * b
# multiply(1, 2)

# def array_diff(a, b):
#
#     for i in range(len(b)):
#         print(b, b[i])
#         while b[i] in a:
#             a.remove(b[i])
#     print(a)
# array_diff([1, 2, 3, 4, 4, 4], [4])

# def array_diff(a, b):
#     c = []
#
#     for i in a:
#         if i not in b:
#             c.append(i)
#     print(c)
#
# array_diff([1, 2, 3, 4, 4, 4], [4])

# def array_diff(a, b):
#
#     for i in b:
#         while i in a:
#             a.remove(i)
#     print(a)
# array_diff([1, 2, 3, 4, 4, 4], [4])

# s = "5a 3 k 99 d00"
# s = s.split()
# s= ''.join(s).replace('', ' ').replace('"', '').split(' ')
# s.pop(0)
# s.pop(-1)
# print(list(filter(str.isdigit, s)))

# for i in s:
#     if i.isdigit():
#         print(i)
#     print(list(i))


# X, Y = map(int, input().split())
# day = 1
#
# while X < Y:
#     X *= 1.15
#     day += 1
# print(day)


# n, m = map(int, input().split())
# print(n, m)
# days = 0
# while n > 0:
#     days += 1
#     n -= 1
#     if days % m == 0:
#         n += 1
# print(days)

# a = input()
# while int(a[0])!= 1 and len(a) < 10:
#     a = str(int(a[0]) * int(a))
# print(a)

# a = int(input())
# s = 0
# while a % 2 == 0:
#     a /= 2
#     s += 1
# if a == 1:
#     print(s)
# else:
#     print('НЕТ')


# n = int(input())
# sn = sorted(list(map(int, input().split())))
# m = int(input())
# sm = sorted(list(map(int, input().split())))
# couple = 0
#
# while len(sn) > 0 and len(sm) > 0:
#     if 0 <= abs(sn[0] - sm[0]) <= 1:
#         couple += 1
#         sn.pop(0)
#         sm.pop(0)
#     elif sn[0] < sm[0]:
#         sn.pop(0)
#     else:
#         sm.pop(0)
# print(couple)

# a = input()
# while len(a) > 0:
#     print(a[0])
#     a = a[1:]

# n = int(input())
#
# k = 1
# r = 1
# count = 0
#
# while n > 0:
#     k = k + 1
#     r = r + k
#     n = n - r
#     count += 1
# print(count)


# n, m = map(int, input().split())
# count = 0
# a = 0
# while a**2 <= n:
#     b = n - a**2
#     if b >= 0 and a + b**2 == m:
#         count += 1
#     a += 1
# print(count)

# a = int(input())
#
# while a > 0:
#     print(a%10)
#     a = a // 10

# a, b = map(int, input().split())
#
# count = 0
#
# while a > 0:
#     a -= 1
#     count += 1
#     if count % b == 0:
#         a += 1
# print(count)


# a, b = map(int, input().split())
#
# z = 0
# time = 0
# countz = 0
#
# while a > 0:
#     countz += 1
#     z = countz * 5
#     a -= 1
#     time += z
# if time + b <= 240:
#     print(countz)
# else:
#     print(countz - 1)


# n, m = map(int, input().split())
# a = sorted(list(map(int, input().split())))
# b = sorted(list(map(int, input().split())))
#
# if n == len(a) and m == len(b):
#     z = a + b
#     print(*sorted(z))
# else:
#     print('Не правильная длина списка')

# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
#
# if n == len(a) and m == len(b):
#     z = a + b
#     i = 0
#     while i < len(z):
#         j = 0
#         while j < len(z) - 1:
#             if z[j + 1] < z[j]:
#                 z[j], z[j + 1] = z[j + 1], z[j]
#             j += 1
#         i += 1
#     print(z)

# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
#
# k = a + b
# z = []
# while k:
#     z.append(min(k))
#     k.remove(min(k))
# print(z)

# n = int(input())
# a = input()
# while '10' in a or '01' in a:
#     a = a.replace('10', '')
#     a = a.replace('01', '')
# print(len(a))


# n, a = input(), input()
# print(abs(a.count('1')-a.count('0')))

# a = int(input())
# n = 0
# while a > 0:
#     n = n  + a % 10
#     a = a // 10
# print(n)

# print(sum(map(int, list(input()))))

# a = map(int, list(input()))
# print(sum(a))


# a = int(input())
# n = 1
# while a > 0:
#     n = n * (a % 10)
#     a = a // 10
# print(n)

# a = int(input())
# count = 0
# n = 0
# while a > 0:
#         count = a % 10
#         if count ==7:
#             n += 1
#         a = a // 10
# print(n)

# a = input()
# print(a.count('7'))

# year = int(input())
# pr = float(input())
# s = int(input())
# st = s
#
# while year > 0:
#     s = s * pr
#     year -= 1
#     print(s)
#
# print(st/s)

# a = int(input())
# b = int(input())
#
# while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a
# print(a)

# a, b = map(int, input().split())
# n = a
# z = b
#
# while b > 0:
#
#     # c = a % b
#     # a = b
#     # b = c
#     a, b = b, a%b
#
# print(int(n*z/a))

# n = int(input())
# i = 1
#
# while n // 2 >= i:
#     if n % i == 0:
#         print(i)
#     i += 1
# print(n)

# n = int(input())
# i = 1
# a = []
# while i*i <= n:
#     if n % i == 0:
#         a.append(i)
#         if i != n//i:
#             a.append(n//i)
#     i += 1
# a.sort()
# if len(a) == 2:
#     print('YES')
# else:
#     print('NO')

# a=int(input())
# i=2
# while a%i!=0 and i<a:
#     i+=1
# print('Yes' if i==a else 'No')

# n = int(input())
# i = 1
# a = []
# while i*i <= n:
#     if n % i == 0:
#         a.append(i)
#         if i != n//i:
#             a.append(n//i)
#     i += 1
# a.sort()
# print(sum(a))

# a = [52, 16, 55, 603, 73, 81]
#
# while len(a) > 0:
#     last = a.pop()
#     if last % 2 == 0:
#         print('Yes', last)
#         break
# else:
#     print('No')


# n = int(input())
#
# count = 0
#
# while n >=1:
#     if n % 2 == 0:
#         n = n/2
#         count += 1
#
#     elif n % 2 != 2 and n != 1:
#         n = n*3 + 1
#         count += 1
#     else:
#         if n == 1:
#             break
# print(count)

# print(list(range(5)))
# print(list(range(0, 11, 2)))
# print(list(range(10, -1, -2)))
# print(sum(range(5)))
# print(len(range(5)))
# a, b, c = range(1, 4)
# print(a, b, c)
# n = range(1, 7)
# print(n[2])
# v = iter(range(5))
# print(next(v))
# print(next(v))
# print(next(v))
# print(next(v))

# s = iter([45, 'Hello', 58, True, 2])
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))

# for i in range(10, 99):
#     if i % 10 == 0:
#         print(i)

# s = 0 # суммирует четные чисела
# for i in range(10, 99):
#     if i % 2 == 0:
#         s = s + i
#         print(i, s)

# pr = 1 # факториал чисел
# for i in range(1, 5): # факториал 4!
#     pr = pr * i
#     print(i, pr)

# n = int(input())
# pr = 1 # факториал чисел
# for i in range(1, n + 1): # факториал 4!
#     pr = pr * i
#     print(i, pr)

# from random import randint # a выводи рандомно числа n и s суммирует рандомные числа
#
# n = int(input())
# s = 0
# for i in range(1, n):
#     a = randint(1, 50)
#     s = a + s
#     print(i, a)
# print(s)

# N = int(input())
# for i in range(1, N + 1):
#     print(i)

# N = int(input())
# for i in range(N, 0, -1):
#     print(i)

# a = input()
# n = int(input())
# for i in range(n):
#     print(a)

# a = int(input())
# b = int(input())
#
# for i in range(a, b + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# a = int(input())
# b = int(input())
#
# for i in range(a, b + 1):
#     print(f'Число {i}; его квадрат = {i**2}; его куб = {i**3}')

# n = int(input())
# M = 0
# K = 0
# for i in range(n):
#     m, k = map(int, input().split())
#     if 1 <= m <= 6 and 1 <= k <= 6:
#         if m > k:
#             M += 1
#         elif m < k:
#             K += 1
# if M > K:
#     print('Mishka')
# elif M < K:
#     print('Chris')
# else:
#     print('Friendship is magic!^^')


# N = int(input())
# for i in range(N):
#     a = input().lower()
#     if 'рок' in a:
#         print(i + 1, a.find('рок') + 1)


# N = int(input())
# l = []
# k = []
# for i in range(N):
#     a = input().lower()
#     l.append(a)
# l = ' '.join(l).split()
# for j in l:
#     if 'соль' not in j:
#         k.append(j)
# print(*k)


# a = int(input())
# s = []
# for i in range(1, a):
#     if i % 5 == 0 or i % 3 == 0:
#         s.append(i)
# print(sum(s))
# s = 0
# for i in range(50, 101):
#     s = s + i**3
#     print(s)

# a = int(input())
#
# for i in range(a):
#     n = input()
#     if len(n) > 10:
#         print(f'{n[0]}{len(n[1:-1])}{n[-1]}')
#     else:
#         print(n)

# a = [25, 78, 5, 56, 10]
#
# for i in range(len(a)):
#     print(i, a[i])
#     a[i] += 5
# print(a)

# a = [25, 78, 5, 56, 10, 10, 25, 6]
# b = []
# for i in a:
#     print(i)
#     if i not in b:
#         b.append(i)
# print(b)

# a = [25, 78, 5, 56, 10, 10, 25, 6]
# chet = []
# nechet = []
#
# for i in a:
#     if i % 2 == 0:
#         chet.append(i)
#     else:
#         nechet.append(i)
# print(chet)
# print(nechet)

# a = [25, 78, 5, 56, 10, 10, 25, 6]
# chet = []
# nechet = []
#
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         chet.append(i+1)
#         chet.append(a[i])
#     else:
#         nechet.append(i+1)
#         nechet.append(a[i])
# print(chet)
# print(nechet)

# a = 'Hell World'
#
# for i in a:
#     if 'a' <= i <= 'z':
#         print(i, 'Smoll')
#     elif 'A' <= i <= 'Z':
#         print(i, 'Big')
#     else:
#         print(i)

# wovels = 'aeiou'
# a = 'kjfajrgohgagaqazfngpoiuyvbaiio'
# for i in range(len(a) - 1):
#     if a[i] in wovels and a[i + 1] in wovels:
#         print(a[i], a[i + 1])

# n = int(input())
# z = []
# for i in range(n):
#     a = input()
#     z.append(a)
# print(z)

# n = int(input())
# a = [input() for i in range(n)]
# print(a)

# print([input() for i in range(int(input()))])

# w = input()
# s = input().split()
#
# for i in s:
#     if w in i:
#         print(i)

# letter = input()
# print(*[i for i in input().split() if letter in i], sep='\n')

# def dig_pow(n, p):
#
#     n = str(n)
#     z = []
#     g = []
#     for i in range(len(n)):
#         z.append(int(n[i]))
#     for i in range(len(z)):
#         z[i] = z[i]**p
#         p += 1
#         g.append(z[i])
#     k = int(sum(g) / int(n))
#     if int(sum(g) % int(n)) == 0:
#         print(k)
#     else:
#         print('-1')
#         # return k
#
# dig_pow(89, 1)

# def dig_pow(n, p):
#     sum = 0
#     for i in str(n):
#         sum = sum + int(i)**p
#         p += 1
#     if sum % n == 0:
#         print(int(sum/n))
#     else:
#         print('-1')
#
# dig_pow(92, 1)

# def dig_pow(n, p):
#
#     n = str(n)
#     g = []
#     for i in range(len(n)):
#         g.append(int(n[i])**p)
#         p += 1
#     k = int(sum(g) / int(n))
#     if int(sum(g) % int(n)) == 0:
#         return k
#     else:
#         return k
#
# dig_pow(92, 1)

# a = list(map(int, input().split()))
#
# n = []
# z = []
# for i in range(len(a)):
#     if a[i] > 0:
#         n.append(a[i])
#     elif a[i] < 0:
#         z.append(a[i])
# if len(n) != 0:
#     print(min(n))
# elif len(n) == 0:
#     print('Empty')

# a = list(map(int, input().split()))
#
# n = []
# for i in a:
#     if i > 0:
#         n.append(i)
# if n:
#     print(min(n))
# else:
#     print('Empty')


# a = input().lower()
# b = []
#
# for i in a:
#     b.append(a.count(i))
# print(max(b))

# a = int(input())
# sp = []
# chet = []
# nechet = []
# for i in str(a):
#     sp.append(int(i))
#
# for i in range(len(sp)):
#     if (i + 1) % 2 == 0:
#         chet.append(sp[i])
#     else:
#         nechet.append(sp[i])
# if (sum(chet) - sum(nechet)) % 11 == 0:
#     print('YES')
# else:
#     print('NO')
#
# print(sum(chet))
# print(sum(nechet))


# a = input()
# b = []
# for i in a:
#     if i.isdigit():
#         b.append(int(i))
# print(len(b), sum(b))

# b = []
# for i in input():
#     if i.isdigit():
#         b.append(int(i))
# print(len(b), sum(b))

# import re
# digit_list = re.findall(r'\d', input())
# print(len(digit_list), sum([int(i) for i in digit_list]))


# a = input()
#
# stek = []
# is_good = True
# for i in a:
#     if i in '([{':
#         stek.append(i)
#     elif i in ')]}':
#         if not stek:
#             is_good = False
#             break
#         deliter = stek.pop()
#         if deliter == '{' and i == '}':
#             continue
#         if deliter == '[' and i == ']':
#             continue
#         if deliter == '(' and i == ')':
#             continue
#         is_good = False
#         break
# if is_good and len(stek)==0:
#     print('YES')
# else:
#     print('NO')

# a = input()
#
# for i in range(len(a)):
#     a = a.replace('{}', '')
#     a = a.replace('[]', '')
#     a = a.replace('()', '')
# if len(a) == 0:
#     print('Yes')
# else:
#     print('No')

# a = [0, 2, 2, 5, 6, 4, 5, 3, 1]
# st = [0] * 7
#
# for i in a:
#    st[i] += 1
# print(st)


# a = map(int, input())
# b = [0] * 7
# for i in a:
#     b[i] += 1
# for i in range(len(b)):
#     if b[i] > 0:
#         print(i, b[i])
# print((str(i) + ' ') * b[i], end='')

# n = input()
#
# for i in range(10):
#     if str(i) in n:
#         print(i, n.count(str(i)))


# n = input()
#
# while len(n)>0:
#     print(n[0])
#     n = n[1:]

# a = int(input())
# c = []
# while a:
#     c.append(a%10)
#     a = a // 10
# print(c[::-1])

# a = list(map(int, input()))
# while len(a)<6:
#     a.append(0)
# if sum(a[:3]) == sum(a[-3:]):
#     print('OK')
# else:
#     print('NO')

# n=int(input())
# s=list(map(int,input().split()))
# a=[]
# while len(s)!=0:
#     a.append(min(s))
#     s.remove(min(s))
# for i in a:
#     print(i,end=" ")


# n = int(input())
# s = list(map(int, input().split()))
# a = []
# print(s)
# for i in s:
#     a.append(max(s))
#     s.remove(max(s))
#     if len(s) == 1:
#         a.append(*s)
# print(*a)

# n = int(input())
# s = list(map(int, input().split()))
# a = [0] * 201
#
# for i in s:
#     a[i + 100] += 1
# for i in range(len(a)):
#     if a[i] > 0:
#         print((str(i - 100) + ' ' * a[i]), end='')


# for i in range(3):
#     for j in range(5):
#         print('+', end='')
#     print()

# # 00000
# # 11111
# # 22222
# for i in range(3):
#     for j in range(5):
#         print(i, end='')
#     print()

# #
# # 1
# # 22
# for i in range(3):
#     for j in range(i):
#         print(i, end='')
#     print()


# # 01234
# # 01234
# # 01234
# for i in range(3):
#     for j in range(5):
#         print(j, end='')
#     print()

# # 1 10 10
# # 1 11 11
# # 1 12 12
# # 2 10 20
# # 2 11 22
# # 2 12 24
# # 3 10 30
# # 3 11 33
# # 3 12 36
# for i in range(1, 4):
#     for j in range(10, 13):
#         print(i, j, (i * j))

# # a c
# # a b
# # a n
# # b c
# # b b
# # b n
# for i in 'ab':
#     for j in 'cbn':
#         print(i, j)

# # подбор пароля тз трех символов
# from string import printable
#
# for w1 in printable:
#     for w2 in printable:
#         for w3 in printable:
#             print(w1, w2, w3)

# for j in range(1, 11):
#     for i in range(1, 10):
#         print(i, '*', j, '=', i*j, end=' ')
#     print()
# k = 0
# for w1 in 'tukva':
#     for w2 in 'tukva':
#         for w3 in 'tukva':
#             for w4 in 'tukva':
#                 for w5 in 'tukva':
#                     cont = w1 + w2 + w3 + w4 + w5
#                     if cont[0] in 'tkv' and cont[-1] in 'tkv':
#                         if cont.count('a') + cont.count('u') == 2:
#                             k +=1
#                         print(cont)
# print(k)

# n = []
# for i in range(1000, 10000):
#     x = i
#     s = 0
#     while x > 0:
#         s = s + x % 10
#         x = x // 10
#     if s % 20 == 0:
#         n.append(i)
# print(sum(n))

# sum = 0
# for i in range(1000, 10000):
#     n = str(i)
#     if (int(n[0]) + int(n[1]) + int(n[2]) + int(n[3])) == 20:
#         sum = sum + i
# print(sum)

# n = int(input())
#
# for i in range(1, n + 2):
#     for j in range(1, i):
#         print(j, ' ', end='')
#     print()


# n = int(input())
# count = 0
#
# for i in range(n + 1, n*2):
#     if i % 2 == 0 and  i != 2 or i == 1:
#         continue # пропустить числа деленые на два, двойку и единицу
#     d = 3
#     is_plain =True
#     while d*d <= i:
#         if i % d == 0:
#             is_plain =False
#             break
#         d += 2
#     if is_plain:
#         count +=1
# print(count)

# n = int(input())
# a=0
# for i in range(n+1,n*2):
#     k = int(i**0.5)
#     for j in range(2, k + 1):
#         print(i, j)
#         if i%j==0:
#             break
#     else:
#         a+=1
# print(a)


# n = int(input())
# p = []
#
# for i in range(n, n + 1):
#     for j in range(1, n + 1):
#         a = i/j
#         if a % 1 == 0:
#             p.append(int(a))
#
# if len(p) == 2:
#     print('Yes')
# else:
#     print('No')
# print(p)

# n = int(input())
# i = 1
# p = []
# while i * i <= n:
#     if n % i == 0:
#         p.append(i)
#         if i != n//i:
#             p.append(n//i)
#     i += 1
# print(p)


# n = list(map(int, input().split()))
#
# for i in n:
#     for j in '*':
#         print(i * j)

# for i in range(1000, 1005):
#     for j in range(i):
#         print(i, j)

# a = int(input())
# n = list(map(int, input().split()))
# b = [0] * (max(n) + 1)

# for i in n:
#     b[i] += 1
# for i in range(len(b)):
#     if b[i] != 0:
#         print(i, end=' ')


# a = int(input())
# n = list(map(int, input().split()))
# print(n)
# count = 0
# for i in range(len(n)):
#     for j in range(0, len(n) - 1):
#         print(n[j], n[j + 1])
#         if n[j] > n[j + 1]:
#             n[j], n[j + 1] = n[j + 1], n[j]
#             count += 1
#
# print(*n)
# print(count)


# n = int(input())
# a = list(map(int, input().split()))
# b = [0] * (max(a) + 1)
# for i in a:
#     b[i] += 1
# for i in range(len(b)):
#     if b[i] != 0:
#         print((str(i) + ' ') * b[i], end='')

# n = int(input())
# a = list(map(int, input().split()))
#
# for i in range(len(a)):
#     for j in range(0, len(a) - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
# print(a)


# n = int(input())
# sp = list(map(int, input().split()))
# for i in range(len(sp)):
#     while i != 0 and sp[i] < sp[i - 1]:
#         sp[i], sp[i - 1] = sp[i - 1], sp[i]
#         i -= 1
# print(*sp)

# a = int(input())
# c = list(map(int, input().split()))
#
# for i in range(len(c)):
#     for j in range(len(c)):
#         if j != 0 and c[j] < c[j - 1]:
#             c[j], c[j - 1] = c[j - 1], c[j]
# print(*c)


# # БЫСТРАЯ СОРТИРОВКА
# import random
#
# A = list(map(int, input().split()))
# m = random.choice(A) # случайное число из списка
# print(m)
# if len(A) <= 1:
#     print(A)
# else:
#     q = random.choice(A)
#     print(f'q = {q}')
#     L = []
#     M = []
#     R = []
#     for elem in A:
#         if elem < q:
#             L.append(elem)
#         elif elem > q:
#             R.append(elem)
#         else:
#             M.append(elem)
#     print(sorted(L) + M + sorted(R))

# # ИНДЕКС ПО СТРОКАМ
# # 12 14 16 11
# # 15 25 21 18
# # 17 23 19 22
# # [[12, 14, 16, 11], [15, 25, 21, 18], [17, 23, 19, 22]]
# a = [[2, 4, 6, 1],
#      [5, 15, 11, 8],
#      [7, 13, 9, 12]
# ]
#
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         a[i][j] += 10
#         print(a[i][j], end=' ')
#     print()
# print(a)

# # ИНДЕКС ПО СТОЛБЦАМ
## 12 14 16 11
## 15 25 21 18
## 17 23 19 22
## [[12, 14, 16, 11], [15, 25, 21, 18], [17, 23, 19, 22]]
# a = [[2, 4, 6, 1],
#      [5, 15, 11, 8],
#      [7, 13, 9, 12]
# ]
#
# for j in range(len(a[0])):
#     for i in range(len(a)):
#         print(a[i][j], end=' ')
#     print()
# print(a)

# # ИНДЕКС ПО СТРОКАМ В ОБРАТНОМ ПОРЯДКЕ
# # 12 9 13 7
# # 8 11 15 5
# # 1 6 4 2
# # [[2, 4, 6, 1], [5, 15, 11, 8], [7, 13, 9, 12]]
# a = [[2, 4, 6, 1],
#      [5, 15, 11, 8],
#      [7, 13, 9, 12]
# ]
#
# for i in range(2, -1, -1):
#     for j in range(3, -1, -1):
#         print(a[i][j], end=' ')
#     print()
# print(a)

# a = [[2, 4, 6, 1],
#      [5, 15, 11, 8],
#      [7, 13, 9, 12]
# ]
# for i in range(3):
#     s = 0
#     for j in range(4):
#         s = s + a[i][j]
#     print(s) # сумма по строкам

# a = [[2, 4, 6, 1],
#      [5, 15, 11, 8],
#      [7, 13, 9, 12]
# ]
# for j in range(4):
#     s = 0
#     for i in range(3):
#         s = s + a[i][j]
#     print(s) # сумма по столбцам

# a = []
# n = int(input())
# c = int(input())
#
# for i in range(n):
#     a.append([0] * c)
# for i in a:
#     print(i)

# a = []
# n = int(input())
# c = int(input())
#
# for i in range(n):
#     b = []
#     for j in range(c):
#         b.append(int(input()))
#     a.append(b)
# for i in range(n):
#     s = 0
#     for j in range(c):
#         s = s + a[i][j]
#     print(s)

# a = []
# n = int(input())
#
# for i in range(n):
#     a.append([0] * n)
# for i in range(n):
#     for j in range(n):
#         if i > j:
#             a[i][j] = 3
#         elif i < j:
#             a[i][j] = 8
#         else:
#             a[i][j] = 10
# for i in a:
#     print(i)

# n = int(input())
# a = []
# for i in range(n):
#     a.append(list(map(int, input().split())))
# s = []
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             s.append(a[i][j])
# print(sum(s))

# a = []
# N = int(input())
#
#
# for i in range(N):
#     a.append(list(map(int, input().split())))
# for j in range(N):
#     for i in range(N):
#         print(a[i][j], end=' ')
#     print()

# a = []
# N = int(input())
#
#
# for i in range(N):
#     a.append(list(map(int, input().split())))
# for j in range(N - 1, -1, -1):
#     for i in range(N - 1, -1, -1):
#         print(a[i][j], end=' ')
#     print()

# a = []
# n, m = map(int, input().split())
#
# for i in range(n):
#         a.append(list(map(int, input().split())))
# # for i in a: # или так
# #         print(*i[::-1])
# # print(*a)
# for i in range(n):
#         for j in range(m - 1, -1, -1):
#                 print(a[i][j], end=' ')
#         print()

# a = []
# n, m = map(int, input().split())
#
# for i in range(n):
#         a.append(list(map(int, input().split())))
# for i in range(n - 1, - 1, -1):
#         for j in range(m):
#                 print(a[i][j], end=' ')
#         print()

# a = []
#
# for i in range(5):
#         a.append(list(map(int, input().split())))
# for i in range(5):
#         for j in range(5):
#                 if a[i][j] == 1:
#                         b = abs(2-i) + abs(2-j)
# print(b)

# a = []
# n, m = map(int, input().split())
#
# for i in range(n):
#     a.append(list(map(int, input().split())))
# for i in range(n):
#     s = 0
#     for j in range(m):
#         s = s + a[i][j]
#     print(s, end=' ')
# print()
# for j in range(m):
#     h = 0
#     for i in range(n):
#         h = h + a[i][j]
#     print(h, end=' ')


# a = []
# n, m = map(int, input().split())
#
# for i in range(n):
#     a.append(list(map(int, input().split())))
#
# for i in range(n):
#     print(sum(a[i]), end=' ')
#     # s = [] # или так
#     # for j in range(m):
#     #     s.append(a[i][j])
#     # print(sum(s), end=' ')
# print()
# for j in range(m):
#     k = []
#     for i in range(n):
#         k.append(a[i][j])
#     print(sum(k), end=' ')

# a = []
# n = int(input())
# for i in range(n):
#     a.append(list(map(int, input().split())))
# row_1 = []
# row_2 = []
# for i in range(n - 1):
#     m = []
#     for j in range(n):
#         if i < j:
#             m.append(a[i][j])
#     row_1.append(m[0:2])
# for j in range(n - 1):
#     c = []
#     for i in range(n):
#         if i > j:
#             c.append(a[i][j])
#     row_2.append(c[0:2])
# if row_1 == row_2:
#     print('Yes')
# else:
#     print('No')

# n = int(input())
# a = []
# t = True
# for i in range(n):
#     a.append(list(map(int, input().split())))
# for i in range(n):
#     for j in range(n):
#         if a[i][j] != a[j][i]:
#             t = False
#             break
# if t:
#     print('Yes')
# else:
#     print('No')

# a = []
# n, m = map(int, input().split())
# for i in range(n):
#     a.append(list(map(int, input().split())))
# k = []
# for i in range(n):
#     z = []
#     for j in range(m):
#         z.append(a[i][j])
#     k.append(sum(z))
# print(max(k), k.index(max(k)), sep='\n')


# n, m = map(int, input().split())
# a = []
# for m in range(n):
#     a.append(sum(list(map(int, input().split()))))
# print(max(a))
# print(a.index(max(a)))

# a = []
# n, m = map(int, input().split())
# for i in range(n):
#     a.append(list(map(int, input().split())))
# z = []
# for i in range(n):
#     k = []
#     for j in range(m):
#         k.append(a[i][j])
#     z.append(k)
# print(max(z))

# a = []
# n, m = map(int, input().split())
# for i in range(n):
#     a.append(list(map(int, input().split())))
# z = []
# for i in range(n):
#     for j in range(m):
#         z.append(a[i][j])
# l = []
# k = []
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == max(z):
#             l.append(i)
#             k.append(j)
# print(max(z))
# print(l[0], k[0])


# n, m = map(int, input().split())
# stroka, i_str, summa = 0, 0, 0
# for s in range(n):
#     a = list(map(int, input().split()))
#     for j in range(m):
#         if a[j] > i_str or (a[j] == i_str and summa < sum(a)):
#             stroka, i_str, summa = s, a[j], sum(a)
# print(stroka)


# a = []
# b = []
# n, m = map(int, input().split())
# for i in range(n):
#   a.append(list(map(int, input().split())))
# for i in range(n):
#   b.append([max(a[i]), sum(a[i])])
# print(a)
# print(b)
# print(b.index(max(b)))


# a = []
# b = []
# n, m = map(int, input().split())
# for i in range(n):
#     a.append(list(map(int, input().split())))
# for i in range(n):
#     b.append(max(a[i]))
# print(b.count(max(b)))

# a = []
# count = 0
# # q = 'Yes'
# for i in range(4):
#     a.append(list(map(str, input())))
# for i in range(3):
#     for j in range(3):
#         if a[i][j] == a[i][j + 1] == a[i + 1][j] == a[i + 1][j + 1]:
#             # q = 'No'
#             count += 1
# if count == 0:
#     print('Yes')
# else:
#     print('No')
# # print(q)


# n, m = map(int, input().split())
# a = []
# b = []
# count = 0
# for i in range(n):
#     a.append((list(map(str, input()))))
# input()
# for i in range(n):
#     b.append((list(map(str, input()))))
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == b[i][j]:
#             count += 1
# print(count)

# n, x = map(int, input().split())
# count = 0
# for i in range(1, n + 1):
#     for j in range(1, n + 2):
#         if i * j == x:
#             count += 1
# print(count)

# n = int(input())
# a = []
# g = []
# s = []
# count = 0
# count_1 = 0
# for i in range(n):
#     a.append(list(map(int, input().split(' '))))
#
# for i in range(n):
#     g.append(a[i][0])
# for i in range(n):
#     s.append(a[i][1])
#
# for i in range(n):
#     if g[i] in s:
#         count += 1
# if count == n:
#     count_1 += 1
# print(count + count_1)

# n = int(input())
# a = [list(map(int, input().split())) for i in range(n)]
# count = 0
# for i in range(n):
#     for j in range(n):
#         print(a[i][0], a[j][1])
#         if a[i][0] == a[j][1]:
#             count += 1
# print(count)

# N, M = map(int, input().split())
# a = []
# count = 0
# for i in range(N):
#     a.append('.' + input() + '.')
# a.insert(0, ('.' * (M + 2)))
# a.append(('.' * (M + 2)))
# for i in range(1, N + 1):
#     for j in range(1, M + 1):
#         if a[i][j] == a[i][j - 1] == a[i][j + 1] == a[i - 1][j] == a[i + 1][j] == '.':
#             count += 1
# print(count)

# n, m = map(int, input().split())
# a = []
# b = []
# g = []
# for i in range(n):
#     for j in range(m):
#         a.append(j)
# for i in range(len(a)):
#     b.append(i)
# while len(b) > m:
#     pice = b[:m]
#     g.append(pice)
#     b = b[m:]
# g.append(b)
# for i in range(n):
#     if (i + 1) % 2 != 0:
#         print(*g[i])
#     elif (i + 1) % 2 == 0:
#         g[i].reverse()
#         print(*g[i])

# n, m = map(int, input().split())
# g = []
# u = 0
# for i in range(n):
#     a = []
#     for j in range(m):
#         a.append(u)
#         u += 1
#     g.append(a)
# for i in range(n):
#     if (i + 1) % 2 != 0:
#         print(*g[i])
#     elif (i + 1) % 2 == 0:
#         print(*g[i][::-1])

# N, M = map(int, input().split())
# n = 0
#
# for i in range(1, N + 1):
#   x = list(range(n, n + M))
#   n += M
#   if i % 2 == 0:
#     x = x[::-1]
#   print(*x)
#
# x = list(range(0, 0 + 10))
# print(x)

# r = range(10, 100, 10)
# print(list(r))

# n, m = map(int, input().split())
# N = 0
# for i in range(1, n + 1):
#     x = list(range(N, N + m))
#     print(x)
#     N += m

# a = [3, 8, 2, 3, 7]
#
# for i in range(len(a)):
#     for j in range(0, len(a) - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
# print(a)

# a = [3, 8, 2, 3, 7]
#
# for i in range(len(a)):
#     for j in range(len(a)):
#         if j != 0 and a[j] < a[j - 1]:
#             a[j], a[j - 1] = a[j - 1], a[j]
# print(a)

# n, m = map(int, input().split())
# color = 0
# BW = 0
# for i in range(n):
#     a = list(map(str, input().split()))
#     print(a)
#     for j in range(m):
#         if a[j] == 'W' or a[j] == 'B':
#             BW += 1
#         else:
#             color += 1
# if color == 0:
#     print('#Black&White')
# else:
#     print('#Color')


# n = int(input())
# mat = [[0] * n for i in range(n)]
# st, m = 1, 0
# # Заранее присваиваю значение центральному элементу
# # матрицы
# mat[n // 2][n // 2] = n * n
# print(n // 2)
# for v in range(n // 2):
#     # Заполнение верхней горизонтальной матрицы
#     for i in range(n - m):
#         mat[v][i + v] = st
#         st += 1
#         # i+=1
#     # Заполнение правой вертикальной матрицы
#     for i in range(v + 1, n - v):
#         mat[i][-v - 1] = st
#         st += 1
#         # i+=1
#     # Заполнение нижней горизонтальной матрицы
#     for i in range(v + 1, n - v):
#         mat[-v - 1][-i - 1] = st
#         st += 1
#         # i+=1
#     # Заполнение левой вертикальной матрицы
#     for i in range(v + 1, n - (v + 1)):
#         mat[-i - 1][v] = st
#         st += 1
#         # i+=1
#     # v+=1
#     m += 2
# # Вывод результата на экран
# for i in mat:
#     print(*i)

# n, m = map(int, input().split())
# b, c, l = [], [], []
# for i in range(n):
#     a = input()
#     if 'S' not in a:
#         b.append(a.count(a[i]))
#     else:
#         c.append(a)
# for j in range(m):
#     k = []
#     for i in range(len(c)):
#         k.append(c[i][j])
#     l.append(k)
# for i in range(len(l)):
#     if 'S' not in l[i] and len(l[i]) > 1:
#         b.append(len(l[i]))
# print(sum(b))

# n = int(input())
# a = []
#
# for i in range(n + 1):
#     a.append([1] + [0] * n)
#
# for i in range(1, i + 1):
#     for j in range(1, i + 1):
#         a[i][j] = a[i - 1][j] + a[i -1][j - 1]
#
# for i in range(i + 1):
#     for j in range(i + 1):
#         print(a[i][j], end='')
#     print()

# [выражение for val in коллеция]

# #[0, 0, 0, 0, 0, 0, 0, 0]
# a = [0 for i in range(8)]
# print(a)
# #
# a = []
# for i in range(8):
#     a.append(0)
# print(a)
# #[0, 1, 2, 3, 4, 5, 6, 7]
# a = [i for i in range(8)]
# print(a)
# # или
# a = []
# for i in range(8):
#     a.append(i)
# print(a)
#
# #[0, 1, 4, 9, 16, 25, 36, 49]
# a = [i**2 for i in range(8)]
# print(a)

# a = [i % 2 for i in range(21)]
# print(a)
#
# a = [i for i in 'hello']
# print(a)
#
# #or
#
# a = []
# for i in 'Hello':
#     a.append(i)
# print(a)

# a = [ord(i) for i in 'hello']
# print(a)

# import random
#
# a = [random.randint(-10, 10) for i in range(10)]
# print(a)
# a = [i + 1 for i in a]
# print(a)

# [выражение for val in коллеция if условие]

# import random
#
# a = [random.randint(-10, 10) for i in range(10)]
# print(a)
# a = [i for i in a if i % 2 == 0 and i % 3 == 0]
# print(a)

# -----------------------------------------------------------------------
# a = input().split()
# b = []
# for i in a:
#     b.append(int(i))
# print(b)

# or

# a = input().split()
# a = [int(i) for i in a]
# print(a)

# n = 4
# m = 5
#
# a = [[0] * m for i in range(n)]
# for i in a:
#     print(i)
#
# #or
#
# a = []
# for i in range(n):
#         a.append([0] * m)
# for i in a:
#     print(i)

# a = [[i, j] for i in 'abs' for j in range(4)]
# for i in a:
#     print(i)

# a = [[i * j] for i in range(6) for j in range(4)  if i * j >= 10]
# for i in a:
#     print(i)

# zeroes = [0 for i in range(100)]
# print(len(zeroes))


# n = int(input())
# a = [i for i in range(1, n + 1)]
# print(a)

from string import ascii_uppercase


# n = int(input())
# a = [ascii_uppercase[i] for i in range(n)]
# print(a)

# a = [ascii_uppercase[i] for i in range(int(input()))]
# print(a)

# print(list(ascii_uppercase[:int(input())]))

# st = 'Create a list of the first letters of every word in this string'
# st = [i[0] for i in st.split(' ')]
# print(st)

# from string import ascii_uppercase
# n = int(input())
# a = [ascii_uppercase[i] * (i + 1) for i in range(n)]
# print(a)

# a, b = map(int, input().split())
# s = [i**2 for i in range(a, b + 1) if a <= b] or [i**3 for i in range(b, a + 1)[::-1] if a > b]
# print(s)

# n = int(input())
# s = [i for i in range(1, n + 1) if n % i == 0]
# print(s)

# phrase = 'Take only the words that start with t in this sentence'
# s = [i for i in phrase.split(' ')]
# s = [s[i] for i in range(len(s)) if s[i][0] == 'T' or s[i][0] == 't']
# print(s)

# or

# print([i for i in phrase.split(' ') if i[0] == 'T' or i[0] == 't'])
# print([i for i in phrase.split(' ') if i[0] in 'Tt'])
# print([i for i in phrase.split(' ') if i.startswith(('T', 't'))])

# a = [
#     ('Mikle', 1995),
#     ('Godridg', 1965),
#     ['Gorhorn', 2005],
#     ('Jonson', 2011),
#     ('Davinci', 1970)
# ]
# b = [elem[0] for elem in a if elem[0].startswith('M')]
# print(b)
# b = [elem[1] for elem in a if elem[1] > 2000]
# print(b)
# b = [elem[0][0] for elem in a if elem[1] > 2000]
# print(b)

# a = {
#     'Mikle': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
#     'Godridg': {'age': 1967, 'hobby': 'box', 'car': 'Jaguar'},
#     'Jonson': {'age': 2001, 'hobby': 'IT', 'car': 'Opel'},
#     'Garry': {'age': 2005, 'hobby': 'travel', 'car': 'Lancha'},
# }
# b = [[elem, a[elem]['car']] for elem in a if a[elem]['age'] < 2000]
# print(b)

# a = 'jgslgjslJFLFJl45ksg,b,d;237'
# b = [int(i) for i in a if i.isdigit()]
# print(b)
# b = [i for i in a if i.isalpha()]
# print(b)

# import random
# n = 6
# m = 6
#
# a = [[random.randint(1, 7) for j in range(m)] for i in range(n)]
# for i in a:
#     print(i)
# print()
# b = [a[i][j] for i in range(n) for j in range(m) if i == j]
# c = [a[2][j] for j in range(m)]
# f = [a[i][3] for i in range(n)]
# print('diagonal', b)
# print('2d line', c)
# print('3d column', f)

# n = 5
# m = 5
# a = [[(i * j) for j in range(1, m + 1)] for i in range(1, n + 1)]
# for i in a:
#     print(i)

# vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
# vector = [vector[i][j] for i in range(len(vector)) for j in range((len(vector[0])))]
# print(vector)

#Creqte Dict +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# b = {}
# print(b)
# n = dict()
# print(n)

# #{'a': 100, 'b': 100}
# c = dict.fromkeys(['a', 'b'], 100)
# print(c)
#
# a = {'city': 'NY',
#     'city2': 'LY',
#      'city3': 'Chicago'
# }
#
# for key in a:
#     print(key, a[key])

# person = {}
# a = 'Garry Adan sendler Oxford 4 5 6 8 9 10'
# a = a.split()
# person['Name'] = a[0]
# person['Secodname'] = a[1]
# person['Lastname'] = a[2]
# person['University'] = a[3]
# person['Grids'] = []
# for i in a[4:10]:
#     person['Grids'].append(int(i))
# print(person)

# del person['University'] # удаление ключа--------------
# print(person)

# print('Name' in person)
# if 'University' in person:
#     print(person['University'])
# else:
#     person['University'] = 'Oxford'


# print(person)
# print(person.get('Name'))# если нет такого ключа, создаст новый ключ со значением None
# print(person.setdefault('Grids'))# если нет такого ключа, создаст новый ключ со значением None
# # или задать значение через запятую
# person.setdefault('school', 'Florida')
# print(person)
# print(person.pop('Secodname'))
# print(person)
# print(person.popitem()) # удаляет рандомно ключ и значение, т.к. словарь не упорядоченная последов..
# print(person.keys()) # возвращает все ключи из словаря
# for key in dict.keys(person):
#     print(key)
# print(person.values()) # возвращает значение ключа
# for value in person.values():
#     print(value)
# for i in person:
#     print(i, '+', person[i])
# print(person.items()) # возвращает картеж пар(key, value)
# for key, value in person.items():
#     print(key, ':', value)


# n = int(input())
# b = {}
# for i in range(1, n + 1):
#     if i not in b:
#         b[i] = i * i
# print(b)

# n = int(input())
# b = {}
# for i in range(1, n + 1):
#     b.setdefault(i, i * i)
# print(b)

# print({i: i*i for i in range(1, int(input()) + 1)})

# from string import ascii_lowercase
# alphabet = {ascii_lowercase[i]: (i + 1) for i in range(len(ascii_lowercase))}
# for key, value in alphabet.items():
#     print(key, value)

# from string import ascii_lowercase
# alphabet = {}
# for i in range(len(ascii_lowercase)):
#     alphabet[ascii_lowercase[i]] = i + 1 #setdefault(ascii_lowercase[i], i + 1)
# print(alphabet)


# d1 = {'a': 100, 'b': 200, 'c': 333}
# d2 = {'x': 300, 'y': 200, 'z': 777}
# rez = d1 | d2
# print(rez)
#
# d1 = {'a': 100, 'b': 200, 'c': 333}
# d2 = {'x': 300, 'y': 200, 'z': 777}
# rez = {**d1, **d2}
# print(rez)

# d1 = {'a': 100, 'b': 200, 'c': 333}
# d2 = {'x': 300, 'y': 200, 'z': 777}
# rez = d1
# for i in d2:
#     d1.setdefault(i, d2[i])
# print(rez)

# log = {}
# for i in range(int(input())):
#     a = input()
#     if a in log:
#         log[a] += 1
#         print(a + str(log[a]))
#     else:
#         log[a] = 0
#         print('OK')


# logins = {}
# logins['n'] = 2
# logins['n'] = logins['n'] + 3
# print(logins)
# for i in logins:
#     print(i + str(logins[i]))

# def create_phone_number(n):
#     n = str(n).replace(',', '').replace(' ', '').replace('[', '').replace(']', '')
#     return f'({n[:3]}) {n[3:6]} - {n[6:]}'
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

# def create_phone_number(n):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

# def create_phone_number(n):
#     return f'({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}'
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


# def sort_vowels(s):
#     b = []
#     for i in range(len(s)):
#         if s[i].isdigit() or s[i] == None:
#             print('')
#             break
#         elif s[i] in 'A, E, I, O, U, Y' or s[i] in 'a, e, i, o, u, y':
#             b.append('|' + s[i])
#         else:
#             b.append(s[i] + '|')
#     for i in range(len(b)):
#         print(b[i])
# sort_vowels(input())

# a = {
#     'BMW': 145,
#     'Oprl': 1478,
#     'Reno': 2578,
#     'Jaguar': 578
# }
#
# for i in sorted(a.items(), key=lambda para: (para[1], para[0])):
#     print(i)

# s = []
# d = {}
# g = []
# while True:
#     a = input()
#     if a == 'конец':
#         break
#     else:
#         s.append(a)
# for i in s:
#     i = i.replace('[', '').replace(']', '').split(':')
#     g.append(i)
# for i in g:
#     d.setdefault(int(i[1]), i[0])
# for i in sorted(d)[::-1]:
#     print(d[i])

# or

# d = {}
# while True:
#     a = input()
#     if a == 'конец':
#         break
#     else:
#         spis = a.split(':')
#         d.setdefault(int(spis[1]), spis[0])
# for i in sorted(d)[::-1]:
#     print(d[i])

# new_d = {}
# d = {}
# while True:
#     a = input()
#     if a == 'конец':
#         break
#     else:
#         spis = a.replace(' ', '').split(',')
#         d.setdefault(spis[0], []).append(int(spis[1]))
# # for i in d:
#     # new_d.setdefault(i, (sum(d[i])/len(d[i])))
# # for i in sorted(new_d.items(), key=lambda para: (-para[1], para[0])):
# #     print(*i)
#
# #or
#
# for k, v in d.items():
#     d[k] = sum(v)/len(v)
#
# for k, v in sorted(d.items(), key=lambda para: (-para[1], para[0])):
#     print(k, v)

# d = {}
#
# for s in iter(input, 'конец'):
#     k, v = s.split(', ')
#     d.setdefault(k, []).append(int(v))
#
# for k, v in d.items():
#     d[k] = sum(v) / len(v)
#
# for k, v in sorted(d.items(), key=lambda x: (-x[1], x[0])):
#     print(k, v)

# n = int(input())
# k = {}
# l = {}
# for i in range(n):
#     j = input()
#     if j in k:
#         k.setdefault(j, []).append(1)
#     else:
#         k.setdefault(j, []).append(1)
# for k, v in sorted(k.items(), key=lambda x: (x[1])):
#     l.setdefault(k, sum(v))
# for k, v in filter(lambda x: l[x[0]] == max(l.values()), l.items()):
#     print(f'{k}, {v}')
# for k, v in filter(lambda x: l[x[0]] == min(l.values()), l.items()):
#     print(f'{k}, {v}')

# n = int(input())
# l = {}
# for i in range(n):
#     j = input()
#     if j not in l:
#         l[j] = 1
#     else:
#         l[j] += 1
# l_max = max(l, key=l.get)
# l_min = min(l, key=l.get)
# print(f'{l_max}, {l[l_max]}')
# print(f'{l_min}, {l[l_min]}')

# s = {}
# for i in range(int(input())):
#     x = input()
#     s[x] = s.get(x, 0) + 1
# print(*max(s.items(), key = lambda value: value[1]), sep = ', ')
# print(*min(s.items(), key = lambda value: value[1]), sep = ', ')

# s = {}
# for i in range(int(input())):
#     x = input()
#     s[x] = s.setdefault(x, 0) + 1
# print(*max(s.items(), key=lambda val: val[1]), sep=', ')
# print(*min(s.items(), key=lambda val: val[1]), sep=', ')

# s = {}
# n = {}
# for i in range(int(input())):
#     x = input().split()
#     s.setdefault(*x)
# for k, v in s.items():
#     n.setdefault(v, []).append(k)
# for i in range(int(input())):
#     name = input()
#     if name in n:
#         print(*n[name])
#     else:
#         print('Неизвестный номер')

# n = {}
# for i in range(int(input())):
#     item = input().split()
#     if item[1] in n:
#         n[item[1]].append(item[0])
#     else:
#         n[item[1]] = [item[0]]
# for i in range(int(input())):
#     name = input()
#     if name in n:
#         print(*n[name])
#     else:
#         print('Неизвестный номер')
# b = {}
# for _ in range(int(input())):
#     phone_no, name = input().split()
#     b[name] = b.get(name, []) + [phone_no]
# for _ in range(int(input())):
#     lst = b.get(input(), [])
#     print(*lst if lst else ['Неизвестный номер'])

# b = {}
# for i in range(int(input())):
#     name, date, mon = input().split()
#     b[mon] = sorted(b.get(mon, []) + [name])
#
#
# #     b[mon].sort()!
# #
# for i in range(int(input())):
#     mon = input()
#     if mon in b:
#         print(*b[mon])
#     else:
#         print('Нет данных')
#или

# for _ in range(int(input())):
#     print(*sorted(b.get(input(), ["Нет данных"])))

# s = input()
# d = {}
#
# for i in s:
#     if i.isalpha():
#         d[i] = d.get(i, 0) + 1
#         # if i in d:
#         #     d[i] += 1
#         # else:
#         #     d[i] = 1
# for i in sorted(d):
#     print(i, d[i])

# words = {}
#
# while True:
#     n = input()
#     if n in words:
#         print(f'{n} переводится как {words[n]}')
#     else:
#         print(f'Введите перевод слова {n}')
#         words[n] = input()
#import age as age

# a = {
#     'Mikle': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
#     'Godridg': {'age': 1967, 'hobby': 'box', 'car': 'Jaguar'},
#     'Jonson': {'age': 2001, 'hobby': 'IT', 'car': 'Opel'},
#     'Garry': {'age': 2005, 'hobby': 'travel', 'car': 'Lancha'},
# }
#
# name = ['Mikle', 'Godridg', 'Jonson', 'Garry']
# for person in name:
#     # print(person, a[person]['hobby'])
#     print(person)
#     for data in a[person]:
#         print(data, a[person][data])

# b = [(name, a[name]['car']) for name in a]
# print(b)

# s = {}
# n = input()
#
# for i in n:
#     i = i.lower()
#     if i.isalpha():
#         s[i] = s.get(i, 0) + 1
# print(s)

# data = {
#   "my_friends": {
#     "count": ...,
#     "items": [
#       {
#         "first_name": 'Lot',
#         "id": 1,
#         "last_name": 'Cotovki',
#       },
#       {
#         "first_name": 'San',
#         "id": 2,
#         "last_name": 'Shurgen',
#       },
#     ]
#   }
# }
#
# names = []
# for i in data:
#   print(data[i]['items'])
#   for name in data[i]['items']:
#     names.append(name['first_name'])
# for i in sorted(names):
#   print(i)

# a = []
# b = []
# n, s = input(), input()
# for i in n:
#   a.append(i)
# for i in s:
#   b.append(i)
# if sorted(a) == sorted(b):
#   print('YES')
# else:
#   print('NO')

# s1, s2 = input(), input()
# d1, d2 = {}, {}
# for i in s1:
#   d1[i] = d1.get(i, 0) + 1
# for i in s2:
#   d2[i] = d2.get(i, 0) + 1
# print('YES 'if d1 == d2 else 'No')
# c = []

# morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
#          'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
#          'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
#          'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
#          'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
#          'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
#          'y': '—•——', 'z': '——••'}
# a = input().lower().split()
# print(a)
# for i in a:
#   for j in i:
#     if j in morze:
#       print(morze[j], end=' ')
#   print()


# people = [
#     ['Amy Smith', '694.322.8133x22426'],
#     ['Brian Shaw', '593.662.5217x338'],
#     ['Christian Sharp', '118.197.8810'],
#     ['Sean Schmidt', '9722527521'],
#     ['Thomas Long', '163.814.9938'],
#     ['Joshua Willis', '+1-978-530-6971x601'],
#     ['Ann Hoffman', '434.104.4302'],
#     ['John Leonard', '(956)182-8435'],
#     ['Daniel Ross', '870-365-8303x416'],
#     ['Jacqueline Moon', '+1-757-865-4488x652'],
#     ['Gregory Baker', '705-576-1122'],
#     ['Michael Spencer', '(922)816-0599x7007'],
#     ['Austin Vazquez', '399-813-8599'],
#     ['Chad Delgado', '979.908.8506x886'],
#     ['Jonathan Gilbert', '9577853541']
# ]
#
# print({i[1]: i[0] for i in people})

# data = {
#     'Jo Nikolas': '128',
#     'loren moriS': '58'
# }
# nwe_data = {key.title(): int(val) for key, val in data.items()}
# print(nwe_data)

# users = [
#     [0, 'pass', 'vslvnsl'],
#     [1, 'pass', 'vslv'],
#     [23, 'pass', 'vslv463030']
# ]
#
# info_user = {info[0]: info for info in users}
# print(info_user[1])

#Create Tuple+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# a = 1, 2, 3
# b = tuple((1, 2, 3)) # tuple([1, 2, 3]), ()
# c = tuple(range(5))
# s = 1, 5, 10, 2, 58, 41, 41, 42
# print(len(c))
# print(1 in c)
# print(c + a, a + c) # (0, 1, 2, 3, 4, 1, 2, 3) (1, 2, 3, 0, 1, 2, 3, 4)
# print(a * 2) #(0, 1, 2, 3, 4, 1, 2, 3) (1, 2, 3, 0, 1, 2, 3, 4)
# print(min(c), max(c), sorted(s))
# n = (1, 5, 8, 100)
# g = {}
# g[n] = 'Hello'
# print(g)
# print(list(n))

#Create Set +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ множество

# a = {1, 2, 1, 2, 10, 15, 11}
# print(a) #{1, 2, 10, 11, 15} убирает дубли
#
# b = {'Ho', 'Ho', 'ko', 'hi', 'hi', 'Ho', 'Ho', 'ko', 'hi', 'hi'} #{'Ho', 'ko', 'hi'}
# print(b)
#
# c = set('abrakadabra') #{'Ho', 'ko', 'hi'}
# print(c)
#
# d = set([1, 2, 1, 5, 6, 5])
# print(d)
#
# e = set(range(5))
# print(e)
#
# f = set()
#
# z = set((1, 5, 10, 1, 5))
# print(z)
#
# x = {1, 54, 13, 8, 8, 16}
# x.add(5)
# print(x)
#
# x.update([7, 8, 17])
# print(x)
#
# x.update('boom') #{1, 5, 7, 8, 13, 'o', 'm', 16, 17, 54, 'b'}
# print(x)
#
# x.update(range(3))
# print(x)
#
# x.discard('m') # without error, если повторно вызывать удалять m
# x.remove('o') # with error, если повторно вызывать удалять o
# x.pop() # delite random element
# x.clear() # delite all elements
# print(x)
#
# print(len(a)) # a = {1, 2, 1, 2, 10, 15, 11}
# print(2 in a)
#
# q = {1, 2, 3, 4, 5}
# w = {8, 2, 3, 4, 6}
#
# for i in q:
#     print(i) # only i
#
# print(q - w, '-------')
# print(w - q, '-------') # change w -= q
# print(q ^ w, '+++++++')
# print(q == w, '======')
# print(q >= b, '>>>>>>')
#
# print(q & w) #{2, 3, 4} cross elements
#
# print(q.intersection(w)) #{2, 3, 4} cross elements
#
# q.intersection_update(w) #{2, 3, 4} cross elements and change q or q&= w
#
# print(q, w) #{2, 3, 4} {2, 3, 4, 6, 8} cross elements
#
# print(q.union(w)) #{2, 3, 4, 6, 8} or q | w (change q |= w)

# a = input()
# b = set()
# while a != ' ':
#     slova = a.split()
#     b.update(slova)
#     a = input()
# print(b)

# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# print(*sorted(a & b))

# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# print(*sorted(a - b))

# a = input()
# b = [i for i in a]
# ye = set()
#
# for i in set(b):
#     if b.count(i) > 1:
#         if i.isdigit():
#             ye.update(i)
# if len(ye) == 0:
#     print('NO')
# else:
#     print(*sorted(ye))

# a = [i for i in input() if i.isdigit()]
# a = sorted(set(i for i in a if a.count(i) > 1))
# if len(a) > 0:
#     print(*a)
# else:
#     print('NO')
# a = [i for i in input()]
# a = [a[i] for i in range(len(a)) if i == a.index(a[i])]
# print(''.join(a))

# a = input()
# b = set(a)
# for i in a:
#     if i in b:
#         print(i, end='')
#         b.remove(i)

# a = [i for i in input() if i.isdigit()]
# b = set(a)
# for i in b:
#     a.remove(i)
# print(*a)

# a = {'Дили': [], 'Били': [], 'Вили': []}
# b = {}
# for i in iter(input, 'конец'):
#     k, v = i.split(': ')
#     a[k] = a.get(k, []) + [v]
# for i in a:
#     b[i] = b.get(i, len(set(a[i])))
# for k, v in sorted(b.items(), key=lambda para: -para[1]):
#     print(f'Количество уникальных комментаторов у {k} - {v}')
#
# a = {'Дили': set(), 'Били': set(), 'Вили': set()}
# for i in iter(input, 'конец'):
#     name, link = i.split(': ')
#     a[name].add(link)
# for i in a:
#     a[i] = len(a[i])
# for k, v in sorted(a.items(), key=lambda para: -para[1]):
#     print(f'Количество уникальных комментаторов у {k} - {v}')

# n = set(input())
# if len(n) % 2 == 0:
#     print('CHAT WITH HER!')
# else:
#     print('CHAT WITH HIM!')
#
# print('CHAT WITH HER!' if len(set(input())) % 2 == 0 else 'IGNORE HIM!')

# n = list(map(int, input().split()))
# m = set(n)
# for i in m:
#     if i in n:
#         n.remove(i)
# print(len(n))

# print(4 - len(set(input().split())))

# y = int(input()) + 1
# new_year = []
# count = y
# while True:
#     if len(set(str(count))) == 4:
#         new_year.append(count)
#         break
#     elif len(set(str(count))) != 4:
#         count += 1
# print(*new_year)

# y = int(input()) + 1
# while len(set(str(y))) != 4:
#     y += 1
# print(y)
# n = input()
# m = set()
# for i in n:
#     if i.isalpha():
#         m.add(i)
# print(len(m))

# print(len({i for i in input() if i.isalpha()}))
# import string
# n = int(input())
# words = set(input().lower())
# all_words = set(string.ascii_lowercase)
# if words == all_words:
#     print('YES')
# else:
#     print('NO')

## ['NO','YES'] - список к значениям которого можно обратится по индексу например ['NO','YES'][0] выдаст 'NO',
## одновременно с этим в питоне булевы значения фактически представляют целые, при этом False это 0, а True это 1
# print(['NO', 'YES', input()][len(set(input().lower())) == 26])
#
# input()
# print('YES' if len(set(input().lower())) == 26 else 'NO')

# def keanu_reeves():
#     return "YOU'RE BREATHTAKING"
# print(keanu_reeves())

# def square(n):
#     print(f'квадрат числа {n} = {n ** 2}')
# for i in range(1, 11):
#     square(i)
#
# # or
#
# def square(n):
#     return f'квадрат числа {n} = {n ** 2}'
# for i in range(1, 11):
#     print(square(i))

# def even(n):
#     if n % 2 == 0:
#         print(n, 'Chet')
#     else:
#         print(n, 'Nechet')
# for i in range(1, 11):
#     even(i)

# def fact(n):
#     pr = 1
#     for i in range(2, n + 1):
#         pr *= i
#     print(pr)
# fact(3)
#
# def factorial(v):
#     pr = 1
#     for i in range(2, v + 1):
#         pr *= i
#     return pr
# print(factorial(3))

# if 5 < 1:
#     def primer():
#         print('hello')
# else:
#     def primer():
#         print('Hello')
# primer()

# def sum(t):
#     S = 0
#     for i in range(1, t + 1):
#         S += i
#     print(f'Я знаю, что сумма чисел от 1 до {t} равна {S}')
# sum(int(input()))

# def check_password(s):
#     sif = 0
#     fig = 0
#     sim = 0
#     up = 0
#     for i in s:
#         fig += 1
#         if i in "!@#$%*":
#             sim += 1
#         if i.isdigit():
#             sif += 1
#         if i.isupper():
#             up += 1
#     if fig >= 10 and sif >= 3 and sim >= 1 and up >= 1:
#         print('Perfect password')
#     else:
#         print('Easy peasy')
# check_password('qwerty')

# def check_password(s):
#     num = [i for i in s if i.isdigit()]
#     up = [i for i in s if i.isupper()]
#     fig = [i for i in s if i in "!@#$%*"]
#     print('Perfect password' if len(num) >= 3 and len(up) >= 1 and len(fig) >=1 and len(s) >= 10 else 'Easy peasy')
# check_password('Qwerty1357!')

# def count_letters(n):
#     up = [i for i in n if i.isupper()]
#     lo = [i for i in n if i.islower()]
#     print(f'Количество заглавных символов:  {len(up)}')
#     print(f'Количество строчных символов: {len(lo)}')
# count_letters(input())

# import turtle
#
# def move(a):
#     turtle.forward(a)
#     turtle.left(90)
#
# def square(a): # рисует без цвета
#     for i in range(4):
#         move(a)
#
# def square_color(a, color):
#     turtle.color(color)
#     turtle.begin_fill()
#     square(a)
#     turtle.end_fill()
#
# turtle.speed(2)
#
# square_color(120, 'green')
# turtle.goto(150, 150)
# square_color(60, 'blue')

# import turtle
#
# def move_gor(a, b):
#     turtle.forward(a)
#     turtle.left(90)
#     turtle.forward(b)
#     turtle.left(90)
#
# def move(a, b, color):
#     turtle.color(color)
#     turtle.begin_fill()
#     move_gor(a, b)
#     move_gor(a, b)
#     turtle.end_fill()
#
# turtle.speed(1)
# move(100, 50, 'red')
# turtle.goto(150, 75)
# move(50, 30, 'blue')

# def even(n):
#     return n % 2 == 0
#
# for i in range(10):
#     print(i, even(i))

# def factorial(n):
#     pr = 1
#     for i in range(2, n + 1):
#         pr *= i
#     return pr
#
# def sochet(a, b):
#     return factorial(a)/ (factorial(b) * factorial(a - b))
# print(sochet(5, 3))

# def squareabdper(a, b):
#     return a * b, 2*(a+b)
#
# squar, per = squareabdper(4, 7)#возвращает в виде картежа
# print(squar, per)
# #или
# print(squareabdper(4, 7)) #возвращает в виде картежа

# def squareabdper(a, b):
#     mas = []
#     mas.append(a*b)
#     mas.append(2*(a+b))
#     return mas
# print(squareabdper(4, 7))


# def factorial(x):
#     pr = 1
#     for i in range(2, x + 1):
#         pr *= i
#     return pr

# def find_duplicate(n):
#     b = []
#     for i in n:
#         if i not in b and n.count(i) > 1:
#             b.append(i)
#     return b
# print(find_duplicate([1, 2, 1, 5, 7, 7, 10, 5, 3, 4]))

# def first_unique_char(f):
#     b = []
#     for i in f:
#         if i not in b and f.count(i) == 1:
#             b.append(i)
#     if len(f) == len(b):
#         return 0
#     elif len(b) == 0:
#         return -1
#     elif b[0] in f:
#         return f.index(b[0])
# print(first_unique_char('abracadabra'))

# def first_unique_char(f):
#     for i in f:
#         if f.count(i) == 1:
#             return f.index(i)
#     return -1
# print(first_unique_char('abracadabra'))

# def format_namelist(x):
#     s = []
#     m = ''
#     if len(x) == 0:
#         return ''
#     elif len(x) == 1:
#         return x[0]['name']
#     else:
#         for i in x:
#             s.append(i['name'])
#     if len(s) >= 2:
#         s.insert(-1, 'и')
#     for i in range(len(s))[:-3]:
#         m = m + s[i] + ', '
#     for i in range(len(s))[-3:]:
#         m = m + s[i] + ' '
#     return m
#
# print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]))
#
# def format_namelist(h):
#     a = []
#     for i in h:
#         for j in i.values():
#             a.append(j)
#     b = []
#     s = ''
#     if len(a)==1:
#         return a[0]
#     elif len(a) == 2:
#         return a[0] + ' и ' + a[1]
#     elif len(a)>=3:
#         for j in range(len(a) ):
#             s = (', '.join(a[:-1])) +' и '+a[-1]
#         return s
#     else:
#         return ''
# print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]))

# def q():
#     a = 10
#     #b = 20
#     print(a, b, 'local')
# a = 500
# b = 800
# q()
# print(a, b, 'global')

# def s():
#     # global a
#     a = 30
#
# a = [1, 5, 10]
# s()
# print(a)

# def n(x):
#     return x**2
# abs = n #global переопределение
# print(abs(-7), abs(5))
# def s():
#     a = 220
#     c = 'Good'
#     def r():
#         nonlocal a
#         a = 'Joom'
#         print(a, c)
#     r()
#     print(a)
# a = [1, 2]
# s()

# MIN_DRIVING_AGE = 18
#
# def allowed_driving(name, age):
#     if age >= MIN_DRIVING_AGE:
#         print(f'{name} может водить')
#     else:
#         print(f'{name} еще рано садиться за руль')
# print(allowed_driving(input(), int(input())))


# def f(a, b):
#     a = 10
#     b.append(1000) #можно менять значения в глобальном списке через методы
#     b[1] = 0
#     print(a, b, 'local')
#
# c = 'lort'
# d = [1, 5, 20, 7]
# f(c, d[:]) # чтобы не менялась гловальная переменнная можно добавить ее копию срезом [:]
# print(c, d, 'global')

# def g(a, b = 200, c = 'unknown'):
#     print(a, b, c)
# g(5, 10)

# def append_to_list(value, my_list = []):
#     my_list.append(value)
#     print(my_list)
#
# append_to_list(77) #[77]
# append_to_list(78) #[77, 78]
# append_to_list(287) #[77, 78, 287]
#
#
# def append_to_list(value, my_list = None):
#     if my_list is None:
#         my_list = []
#     my_list.append(value)
#     print(my_list)
#
# append_to_list(77) #[77]
# append_to_list(78) #[78]
# append_to_list(287) #[287]

# def append_to_dict(key, value, my_dict = {}):
#     # if my_list is None:
#     #     my_list = []
#     my_dict[key] = value
#     #or
#     #my_dict.setdefault(key, value)
#     print(my_dict)
#
# append_to_dict(1, 50) #[1: 50]
# append_to_dict(2, 70) #[1: 50, 2: 70]

# def append_to_dict(key, value, my_dict = None):
#     if my_dict is None:
#         my_dict = {}
#     # my_dict[key] = value
#     #or
#     #my_dict.setdefault(key, value)
#     #or
#     my_dict[key] = my_dict.get(key, value)
#     print(my_dict)
#
# append_to_dict(1, 50) #[1: 50]
# append_to_dict(2, 70) #[1: 50, 2: 70]


# a = [2, 7]
# print(list(range(*a)))


# def vok(a, b, c, d):
#     print(a, b, c, d)
#
# vok(1, 2, 3, 4)
# a = [25, 'Kool', [2, 'John', 15], 10]
# vok(*a)

# def f(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
# print(f(1, 15, 18, 20, 20))

# def f(**kwargs):
#     for k, v in kwargs.items():
#         print(k, v)
# f(a = 2, b = 8, m = 'Koko')

# a, *b, c = 'No money', 'no honey'
# print(a, b, c)

# def count_args(*args):
#     return len(args)
# print(count_args(1, 'koltor', [1, 2, 8]))


# def print_goods(*args):
#     a = []
#     for i in args:
#         if i == str(i) and str(i).isalpha():
#             a.append(i)
#     if len(a) == 0:
#         print('Нет товаров')
#     else:
#         for i in range(len(a)):
#             print(f'{i + 1}. {a[i]}')
#
# print(print_goods(1, True, 'Грушечка', '', 'Pineapple', []))

# def info_kwargs(**kwargs):
#     for k, v in sorted(kwargs.items(), key=lambda x: x[0]):
#         print(f'{k} = {v}')
# print(info_kwargs(first_name="John", last_name="Doe", age=33))

# def rec(x):
#     if x < 4:
#         print(x)
#         rec(x + 1)
#         print(x)
# rec(1)

# def fact(x):
#     pr = 1
#     for i in range(2, x + 1):
#         pr*= i
#     return pr
# print(fact(5))

# def f(n):
#     if n == 1:
#         return 1
#     return f(n - 1)*n
# print(f(5))

# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# print(fib(7))

# fib1 = 0
# fib2 = 1
# n = int(input())
#
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
# print(fib2)

# def palindrom(s):
#     if len(s) == 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return palindrom(s[1:-1])
# print(palindrom('шалаш'))


# n = int(input())
# s = list(map(int, input().split()))
#
# def rec(n):
#     if n > 0:
#         print(s[n - 1], end=' ')
#         rec(n - 1)
# rec(n)

# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
# print(fib((int(input())) + 1))


# def list_sum_recursive(b):
#     if len(b) == 0:
#         return 0
#     if len(b) == 1:
#         return b[0]
#     return b[0] + list_sum_recursive(b[1:])
#
# print(list_sum_recursive(list(map(int, input().split()))))

# def list_sum_recursive(b):
#     if len(b) == 1:
#         return b[0]
#     return b[0] + list_sum_recursive(b[1:])
#
# print(list_sum_recursive([1, 2, 3]))

# a = [1, 2, 3]
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

# a = [1, 2, 3]
# pr = 0
# for i in range(len(a)):
#     pr = a[i] + pr
# print(pr)

# def flatten(x):
#     new = []
#     for i in x:
#         if isinstance(i, int):
#             new.append(i)
#         else:
#             new += flatten(i)
#     return new
#
# print(flatten([1, [2,3], [[2], 5], 6]))

# def flatten(x):
#     new = []
#     for i in x:
#         if isinstance(i, list):
#             new.extend(flatten(i))
#         else:
#             new.append(i)
#     return new
#
# print(flatten([1, [2,3], [[2], 5], 6]))

# def flatten(x):
#     if not x:
#         return []
#     if isinstance(x[0], list):
#         return flatten(x[0]) + flatten(x[1:])
#     return x[0] + flatten(x[1:])
#
# print(flatten([1, [2, 3], [[2], 5], 6]))

# def sum(n):
#     if n == 1:
#         return 1
#     return n + sum(n - 1)
# print(sum(3))

# def pal(n):
#     if len(n) == 1:
#         return True
#     return n[0] == n[-1] and pal(n[1:-1])
#     # return ш == ш and аплпа
#     # return а == а and плп
#     # return п == п and л
# print(pal('шаплпаш'))

# def sum_list(n):
#     if len(n) == 0:
#         return 0
#     return n[0] + sum_list(n[1:])
#     # return 1 + [2, 3, 4]
#     # return 2 + [3, 4]
#     # return 3 + [4]
#     # return 4 + []
# print(sum_list([1, 2, 3, 4]))


# def max_list(n):
#     if len(n) == 1:
#         return n[0]
#     return max(max_list(n[1:]), n[0])
# print(max_list([1, 2000, 3, 500]))

# a = 'ifkfi'
# count = 0
# for i in a:
#     if len(a) <= 1:
#         print(a)
#         break
#     if a[0] == a[-1]:
#         count += 1
#     a = a.replace(a[0], '').replace(a[-1], '')
# print(count)

# def rec(n):
#     if len(n) == 1 or len(n) == 2:
#         return n
#     return n[0] + '(' + rec(n[1:-1]) + ')' + n[-1]
#     #return h + '(' + rec(n[ell]) + ')' + o
#     # return e + '(' + rec(n[ell]) + ')' + l
#     #return e + '(' + rec(n[l]) + ')' + l
# print(rec('helo'))

# def rec(a, x):
#     if x == 0:
#         return 1
#     if x % 2 == 0:
#         return rec(a, x//2) * rec(a, x//2)
#     else:
#         return rec(a, x - 1) * a
# print(rec(3, 2))

# def rec(a, level = 1):
#     print(*a, 'level', level)
#     for i in a:
#         if isinstance(i, list):
#             rec(i, level + 1)
# print(rec([1, 2,[4,5,[78, [1]]], [4, 8], 1]))

# a, b = map(int, input().split())
# n = list(map(int, input().split()))
# m = list(map(int, input().split()))
# c = []
# i = 0
# f = 0
# while i < a and f < b:
#     if n[i] < m[f]:
#         c.append(n[i])
#         i += 1
#     else:
#         c.append(m[f])
#         f += 1
# while i < a:
#     c.append(n[i])
#     i += 1
# while f < b:
#     c.append(m[f])
#     f += 1
# print(c)

# функция merge_two_list должна объединить два списка
# def merge_two_list(a, b):
#     i = j = 0
#     c = []
#     while len(a) > i and len(b) > j:
#         if a[i] < b[j]:
#             c.append(a[i])
#             i += 1
#         else:
#             c.append(b[j])
#             j += 1
#     while i < len(a):
#         c.append(a[i])
#         i += 1
#     while j < len(b):
#         c.append(b[j])
#         j += 1
#     return c
# # print(merge_two_list(a = [6, 2, 19], b = [5, 10, 7, 11]))
# # функция merge_sort должна выполнить сортировку
# def merge_sort(s):
#     if len(s) == 1:
#         return s
#     midle = len(s) // 2
#     s_left = merge_sort(s[:midle])
#     s_right = merge_sort(s[midle:])
#     #print(s_left, s_right)
#     return merge_two_list(s_left, s_right)
#
#
# print(merge_sort([6, 2, 19, 5, 10, 7, 11]))
# import time
# start = time.localtime()
# def quick_sort(s):
#     if len(s) <= 1:
#         return s
#     elem = s[0]
#     left = list(filter(lambda x: x < elem, s))
#     #left = [i for i in s if i < elem]
#     center = [i for i in s if i == elem]
#     right = list(filter(lambda x: x > elem, s))
#     #right = [i for i in s if i > elem]
#     return quick_sort(left) + center + quick_sort(right)
#
# print(quick_sort([16, 19, 2, 12, 20, 15, 20, 15]))
# end = time.localtime()
# print(end.tm_sec - start.tm_sec)

# import time
# start = time.localtime()
# def sort(a):
#     for i in range(len(a)):
#         for j in range(len(a) - 1):
#             if a[j] > a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#     return a
# print(sort([16, 19, 2, 12, 20, 15, 20, 15]))
# end = time.localtime()
# print(end.tm_sec - start.tm_sec)
# import os
#
# def doc(path, level = 1):
#     print('level=', level, 'content', os.path.isdir(path))
#     for i in os.listdir(path): # return list of doc
#         if os.path.isdir(path + '\\' + i):
#             print('Спускаемся', path + '\\' + i)
#             doc(path + '\\' + i, level + 1)
#             print('Возвращаемся', path)
#         #print(path + '\\' + i, os.path.isdir(path + '\\' + i)) #isdir find folder, isfile find file
#
# print(doc('D:\\фото'))

import os

def new_doc(folder, level = 1):
    print('level=', level, 'content', os.path.isdir(folder))
    for i in os.listdir(folder):
        if os.path.isdir(folder + '\\' + i):
            print('Спускаемся', folder + '\\' + i)
            new_doc(folder + '\\' + i, level + 1)
            print('Возвращаемся', folder)
print(new_doc('D:\\progs'))


