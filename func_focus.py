list_focusn = ['Cyril Takayama', 'Dante the Magician', 'Magic Babe Ning']

def great_focusn(list_great):
    for key, name in enumerate(list_great):
        list_great[key] = "Greate " + name
    return list_great

def show_magicians(list_show):
    for l in list_show:
        print(f'Фокусник - {l}', end = "\n")

new_list = great_focusn(list_focusn[:])
show_magicians(list_focusn)
show_magicians(new_list)