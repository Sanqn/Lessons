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

# Creqte Dict +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
# или

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
# import age as age

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

# Create Tuple+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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

# Create Set +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ множество

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
# f(c, d[:]) # чтобы не менялась глобальная переменнная можно добавить ее копию срезом [:]
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
#     # return e + '(' + rec(n[l]) + ')' + l
#     #return '' + '(' + rec(n[l]) + ')' + ''
# print(rec('hello'))

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
#         if os.path.isdir(path + '\\' + i): #os.path.isdirfile (является ли путь файлом.)
#             print('Спускаемся', path + '\\' + i)
#             doc(path + '\\' + i, level + 1)
#             print('Возвращаемся', path)
#         #print(path + '\\' + i, os.path.isdir(path + '\\' + i)) #isdir find folder, isfile find file
#
# print(doc('D:\\фото'))

# def new_doc(folder,level = 1, name = 'База'):
#     #print('level=', level, 'content', os.path.isdir(folder))
#     for i in os.listdir(folder):
#         if os.path.isdir(folder + '\\' + i):
#             if i == name:
#                 print('Name is', folder + '\\' + i, '------------------------------------------------')
#             #print('Спускаемся', folder + '\\' + i)
#             new_doc(folder + '\\' + i, level + 1)
#             #print('Возвращаемся', folder)
# print(new_doc('D:\\progs'))

# def rec(x):
#     if len(x) == 1:
#         if x != '(':
#             return x + x
#         return '()'
#     if x[0] != '(':
#         return x[0] + rec(x[1:]) + x[0]
#     return '(' + rec(x[1:]) + ')'
# print(rec('he(ll((o('))


# per = lambda a, b, c: a + b + c
# print(per(1, 2, 3))

# a = {1: 'Ron', 2: 'Gorillas', 3: 'monkey'}
#
# for key, val in sorted(a.items(), key= lambda x: x[1]):
#     print(key, val)

# a = [10, 524, 16, 2, 7, 25578, 311, 11]
#
# a.sort(key= lambda x: x % 10) # сортировка по последней цифре
# print(a)

# def line(a, b):
#     return lambda x: x * a + b
#
# flag = line(2, 5)
# print(flag(3))


# adding_10 = lambda x: x + 10
# a = int(input())
# print(adding_10(a))

# starts_with = lambda x: True if x[0] == 'W' else False
# print(starts_with('War'))

# import datetime
# now = datetime.datetime.now()
# get_year = lambda now: now.year
# get_month = lambda now: now.month
# get_day = lambda now: now.day
# print(get_year(now))
# print(get_month((now)))
# print(get_year((now)))


# a = lambda **kwargs: sum(kwargs.values())
# print(a(one=1, two=2, three=3))

# a, b = map(int, input().split())
# print(list(map((lambda x: x**x), range(a, b + 1)))) #[1, 4, 27, 256, 3125]

# g = 'grey'
# def colors():
#     y = 'yellow'
#
#     def red():
#         nonlocal y
#         r = 'red'
#         print(r, g, p, y)
#         y = 'New color'
#     p = 'purpul'
#     g = 'black'
#     def blue():
#         b = 'blue'
#         print(b, g, p, y)
#
#     red()
#     blue()
#
# colors()

# def mine_fun(name):
#     def loc_fun():
#         print('Hello', name)
#     loc_fun()
# mine_fun('Lock')
# mine_fun('Joomba')

# def mine_fun(name):
#     def loc_fun():
#         print('Hello', name)
#     return loc_fun
# a = mine_fun('San')
# a()
# b = mine_fun('Konny')
# b()

# def adder(value):  # value 2
#     def inner(a): # a 2
#         print(value * a)
#     return inner
# a2 = adder(2)
# a2(2) # in inner(2)

# def counter():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner
# a = counter()
# a()

# def multiply(value):
#     def inner(a):
#         return value * a
#     return inner
# f_2 = multiply(2)
# f_2(15)

# def counter(n):
#     count = n
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner
#
# l, b = map(int, input().split())
# a = counter(l - 1)
# print(list(map(lambda x: x**a(), range(l, b + 1))))

# l, b = map(int, input().split())
# print(list(map(lambda x: x**x, range(l, b + 1))))


# def counter(n):
#     count = n
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner
# a, b = map(int, input().split())
# for i in range(a, b + 1):
#     enter = counter(i - 1)
#     print(enter() ** (enter() -1), end=' ')

# def func(n):
#     def f():
#         print(n)
#     return f
#
# numbers = 'one', 'two', 'three'
# new_list = []
# for i in numbers:
#     new_list.append(func(i))
# for z in new_list:
#     z()

# numbers = 'one', 'two', 'three'
# funcs = []
# for n in numbers:
#     funcs.append(lambda x = n: print(x))
# for f in funcs:
#     f()

# print(list(map(lambda x: x.upper(), ['cat', 'dog', 'cow'])))

# def avarage_namber():
#     nambers = []
#     def inner(namber):
#         nambers.append(namber)
#         print(nambers)
#         return sum(nambers) / len(nambers)
#     return inner
#
# d = avarage_namber()
# for i in range(1, 5 + 1):
#     print(d(i))

# def avarage_namber():
#     summ = 0
#     count = 0
#     def inner(namber):
#         nonlocal summ
#         nonlocal count
#         summ += namber
#         print(summ)
#         count += 1
#         print(count)
#         return summ / count
#     return inner
#
# d = avarage_namber()
# for i in range(1, 5 + 1):
#     print(d(i))


# def avarage_namber():
#     nambers = []
#     def inner(namber):
#         nambers.append(namber)
#         print(nambers)
#         return sum(nambers) / len(nambers)
#     return inner
#
# a = avarage_namber()
# a(2)
# a(5)
# print(a(7))

# from datetime import datetime
#
# def timer():
#     start = datetime.now()
#     def inner():
#         return datetime.now() - start
#     return inner
# d = timer()
# print(d())

# def add(a, b):
#     return a + b
#
# def counter(func):
#     count = 0
#     def inner(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f'function {func.__name__} repeat {count} times')
#         return func(*args, **kwargs)
#     return inner
# c = counter(add) # add without ()
# print(c(5, 10))
# #function add repeat 1 times
# #15
# print(c(22, 1120))
# #function add repeat 2 times
# #1142

