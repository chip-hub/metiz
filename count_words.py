def count_words(filename):
    """Подсчет приблизительного количества слов в файле."""
    try:
        with open(filename) as file_object:
            data = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist." 
        print(msg)
    else:
        words = data.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} wods.")

filenames = ['alice.txt', 'fignya.txt', 'the_princess_casamassima.txt', 'the_grey_monk.txt']
for filename in filenames:
    count_words('files_txt\\' + filename)