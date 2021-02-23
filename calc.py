import sys

def num_input(text):
    key = True
    while key:
        num_str = input(text + " (q- выход): ")
        if num_str == 'q':
            print("Программа завершена.")
            sys.exit(0)
        try:
            num = int(num_str)
        except ValueError:
            print("Введено не число. Повторите ввод. ")
        else:
            return num

op = input("Введите операцию (+, -, *, /): ")
if op in ['+', '-', '*', '/']:
    n1 = num_input("Введите первое число: ")
    n2 = num_input("Введите второе число: ")
    if op == '+':
        res = n1 + n2
    elif op == '-':
        res = n1 - n2
    elif op == '*':
        res = n1 * n2
    elif op == '/':
        try:
            res = n1 / n2
        except ZeroDivisionError:
            res = "Делить на ноль нельзя"
else:
    res = "Вид операции введен неверно (+, -, *, /)"

print(res)