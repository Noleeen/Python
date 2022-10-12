# задача 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# date_week = int (input('enter number of the day of week: ')) 

# if date_week > 5 and date_week < 8:
#     print('weekend')
# elif date_week > 0 and date_week < 6:
#     print('working day')
# else:
#     print('you enterer wrong number ')

# задача 2. Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

xyz = []
for i in range(3):
    xyz.append(int(input(f'enter {i+1} numbers: ')))
print(xyz)

if not(xyz[0] or xyz[1] or xyz[2]) == (not xyz[0] and not xyz[1] and not xyz[2]):
    print('True')
else:
    print('False')



# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).

# x = int(input('enter coordinate x: '))
# y = int(input('enter coordinate y: '))

# if x == 0 or y == 0:
#     print('your coordinate is on the border of quarters, enter coordinates not equal to zero ')
# elif x > 0 and y > 0:
#     print('1 quarter')
# elif x < 0 and y > 0:
#     print('2 quarter')
# elif x < 0 and y < 0:
#     print('3 quarter')
# elif x > 0 and y < 0:
#     print('4 quarter')

# задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского 
# ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым 
# числам ("первое число" "операция" "второе число") и выводит результат на экран.

# print('calculator: enter two numbers and mathematical operation (+, -, /, *, mod, pow, div)')
# a = float(input('enter first numbers: '))
# b = float(input('enter second numbers: '))
# math = input('enter math operation: ')

# if math == '+':
#     print(f'{a} + {b} = {a+b}')
# elif math == '-':
#     print(f'{a} - {b} = {a-b}')
# elif math == '/':
#     if b == 0:
#         print('error: divine by zero!')
#     else: 
#         print(f'{a} / {b} = {a/b}')
# elif math == '*':
#     print(f'{a} * {b} = {a*b}')
# elif math == 'mod':
#     print(f'{a} % {b} = {a%b}')
# elif math == 'pow':
#     print(f'{a} pow {b} = {a**b}')
# elif math == 'div':
#     print(f'{a} // {b} = {int(a//b)}')