# def mult(a, b, c):
#     return a * b * c
#
# def counter(func):
#     count = 0
#     def inner(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f'function {func.__name__} repeat {count} times')
#         return func(*args, **kwargs)
#     return inner
# z = counter(mult) # mult without ()
# print(z(5, 2, 3))
# print(z(15, 18, 3))

# def sum(a, b):
#     return a + b
#
# def decorator(func):
#
#     def inner(*args, **kwargs):
#         return func(*args, **kwargs)
#     return inner
#
# sum = decorator(sum)
# print(sum(10, 15))

# def decorator(func):
#
#     def inner(*args, **kwargs):
#         print('Wow ....')
#         func(*args, **kwargs)
#         print('Bay ....')
#     return inner
#
# def fio(name, surname, age):
#     print('hello', name, surname, age)
#
# fio = decorator(fio)
# fio('Loki', 'Nootik', 20)

# def hader(func):
#
#     def inner(*args, **kwargs):
#         print('<h1>')
#         func(*args, **kwargs)
#         print('</h1>')
#     return inner
#
# def table(func):
#     def inner(*args, **kwargs):
#         print('<table>')
#         func(*args, **kwargs)
#         print('</table>')
#     return inner
#
# @table
# @hader #fio = table(hader(fio))
# def fio(name, surname, age):
#     print('hello', name, surname, age)
#
# #fio = table(hader(fio))
# fio('Loki', 'Nootik', 20)

# from functools import wraps
#
# def hader(func):
#
#     @wraps(func) # оборачивает функцию mult вместо inner
#     def inner(*args, **kwargs):
#         print('<h1>')
#         func(*args, **kwargs)
#         print('</h1>')
#     return inner
# @hader # name = hader(name)
# def name(name):
#     print(name)
# name('Rokki')

# @hader
# def mult(a, b):
#     """
#     function multiply and return a * b
#     :param a:
#     :param b:
#     :return:
#     """
#     print(a * b)
# mult(10, 20)
# print(mult.__name__) # показывает имя функции
# print(help(mult)) # показывает коментарий к функции

# def print_given(*args, **kwargs):
#     for i in args:
#         print(i, type(i))
#
#     for k, v in kwargs.items():
#         print(k, v, type(v))
#
# print_given(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', two = 2, one = 1, three = 3)

# def spis(a, b, *args):
#     print(a + b, args)
#
# spis(2, 2, 1, 2, 3)

# a, b, *other = [1, 2, 3, 4, 5]
# print(a, b, other) #1 2 [3, 4, 5]

# a, b, *other = input().split()
# print(float(a), float(b), sep='\n')
# for i in other:
#     print(float(i))

# print(*map(float, input().split()), sep='\n')
# print((lambda x, y: x + y)(2, 5))
# print(list(map(lambda x: x.upper(), ['cat', 'dog'])))
# xs = [7, 95, 60, 20, 121]
# index_max = max((0, 1, 2, 3, 4), key=lambda i: xs[i])
# print(index_max)
# xs = [7, 95, 60, 20, 121]
# print(xs.index(max(xs)))

# number_names = {
# 0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
# 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
# 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
# 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
# 19: 'Nineteen'
# }

# def sort_digit(a):
#     for k, v in sorted(number_names.items(), key=lambda x: x[1]):
#         for i in a:
#             if i == k:
#                 print(k, end=' ')
#
# a = list(map(int, input().split()))
# sort_digit(a)

##or

# print(*sorted([int(num) for num in input().split()], key=lambda n: number_names[n]))

# lst = [('candy','30','100'), ('apple','10','200'), ('baby','20','300')]
# print(*sorted(lst, key=lambda x: x[1]))

# ids = ['id1', 'id100', 'id2', 'id22', 'id3', 'id30']
# print(*sorted(ids, key=lambda x: x[2:])) # id1 id100 id2 id22 id3 id30 (sort by digit)

# a = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
# print(sorted(a.items(), key=lambda x: x[1])) #[(5, 'A'), (2, 'B'), (3, 'B'), (1, 'D'), (4, 'E')]

# a = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
# print(sorted(a)) #[1, 2, 3, 4, 5]

# def make_gtetter(phrase):
#     prefix = phrase + ', '
#     def greetter(name):
#         return prefix + name
#     return greetter
# name_1 = make_gtetter('Hello')
# print(name_1('boss'))

# h(x) = f(g(x))

# def composition(f, g):
#
#     def h(*x):
#         return f(g(*x))
#     return h
# n = composition(sum, lambda x, y, z: (x**2, y**3, z**4))
# print(n(2, 3, 9))

# from datetime import datetime
#
# def timer():
#     start = datetime.now()
#     def inner():
#         return datetime.now() - start
#     return inner
# d = timer()
# print(d())

# def introduce(func):
#
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         return func(*args, **kwargs)
#
#     return wrapper
#
# @introduce
# def identity(x):
#     return x * 2
# print(identity(42))


# def timed(func):
#     def inner(*args, **kwargs):
#         tmp = time()
#         func(*args, **kwargs)
#         print(func.__name__, 'exicutd time =', time() - tmp)
#         return func(*args, **kwargs)
#     return inner
#
# def memoised(func):
#
#     mamory = {}
#     def wrapper(*args, **kwargs):
#         key = (args, tuple(sorted(kwargs.items())))
#         if key not in mamory:
#             mamory[key] = func(*args, **kwargs)
#         return mamory[key]
#     return wrapper
# @timed
# @memoised
# def colatz2(n):
#     while n != 1:
#         print(n)
#         n = (3*n + 1) if n % 2 != 0 else (n // 2)
# colatz2(5246464)


# def flip(func):
#     def inner(*args, **kwargs):
#         #args = args[::-1]
#         return func(*args[::-1], **kwargs)
#     return inner
# @flip
# def div(x, y, show=False):
#     res = x / y
#     if show:
#         print(res)
#     return res
# div(2, 4, show=True)

# def introduce_on_debug(func):
#     def inner(*args, **kwargs):
#         if debug:
#             print(func.__name__)
#             return func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return inner
# @introduce_on_debug
# def identity(x):
#     return x
# identity(239)
# from functools import wraps
#
# def optional_introduce(func):
#     @wraps(func)
#     def inner(*args, introduce=False, **kwargs):
#         if introduce:
#             print(func.__name__)
#             return func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return inner
# @optional_introduce
# def identity(x):
#     return x
# print(identity(42, introduce=True))


