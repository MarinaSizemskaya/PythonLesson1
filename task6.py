#Задача 6: Билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

#*Пример:*
#385916 -> yes
#123456 -> no

#Решение:
n = list(input("Введите шестизначный номер билета: "))
if (int(n[0]) + int(n[1]) + int(n[2])) == (int(n[3]) + int(n[4]) + int(n[5])):
    print("yes")
else:
    print("no")