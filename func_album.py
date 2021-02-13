def go_on():
    answer = input("Input new album ('y' or anything)? ")
    if answer == 'y':
        return True
    else:
        return False

def in_album(name_artist, name_album):
    dict_album = {'name': name_artist, 'album': name_album}
    return dict_album

def main():
    list_album = []
    
    while go_on():
        name_artist = input('Input name of artist: ')
        name_album = input('Input name album: ')
        list_album.append(in_album(name_artist, name_album))

    print(list_album)



if __name__ == '__main__':
    main()