# from functools import wraps
#
# def introduce(n):
#     def optional_introduce(func):
#         @wraps(func)
#         def inner(*args, **kwargs):
#             print((func.__name__ + '\n')*n)
#             return func(*args, **kwargs)
#         return inner
#     return optional_introduce
# @introduce(4)
# def identity(x):
#     return x
# print(identity(42))

# from functools import wraps
#
# def bucket(*n, **kn):
#
#     def introduce(func):
#         @wraps(func)
#         def inner(*args, **kwargs):
#             print(f'({n}, {kn})')
#             return func(*args, **kwargs)
#         return inner
#     return introduce
# @bucket()
# def identity(x):
#     return x
# print(identity(42))

# from time import time
#
#
# def timed(func):
#     def inner(*args, **kwargs):
#         tmp = time()
#         func(*args, **kwargs)
#         print(func.__name__, 'exicutd time =', time() - tmp)
#         return func(*args, **kwargs)
#
#     return inner
# from functools import wraps
#
# def memoized(maxsize=None):
#
#     def other_func(func):
#         memory = {}
#         count = 0
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             nonlocal count
#             key = (args, tuple(sorted(kwargs.items())))
#             if maxsize is None:
#                 if key not in memory:
#                     memory[key] = func(*args, **kwargs)
#                 return memory[key]
#             elif key not in memory and count != maxsize:
#                 memory[key] = func(*args, **kwargs)
#                 count += 1
#             return memory[key]
#
#         return wrapper
#
#     return other_func
#
#
# @memoized(maxsize=None)
# def sum_of_two(a, b):
#     print(a, b, end='; ')
#     return a + b
#
# print(sum_of_two(2, 0), '\n')
# print(sum_of_two(2, 0), '\n')
#
# print(sum_of_two(4, 2), '\n')
# print(sum_of_two(4, 2), '\n')
#
# print(sum_of_two(5, 0), '\n')
# print(sum_of_two(5, 0), '\n')
#
# print(sum_of_two(4, 2))


# from functools import wraps
#
# def parameterized(init_deco):
#     def param_deco(*args, **kwargs):
#         def res_deco(func):
#             return init_deco(func, *args, **kwargs)
#         return res_deco
#     return param_deco
#
# @parameterized
# def introduce(func, n, newline=True):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         print(('\n' if newline else ' ').join([func.__name__]*n))
#         return func(*args, **kwargs)
#     return inner

# @introduce(4)
# def identity(x):
#     return x
# print(identity(42))

# from functools import wraps
#
# def decorator(res_inner):
#     def res_deco(func):
#         @wraps(func)
#         def inner(*args, **kwargs):
#             return res_inner(func, *args, **kwargs)
#         return inner
#     return res_deco
#
# @decorator
# def introduce(func, *args, **kwargs):
#     print(func.__name__)
#     return func(*args, **kwargs)
#
# @introduce
# def identity(x):
#     return x
#
# print(identity(31415))

# from functools import partial
#
# def con(n, a):
#     for i in a:
#         if i % n == 0:
#             print(i)
# con_class = partial(con, a = range(101))
# con_class(11)

# from functools import partial
# from functools import wraps
# def introduce(func = None, num = 1):
#     if func is None:
#         return partial(introduce, num = num)
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print((func.__name__ + ' ') * num)
#         return func(*args, **kwargs)
#
#     return wrapper
#
# @introduce(num = 5)
# def identity(x):
#     return x * 2
# print(identity(42))

# from functools import partial
# from functools import wraps
#
# def bucket(func = None, *n, **kn):
#     if func is None:
#         return partial(bucket, **kn)
#     @wraps(func)
#     def inner(*args, **kwargs):
#         print(f'{kn}')
#         return func(*args, **kwargs)
#     return inner
# @bucket
# def identity(x):
#     return x
# print(identity(42))

# def call(arg):
#
#     def actual_deco(func):
#         return func(arg)
#     return actual_deco
# n = 5
# @call('la')
# def printfew(string):
#     n = 3
#     print(string * n)

# from operator import attrgetter as attribute
#
# @len
# @attribute('__name__')
# def twenty_four():
#     pass
# print(twenty_four)

# def check(*preconditios):
#     def work_dek(func):
#         def inner(*args, **kwargs):
#             args_name = func.__code__.co_varnames
#             environment = dict(zip(args_name, args))
#             environment.update(kwargs)
#
#             for cond, msq in preconditios:
#                 if not eval(cond, environment):
#                     raise ValueError(msq)
#             return func(*args, **kwargs)
#
#         return inner
#
#     return work_dek
#
#
# @check(('all(xs[i] <= xs[i + 1] for i in range(len(xs)-1))',
#         'The data is not sorted'),
#        ('x != 0',
#         'Can not seek for zeros for same reason'))
# def binsearch(x, xs):
#     pass
#
#
# binsearch(2, [1, 2, 3])

# def apply(*args, **kwargs):
#     def dec(func):
#         return func(*args, **kwargs)
#     return dec
#
# @apply(2, 3)
# def multiply(x, y):
#     return x * y
#
# print(multiply, type(multiply))

# from patterns import patterns
#
# @patterns
# def product():
#     if []: 1
#     if [x] + xs: x * product(xs)
#
# print(product([1, 2, 3, 4, 5]))

# def product(value):
#
#     if value == []:
#         return 1
#     if isinstance(value, list) and len(value) >= 1:
#         x, xs = value[0], value[1:]
#         return x * product(xs)
# print(product([1, 2, 3, 4]))

# n = int(input())
# x = list(map(int, input().split()))
#
# # def rec(x):
# #     if len(x) == 1:
# #         return x
# #     return rec(x[1:]) + [x[0]]
# # print(*rec(x))
#
# def rec(n):
#     if n > 0:
#         print(x[n - 1], end=' ')
#         rec(n - 1)
# rec(n)

# def palin(n):
#     if len(n) == 1:
#         return True
#     if n[0] != n[-1]:
#         return False
#     return palin(n[1:-1])
# print(palin('ifkf'))

# def mult(n):
#     if len(n) == 0:
#         return 0
#     if len(n) == 1:
#         return n[0]
#     return n[0] * mult(n[1:])
# print(mult([1, 2, 3]))

# n = [5, 2, 9, 5, 1, 4, 16, 17]
#
# for i in range(len(n)):
#     for y in range(len(n) - 1):
#         if n[y] > n[y + 1]:
#             n[y], n[y + 1] = n[y + 1], n[y]
#
# print(n)

