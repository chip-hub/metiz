filename = "files_txt\\alice.txt"

try:
    with open(filename) as file_object:
        data = file_object.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist." 
    print(msg)
else:
    # Подсчет приблизительного количества слов в файле.
    words = data.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} wods.")