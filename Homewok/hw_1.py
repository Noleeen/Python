# задача 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

date_week = int (input('enter number of the day of week: ')) 

if date_week > 5 and date_week < 8:
    print('weekend')
elif date_week > 0 and date_week < 6:
    print('working day')
else:
    print('you enterer wrong number ')