# import math as m #можно создать псевдоним (m)
# from math import factorial as fact # можно дать имени модуля псивдоним
# from math import * # импорт всех имен из модуля (не желательно так делать, могут перезатерется имена своих функций)


# def say_hello(name):
#     print('Hello', name)
#
# def summa(*args):
#     return sum(args)
#
# def fac(n):
#     if n == 0:
#         return 1
#     return n * fac(n - 1)
#
#
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
# my_str = 'Hihihihi'
#
# num_1 = 2
# num_2 = 3
#
# import calendar
#
# c = calendar.TextCalendar()
# print(c.formatyear(2021, 5))

# from less.dir.import_my_name import factor
# #import sys
# #import pprint
#
# print(factor(5))
# #pprint.pprint(sys.path)

# work with file ----------------------------------------------------------------

# file = open('text11.txt', 'a', encoding='utf-8')
#     # 'r'       open for reading (default)
#     # 'w'       open for writing, truncating the file first
#     # 'x'       create a new file and open it for writing
#     # 'a'       open for writing, appending to the end of the file if it exists
#     # 'b'       binary mode
#     # 't'       text mode (default)
#     # '+'       open a disk file for updating (reading and writing)
#     # 'U'       universal newline mode (deprecated)
# file1 = open(r'C:\Users\Admin\PycharmProjects\Lessons\less\text11.txt', encoding='utf-8')
# print(file.read(5)) # func 'read()' take argument, amount symbols
# print(file.read(5))
# file.seek(0) #returns cursor to 0 position
# print(file.read(5))
#
# print(file1.readline()) #read one line
# print(file1.readline())
# for row in file:
#     print(row)
#     for letter in row:
#         print(letter)
# s = file.readlines() # create list
# print(s)
# one_list = []
# for row in file:
#     if '\n' in row:
#         one_list.append(row[:-2])
#     else:
#         one_list.append(row)
# print(one_list)

# print(file.write(' Bye Bye'))
# file.close()

# def file_read(file_name):
#     print((open(file_name, encoding='utf-8')).read())
#
# file_read('text11.txt')

# def create_file_with_numbers(n):
#     file = open(f'range_{n}.txt', 'x+')
#     for i in range(1, n + 1):
#         file.write(str(i) + '\n')
#     print(file.read())

# def create_file_with_numbers(n):
#     open(f'range_{n}.txt', 'w').writelines('\n'.join(map(str, range(1, n + 1))))
#
# create_file_with_numbers(8)

# from string import punctuation
#
# def longest_word_in_file(file_name):
#     file = open(file_name, 'r', encoding='utf-8')
#     s = file.read()
#     ot = punctuation
#     # for i in s:
#     #     if i in ot:
#     #         s = s.replace(i, '')
#     # s = s.split()
#     # l = []
#     # z = {}
#     # for i in s:
#     #     z[i] = z.get(i, len(i))
#     # for k, v in sorted(z.items(), key=lambda x: x[1]):
#     #     l.append(k)
#     # return l[-1]
#     words = [*map(lambda x: x.strip(ot), s.split())]
#     return max(words[::-1], key = lambda x: len(x))
#
# print(longest_word_in_file('text11.txt'))


# from string import punctuation
# n = 'fsgs, sgsgs, gsgsg $ gssg! gsgsg'
# word = [*map(lambda x: x.strip(punctuation), n.split())]
# print(word)
# print(max(word[::-1], key=lambda x: len(x)))

# def number(files):
#     file = (open(files)).read()
#     s = [*map(lambda x: x.strip('\n'), file.split())]
#     count = 0
#     k = []
#     for i in s:
#         if len(i) == 3:
#             count += 1
#     print(count)
#     # for i in s:
#     #     if len(i) == 2:
#     #         k.append(int(i))
#     # print(sum(k))
#     print(sum(map(int, filter(lambda x: len(x)==2, s))))

# number(r"C:\Users\Admin\Downloads\numbers.txt")


# s = open(r"C:\Users\Admin\Downloads\numbers.txt").read().split()
# print(s)
# print(len(list(filter(lambda x: len(x) == 4, s))))
# print(sum(map(lambda x: int(x) if len(x) == 3 else 0, s)))
# print(sum(map(int, filter(lambda x: len(x) == 3, s))))

# a = [('john', 20, 'a'), ('lokki', 115, 'c'), ('nokia', 2, 'b')]
# print(sorted(a, key=lambda x: x[0]))

import os
from datetime import datetime

# if not os.path.isdir("folder"):
#      os.mkdir("folder") # создать пустой каталог (папку)
# print("Текущая деректория:", os.getcwd())# вывести текущую директорию
# os.chdir("folder") # изменение текущего каталога на 'folder'
# print("Текущая директория изменилась на folder:", os.getcwd()) # вывод текущей папки
#
# os.makedirs("nested1/nested2") # сделать несколько вложенных папок
# #os.chdir("..") # вернуться в предыдущую директорию
# print("Текущая деректория:", os.getcwd())
# # создать новый текстовый файл
# text_file = open("text.txt", "a+", encoding='utf-8')
# # запить текста в этот файл
# text_file.write("Это текстовый файл")
# text_file.write(f'currtn time: {datetime.now()}')
# print(text_file.read())
# os.chdir("..")
# os.removedirs("folder/nested1/nested2")
# os.remove("folder/text.txt") # удалить этот файл
# os.rmdir("folder") # удалить папку

# def find_filenme(path, name = 'numbers.txt'):
#     findname= []
#     s = []
#     for dirpath, dirnames, filenames in os.walk(path):
#         #перебрать каталоги
#         for dirname in dirnames:
#             #print("Каталог:", os.path.join(dirpath, dirname))
#             s.append(os.path.join(dirpath, dirname))
#         #перебрать файлы
#         for filename in filenames:
#             if filename == name:
#                 findname.append(os.path.join(dirpath, filename))
#                 #print("Файл:", os.path.join(dirpath, filename),'++++++++++++++++++++++++++++++++++++++++')
#                 newname = open(os.path.join(dirpath, filename), 'a+', encoding='utf-8')
#                 newname.write('Я тебя нашел')
#     print(s)
#     print(*findname)
#     print(os.stat(*findname))
# find_filenme("C:\\Users\\Admin")
import json
from random import randint
from datetime import datetime

