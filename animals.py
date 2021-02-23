filename_cat = "files_txt/cat.txt"
filename_dog = "files_txt/dog.txt"

def animals_get(filename):
    try:
        with open(filename) as file_object:
            names = file_object.readlines()
    except FileNotFoundError:
        pass
        #print(f"Файл {filename} не найден")
    else:
        for line in names:
            print(line.rstrip())

animals_get(filename_cat)
animals_get(filename_dog)