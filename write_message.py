filename = 'files_txt\\text_write.txt'

#with open(filename, 'a') as file_object:
#    file_object.write("I love programming!\n\r")

key_clear = input("Очистить файл 'text_write.txt' (y/n)? ")
if key_clear == 'y':
    key = 'w'
else:
    key = 'a'

with open(filename, key) as file_object:
    while True:
        name = input("Как тебя зовут? ('q' - выход) ")
        if name == 'q':
            break
        else:
            file_object.write(name+"\n")
            print(f"Приветствую {name}!")