# str_json = """{
#     "response": {
#         "count": 265448488,
#         "items": [{
#             "first_name": "Micke",
#             "id": 4564646,
#             "last_name": "Jordon",
#             "can_access_closed": true,
#             "is_closed": false,
#             "photo_50": "https://ggr-97...gggsgsgs1"
#         }, {
#             "first_name": "Tom",
#             "id": 7864456,
#             "last_name": "Cruse",
#             "can_access_closed": true,
#             "is_closed": false,
#             "photo_50": "https://ggr-12...gggsgsgs1"
#         }]
#     }
# }"""
#
# data = json.loads(str_json)
# print(data['response']['items'])
# for item in data['response']['items']:
#     del item['id']
#     item['like'] = randint(100, 500)
#     item['now_time'] = datetime.now().strftime('%d/%m/%y')
# #     for k, v in item.items():
# #         print(k, '=', v)
# new_json = json.dumps(data, indent=1)
# print(new_json)
# with open('my.json', 'w') as file:
#     json.dump(data, file, indent=3)

# with open('my.json', 'r') as file:
#     data = json.load(file)
# print(data)

# with open(r'C:\Users\Admin\Downloads\manager_sales.json', 'r') as file:
#     data = json.load(file)
# s = {}
# # a = []
# for item in data:
#     m = sum([pric['price'] for pric in item['cars']])
#     n = item['manager']['first_name'], item['manager']['last_name']
#     s.setdefault(n, m)
# print(*sorted(s.items(), key=lambda x: -x[1])[0])
# for k, v in sorted(s.items(), key=lambda x: x[1]):
#     print(*k, v)

# a = []
# for item in data:
#     a.append((item['manager']['first_name'], item['manager']['last_name'], len(item['cars']), sum([pric['price'] for pric in item['cars']])))
# print(*(sorted(a, key=lambda x: x[3])[-1]))

# with open(r'C:\Users\Admin\Downloads\group_people.json', 'r') as file:
#     data = json.load(file)
# s = {}
#
# for peop in data:
#     a = peop['id_group']
#     year = 0
#     for gen in peop['people']:
#         if gen['gender'] == 'Female' and gen['year'] > 1977:
#             year += 1
#     s[a] = year
# print(*sorted(s.items(), key=lambda x: x[1])[-1])

# def convert(group):
#
#     is_w_after_77 = lambda x: x['gender'] == 'Female' and x['year'] > 1977
#     return [group['id_group'], sum(map(is_w_after_77, group['people']))]
#
# with open(r'C:\Users\Admin\Downloads\group_people.json', 'r') as f:
#     groups = json.load(f)
# print(*max(map(convert, groups), key = lambda x: x[1]))
from string import punctuation

# with open(r'C:\Users\Admin\Downloads\Alphabet.json', 'r') as file:
#     data = json.load(file)
# with open(r'C:\Users\Admin\Downloads\Abracadabra.txt', 'r') as text_file:
#     new_text = text_file.read()
#
# # print(''.join([data.get(i) if i.isalpha() else i for i in new_text]))
# d = []
# for i in new_text:
#     if i.isalpha():
#         d.append(data[i])
#         #d.append(data.get(i))
#         #print(''.join(data.get(i)), end='')
#     else:
#         #print(i, end='')
#         d.append(i)
# str = ''.join(d)
# print(str)


