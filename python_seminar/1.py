# программа принимает 2 числа и говорит является ли первое квадратом второго

# a = int(input('a = '))
# b = int(input('b = '))

# if b == a**2:
#     print(f'yes it is{a}')
# else:
#     print('no')





# принимает 5 чисел и находит максимальное из них

#простой способ:
# list = map(int, input('enter numbers via commas').split(','))
# maxx = max(x)
# print(f'max number is {maxx}')

#способ прімітівнее

# list1 = []
# for _ in range(5):
#     user_number = int(input(f'input number '))
#     list1.append(user_number)
    
# print(list1)

# maxx = list1[0]

# for el in list1:
#     if el > maxx:
#         maxx = el
#         print(maxx)
# print(f'max volume is {maxx}')





# принимает 5 чисел и находит максимальное из них
# всё одним циклом, т е быстрее делает!

# num = int(input("enter number "))
# max = num
# for _ in range(4):
#     num = int(input('enter number '))
#     if num > max:
#         max = num
# print(max)





# 3) программа которая будет на вход принимать 
# число N и выводить числа от -N до N
# a = int(input('enter number '))
# l = []
# for i in range(-a, a+1):
#     l.append(i)
# print(str(l).strip('[]'))

# проще)
# a = int(input('enter number '))
# for i in range(-a, a+1):
#     print(i, end = ' ')

# ещё проще)
# a = int(input('enter number '))
# print(*range(-a,a+1), sep = ', ')




# 4) программа прінімаем на вход дробь и показывает 
# первую цифру дробной части числа 
# a = float(input('enter number '))

# if a % 1 == 0:
#     print("no")
# else:
#     print(int(((a*10) // 1) % 10))

# second way
# a = input('enter number ')

# if '.' not in a:
#     print("no")
# else:
#     print(int((float(a)*10) % 10))

# n = input()
# if '.' in n:
#     index_t = n.find('.')
#     print(n[index_t +1])
# else:
#     print('no')





# 5) программа прінімает на вход число и проверяет, 
# кратно ли оно 5 и 10 или 15, но не 30

a = int(input('enter number '))

if (a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and a % 30 != 0:
    print('yes')
else:
    print('no')







