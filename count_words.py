def count_words(filename):
    """Подсчет приблизительного количества слов в файле."""
    try:
        with open(filename) as file_object:
            data = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file '" + filename + "' does not exist." 
        with open('files_txt\\error.txt', 'w') as file_err:
            file_err.write(msg)            
        print(msg)
    else:
        words = data.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} wods.")

filenames = ['alice.txt', 'fignya.txt']
for filename in filenames:
    count_words('files_txt\\' + filename)