# people = '[{"name": "Haley Whitney", "country": "British Indian Ocean Territory (Chagos Archipelago)", "age": 54}, {"name": "Matthew King", "country": "Colombia", "age": 34}, {"name": "Sean Sullivan", "country": "Mayotte", "age": 40}, {"name": "Christian Crawford", "country": "Russian Federation", "age": 29}, {"name": "Sarah Contreras", "country": "Honduras", "age": 82}, {"name": "Danielle Williams", "country": "Togo", "age": 91}, {"name": "Jonathan Wilson", "country": "Tunisia", "age": 49}, {"name": "Patricia Wilkerson", "country": "Georgia", "age": 22}, {"name": "Zachary Scott", "country": "Brunei Darussalam", "age": 55}, {"name": "Elizabeth Sanchez", "country": "Nauru", "age": 23}, {"name": "Christina Fernandez", "country": "Burundi", "age": 71}, {"name": "Allen Norton", "country": "Montserrat", "age": 79}, {"name": "Scott Arroyo", "country": "Montenegro", "age": 72}, {"name": "Brooke Boyd", "country": "Latvia", "age": 74}, {"name": "Jerry Morrow", "country": "San Marino", "age": 23}, {"name": "Danielle Bradshaw", "country": "Vietnam", "age": 64}, {"name": "Jerry Thompson", "country": "Belgium", "age": 30}, {"name": "Mark Jordan", "country": "Comoros", "age": 89}, {"name": "Joseph Berger", "country": "Cook Islands", "age": 94}, {"name": "Gina Brooks", "country": "Samoa", "age": 51}, {"name": "Walter Duran", "country": "Chad", "age": 67}, {"name": "John Martinez", "country": "Wallis and Futuna", "age": 65}, {"name": "Johnny Glover", "country": "Eritrea", "age": 72}, {"name": "Lindsay Moore", "country": "Liberia", "age": 53}, {"name": "Kimberly Burton", "country": "Nicaragua", "age": 92}, {"name": "Jacqueline Ballard", "country": "Nigeria", "age": 78}, {"name": "Charles Thompson", "country": "Saudi Arabia", "age": 50}, {"name": "Suzanne Roberts", "country": "Serbia", "age": 43}, {"name": "David Decker", "country": "South Africa", "age": 71}, {"name": "Christopher Perez", "country": "Cayman Islands", "age": 49}, {"name": "Debra Hall", "country": "Greece", "age": 13}, {"name": "John King", "country": "Bahamas", "age": 40}, {"name": "Justin Galvan", "country": "Namibia", "age": 19}, {"name": "Jacqueline Berger", "country": "Yemen", "age": 59}, {"name": "Shawn Robinson", "country": "Saint Pierre and Miquelon", "age": 32}, {"name": "Kristen Garcia", "country": "Portugal", "age": 48}, {"name": "Christopher Barry", "country": "French Polynesia", "age": 23}, {"name": "Alejandra Cook", "country": "Egypt", "age": 16}, {"name": "Jill Harrell", "country": "Comoros", "age": 49}, {"name": "Sara Zimmerman", "country": "Brazil", "age": 26}, {"name": "Mrs. Charlene Flores", "country": "New Caledonia", "age": 75}, {"name": "Melissa Crawford", "country": "Lebanon", "age": 17}, {"name": "Larry Wong", "country": "New Caledonia", "age": 6}, {"name": "Brenda Acosta", "country": "Grenada", "age": 48}, {"name": "Latoya Terry", "country": "Saint Martin", "age": 41}, {"name": "Seth Luna", "country": "Sao Tome and Principe", "age": 59}, {"name": "Micheal Adams", "country": "Barbados", "age": 53}, {"name": "Susan Carroll", "country": "Somalia", "age": 64}, {"name": "Douglas Morris", "country": "Thailand", "age": 24}, {"name": "Dennis Wagner", "country": "Zimbabwe", "age": 66}, {"name": "Kristin Johnson", "country": "Niue", "age": 71}, {"name": "Steven Krause", "country": "Turkmenistan", "age": 84}, {"name": "Jared Smith", "country": "Colombia", "age": 46}, {"name": "Lauren Anderson", "country": "Christmas Island", "age": 46}, {"name": "Joshua Spencer", "country": "Russian Federation", "age": 38}, {"name": "Maria Edwards", "country": "Hungary", "age": 78}, {"name": "Anne Lee", "country": "United States of America", "age": 10}, {"name": "James Mckenzie", "country": "Uganda", "age": 43}, {"name": "Joshua Gallegos", "country": "United States Minor Outlying Islands", "age": 27}, {"name": "Paul Herrera", "country": "Kiribati", "age": 17}, {"name": "Veronica White", "country": "Gabon", "age": 88}, {"name": "Michael Hall", "country": "China", "age": 43}, {"name": "Sabrina Thompson", "country": "Chad", "age": 27}, {"name": "Jennifer Archer", "country": "Korea", "age": 45}, {"name": "Christina Simmons", "country": "Israel", "age": 80}, {"name": "Travis White", "country": "Central African Republic", "age": 31}, {"name": "Dennis Hernandez", "country": "Slovenia", "age": 66}, {"name": "Matthew Richards", "country": "Svalbard & Jan Mayen Islands", "age": 34}, {"name": "Stephen Curry", "country": "Finland", "age": 92}, {"name": "Margaret Williamson", "country": "Hong Kong", "age": 86}, {"name": "Mary Estes", "country": "Montenegro", "age": 19}, {"name": "Alex Scott", "country": "Christmas Island", "age": 67}, {"name": "John Andrews", "country": "Bahamas", "age": 68}, {"name": "Jonathan Willis", "country": "Saint Martin", "age": 23}, {"name": "Olivia Campos", "country": "Armenia", "age": 72}, {"name": "Diana Davis", "country": "Azerbaijan", "age": 54}, {"name": "Jack Cummings", "country": "Martinique", "age": 94}, {"name": "Kaitlyn Mcdonald", "country": "Austria", "age": 12}, {"name": "Maria Blake", "country": "Pitcairn Islands", "age": 91}, {"name": "Kelly Thomas", "country": "Ethiopia", "age": 74}, {"name": "John Terrell Jr.", "country": "India", "age": 50}, {"name": "Lindsay Wood", "country": "United Arab Emirates", "age": 72}, {"name": "Matthew Gilbert", "country": "Madagascar", "age": 86}, {"name": "Tanner Johnson", "country": "Congo", "age": 11}, {"name": "Michael Garcia", "country": "Liberia", "age": 45}, {"name": "Nicole Johnson", "country": "Barbados", "age": 54}, {"name": "William Lee", "country": "Lithuania", "age": 59}, {"name": "Jeffrey Coffey", "country": "Faroe Islands", "age": 88}, {"name": "Sandra Freeman", "country": "Philippines", "age": 35}, {"name": "Latoya Maxwell", "country": "Sweden", "age": 12}, {"name": "Darius Blevins", "country": "Thailand", "age": 29}, {"name": "Teresa Newman", "country": "Jersey", "age": 6}, {"name": "Larry Bray", "country": "Brunei Darussalam", "age": 21}, {"name": "Adam Roberson", "country": "Jordan", "age": 71}, {"name": "Michael Gomez", "country": "Tajikistan", "age": 37}, {"name": "Abigail Mccarthy", "country": "Kiribati", "age": 85}, {"name": "Tom Morris", "country": "Cayman Islands", "age": 27}, {"name": "Kevin Wagner", "country": "Suriname", "age": 55}, {"name": "Peggy Bryant", "country": "Korea", "age": 36}, {"name": "Erik Mclaughlin", "country": "Austria", "age": 24}]'
# data = json.loads(people)
# sort_data = sorted(data, key=lambda x: (x['age'], x['name']))
# for i in sort_data:
#     print(f"{i['name']}, {i['country']}, {i['age']}")

# # Generator list---------------------------------------------+++++++++++++++++++++++++++++++++++++++++++++++
# a = [i ** i for i in range(5)]
# print(a)
#
# # Generator of objects------------------------------------------++++++++++++++++++++++++++++++++++++++++++++++
#
# b = (i ** i for i in range(5)) # Generator objects is developing 'next'
# #print(next(b)) #или вызыыввать по одному принту
# for i in range(5):
#     print(next(b), 'first') # Генератор можно обойти только один раз
# for i in b:
#     print(i, 'Second')
# for i in b:
#     print(i, 'Therd')
# print(sum(b))
# # Где полезно, если используются большие числа - 1000000000
#
# c = (i for i in range(10000000000))
# for i in c:
#     print(i)
# n = (i ** 2 for i in range(5))
# print(list(n))

# def genf():
#     s = 7
#     for i in list(range(5)):
#         yield i
#         print(s)
#         s += 10
#
# g = genf()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def fact(n):
#     pr = 1
#     for i in range(1, n + 1):
#         pr *= i
#         yield pr # выдает по одному значению и не сохраняет весь список в памяти
#
# for i in fact(10):
#     print(i)


# class map(object):++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#     """
#     map(func, *iterables) --> map object
#
#     Make an iterator that computes the function using arguments from
#     each of the iterables.  Stops when the shortest iterable is exhausted.

# a = [1, 5, 18, 58, -10]
# print(sorted(a))
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(map(lambda x: x**2, numbers)))
# print(list(map(lambda x: x**3, numbers)))

# class filter(object):==============================+++++++++++++++++++++++++++++++++++++++++++++++++++
#     """
#     filter(function or None, iterable) --> filter object
#
#     Return an iterator yielding those items of iterable for which function(item)
#     is true. If function is None, return the items that are true.
#     """

