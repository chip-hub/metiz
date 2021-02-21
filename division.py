print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    second_num = input("Second number: ")
    if second_num == 'q':
        break
    try:
        answer = int(int(first_num) / int(second_num))
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(f"Деление {first_num} на {second_num} равно {answer}.")