# def f(x):
#     return x > 10
#
# a = [1, 10, 0, 15, 258, 1567, 0, 8, 5, 16, 15]
# b = list(filter(f, a))
# print(b)
#
# def f(y):
#     return y % 2 == 0
#
# m = [1, 10, 0, 15, 258, 1567, 0, 8, 5, 16, 15]
# k = list(filter(f, m))
# print(k)

# z = [1, 10, 0, '', 258, ' ', 0, [8], 5, 16, 15]
# print(list(filter(bool, z)))

# a = ['hello', 'hi', 'madjongo', 'locki', 'patato']
#
# print(list(filter(lambda x: len(x) < 6, a)))
# print(list(map(lambda x: len(x) < 6, a)))

# a = 'jlsf42522JLEE533'
# print(list(filter(str.isalpha, a))) #isdigit, isupper, lower,

# d = {
#     'LA': 500,
#     'Moscow': 800,
#     'Chicago': 350,
#     'NY': 740
# }
# print(sorted(d.items(), key=lambda x: x[0]))
# print(list(filter(lambda x: d[x] > 600, d)))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(lambda x: x % 2 == 0, numbers)))

# numbers = [54, 71, 65, 51, 36, -82, -32, 61, -61, 92, 17, -68, -62, 40, 16, -49, -51, -38, 60, -24, -61, 3, -26, -46, -97, -28, 36, 7, 52, 56, -96, -69, 67, 76, 16, 36, 38, 74, 11, -87, 69, 69, -69, -61, 92, 67, -45, -26, 94, 38, 27, -26, 10, 55, 28, -81, 53, -75, -32, -83, 38, 83, -40, -51, 88, 28, 76, 25, 84, -79, -69, -65, 6, 12, 81, -58, -92, 44, -41, 60, -14, -65, 7, 64, -40, -25, -91, -23, -19, -40, -4, 36, 38, 28, -27, -28, 72, 47, -95, 47, 10, 31, 62, -75, 22, -34, 44, -62, -30, -41, 19, -13, 30, -11, -54, -46, -80, -57, -60, 72, -49, 84, 5, 66, 62, -35, 69, 23, 41, -15, 75, -53, 94, -76, -28, -41, -17, 71, 67, -50, 18, 65, -16, -27, -88, 21, -42, 58, 85, 36, 9, -72, -26, -73, -1, 41, -87, 85, 5, -92, -60, -33, 33, -74, 17, 47, -38, -95, -39, 64, 85, -27, -42, -91, -39, -15, -75, 78, -54, 26, -10, -3, 89, -11, -71, -85, 63, 9, -59, 72, 27, 40, 99, -9, 77, 64, -39, -28, 73, -50, -80, -74, 52, 26, 53, -18, 22, 70, 85, 1, -90, 53, -19, -80, -14, -29, -64, -21, 23, 99, 15, -52, 66, 30, 82, -81, -30, -68, 30, -25, -63, 33, 1, 0, 84, 18, -35, 31, -34, 10, 48, -37, -41, -94, -1, -14, -87, -37, -6, 48, 38, 33, -13, 71, -81, 45, -63, 52, -35, 34, -88, -82, -7, -92, -22, 96, -28, 0, 21, 74, -28, 81, 81, 44, -16, 17, -95, 18, -73, 15, -61, 6, -43, -67, -31, -61, -72, -66, 60, 67, -13, 47, 29, 44, -93, 55, -13, -23, 74, 79, 32, -20, 33, 17, -48, 7, 24, 19, 89, -60, 34, 81, 18, -39, 56, 10, -32, 46, -33, -75, -99, -37, -23, 59, -33, -1, 75, -65, 92, 80, 51, -59, -28, -22, -47, -1, 28, -85, 1, 23, -15, -66, -97, -25, 7, 17, -87, -60, 14, -70, 88, 20, 40, -89, 38, -41, -97, 76, 80, 43, 22, -72, -38, 47, -2, 12, 58, -91, 82, -98, 50, 15, -33, -56, 69, -27, 94, -90, 92, -71, -73, -71, -78, 22, -86, -48, 10, 46, 19, 68, -23, 52, -42, 74, 44, 89, -71, 93, 43, -86, 79, 3, -56, 14, 41, 15, -37, 77, -9, 36, 51, -89, 1, 37, 82, 27, 72, -92, 91, 94, 71, -81, -49, -42, 26, 57, -30, -40, 86, -77, -85, 1, 71, 16, 73, -82, 26, -90, 72, 14, -65, -55, 34, 45, 66, -64, -40, 92, 42, -78, -22, 53, -18, -41, -75, 10, -59, -55, 8, -90, -3, -65, 43, -49, -86, -96, 69, 48, 27, -48, -42, -34, -6, 7, 50, -55, -65, 79, 30, 16, -21, -98, -73, -25, -20, -51, 20, 17, -91, 34, 96, 12, 13, -58, -73, -82, 19, -48, -61, 57, 96, 74, 34, -63, 38, -27, -12, -24, 94, -25, -10, -41, 53, -13, 16, -21, 24, 96, 95, 58, 83, 10, 42, -11, -33, 10, 38, -6, -66, -40, -36, -99, -55, 37, -81, -93, 67, -77, -3, 77, 25, 38, -16, 21, -82, 77, 95, 73, 9, 94, -27, -21, -33, -90, 31, 98, 28, -63, 75, 53, -17, -1, 6, 51, 11, -92, 30, -24, 12, 47, -75, -15, -63, 57, 3, 37, -82, -28, -26, -3, -30, -90, -45, 20, -41, 72, -42, 15, -3, 92, 57, -1, 40, -65, 88, 28, -76, 52, -63, -51, 59, 69, -39, -47, -1, -18, -57, 68, 77, 66, 62, -71, 31, -50, 61, 88, 98, 5, 98, -57, -46, 2, 90, 43, 67, 76, -81, -57, 77, 25, -66, -81, -92, -76, 72, 14, 59, 52, 36, 20, -2, 92, 58, 36, -34, 94, -74, 42, -56, 96, -81, 69, -83, 71, -13, -13, 56, 86, -29, 58, -17, 65, 70, 74, 28, 8, 91, 51, 79, -57, -86, 5, -37, -67, -28, 56, 65, -90, 97, -20, 81, -85, -45, 46, -74, 76, -75, -7, 74, 82, 56, 14, -43, 20, -48, -99, 19, -39, -66, 44, -75, 24, -5, -70, 85, -12, 20, -85, -69, -26, -57, 28, -96, 42, -56, 13, 80, -48, 59, 11, -30, 4, -96, 58, 41, -2, -84, -51, 52, -69, 37, 60, -12, 48, -5, -48, 29, -62, 42, 15, 16, 65, 60, 43, -53, 4, 50, -21, 1, -21, -42, -57, -21, -50, -67, 77, -22, -5, 59, -67, 86, -77, 39, -67, 41, 83, -21, 33, 73, 55, 80, 93, 44, -71, 38, -93, 4, 83, -52, 75, -51, 1, -11, -45, 56, 81, 84, 70, 23, -36, -63, 69, 1, 86, -21, 53, -85, 70, -89, -31, -10, -94, -76, -17, -21, -60, 49, -22, -48, 67, 21, 18, 89, 20, 73, -43, -17, -52, 36, -21, 6, -37, -98, 94, 56, 31, 99, 86, 65, -19, -67, 46, 20, -29, -88, -54, 88, -12, -69, 17, 83, -94, 21, 59, -99, 70, -54, -35, 2, 58, 93, 1, -35, -44, 47, 40, 55, 10, -15, -96, -42, 10, -83, -82, -26, 48, 78, -72, 56, -99, -36, 25, 76, -3, -95, -38, -24, 96, 82, 7, 84, 46, 8, 93, -52, -86, 87, -85, -81, 52, -67, 52, -45, -93, -69, 60, -83, -20, -14, 80, -36, 62, -78, 3, -61, 51, 48, 73, 92, -65, 71, -86, 8, -14, 82, 58, -58, -21, 62, -38, 16, 20, -80, -78, 19, 19, 93, -83, 2, 71, 85, 71, -4, 81, 4, 90, 73, 21, -3, -55, 49, 66, -4, -6, 42, 76, -3, -94, 49, 55, -53, 12, 1, -25, 56, 93, -68, -21, 15, -13, 35, 71, -68, 34, -44, 48, 97, 51, 32, 87, 27, -85, -41, -27, 54, -91, -99, 83, -44, 70, -87, -76, 49, 99, 38, 15, 75, -54, -59, 22, 80, 49, -63, 8, -46, 97, -4, -92, -47, -20]
# # print(len(list(filter(lambda x: (0 > x), numbers))), len(list(filter(lambda x: x == 0, numbers))), len(list(filter(lambda x: x > 0, numbers))))
# #or
# # print(*list(eval(f'len(list(filter(lambda x: 0 {i} x, numbers)))') for i in ['<', '==', '>']))
# #or
# # a = [lambda x: x < 0, lambda x: x == 0, lambda x: x > 0]
# # for i in a:
# #     print(len(list(filter(i, numbers))), end=' ')

# days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
# print(*sorted(list(filter(lambda x: len(x) == 4 or x[0] == 'S', days))), sep='\n')

# class zip(object):+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#     """
#     zip(*iterables, strict=False) --> Yield tuples until an input is exhausted.
#
#        >>> list(zip('abcdefg', range(3), range(4)))
#        [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
#
#     The zip object yields n-length tuples, where n is the number of iterables
#     passed as positional arguments to zip().  The i-th element in every tuple
#     comes from the i-th iterable argument to zip().  This continues until the
#     shortest argument is exhausted.
#
#     If strict is true and one of the arguments is exhausted before the others,
#     raise a ValueError.
#     "

# a = [5, 8, 6, 7]
# b = [100, 200, 350, 150]
# c = 'abnc'
# # rez = list(zip(a, b, c))
# # print(sorted(rez, key=lambda x: x[0]))
# rez = zip(a, b, c) # выводт, как и yield только один раз (чтобы можно было ободить много раз, обернуть в list)
# # print(list(rez)) # [(5, 100, 'a'), (8, 200, 'b'), (6, 350, 'n'), (7, 150, 'c')]
# col1, col2, col3 = zip(*rez)
# print(col1, col2, col3) #(5, 8, 6, 7) (100, 200, 350, 150) ('a', 'b', 'n', 'c') unpack again

# employee_numbers = [2, 9, 18, 28]
# employee_names = ["Дима", "Марина", "Андрей", "Никита"]
#
# for name, number in list(zip(employee_names, employee_numbers)):
# 	print(name, number)
#
# rez = zip(employee_names, employee_numbers)
# col1, col2 = zip(*rez)
# print(list(col1), col2)

#sort(method'You can use only with list.sort') vs sorted(function) ==============++++++++++++++++++++++++++++++++++++++++++++++++++++

# a = [5, 10, 15, 0, 1, 5]
# b = 'hi how are you'
# c = ('hi', 'how', 'are', 'you')
# a.sort()
# for i in a:
#     print(i)
# print(sorted(c, reverse=False)) # always return list
# print(sorted(c, reverse=True))

#argument key in sort ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 1. func inset
# 2. func creation
# 3. methods (lower, upper)
# 4. lambda

# def f(x):
#     return x % 10, x // 10 % 10
#
# b = [500, 25, 18, 100, 37, 18, 27, 52, 3, 524]
# print(sorted(b, key=f))
# print(sorted(b, key=lambda x: (x % 10, x // 10 % 10)))

# a = [500, 25, 18, -100, 25, 18, -25, -52]
# print(sorted(a, key=abs))

# s = ['GGG', 'ggg', 'DDDDD', 'dd', 'mmmmmm', 'JJJ']
# print(sorted(s))
# print(sorted(s, key=str.lower))

# s = ['GGG 1', 'ggg 78', 'zzzzz 12', 'dd 78', 'mmmmmm 1', 'JJJ 8']
# print(sorted(s, key=lambda x: (int(x.split()[1]), x.split()[0].lower()[::-1])))

# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]
# # a = sorted(subject_marks, key=lambda x: x[1])
# # for i in a:
# #     print(*i)
# [print(*i) for i in sorted(subject_marks, key=lambda x: x[1])]

# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
#                  ('Physics', 93), ('History', 82), ('French', 78),
#                  ('Art', 58), ('Chemistry', 76), ('Programming', 91)]
# [print(*i) for i in sorted(subject_marks, key=lambda x: x[1])[::-1]]

subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
                 ('Physics', 93), ('History', 78), ('French', 78),
                 ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
[print(*i) for i in sorted(subject_marks, key=lambda x: (-x[1], x[0]))]




