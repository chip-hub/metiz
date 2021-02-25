"""Программа загружает имя пользователя, если оно было сохранено.
В противном случае запрашивает аго и сохраняет."""
import json

def get_stored_username():
    """Возвращает хранимое имя пользователя, если оно существует."""
    filename = 'username.json'
    try:
        with open(filename) as file_obj:
            username = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def save_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as file_obj:
        json.dump(username, file_obj)
        print(f"We'll remember you when you come back, {username}!")

def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
        print(f"Welcom back, {username}!")
        if input("It's you, isn't it (y/n)?").lower() == 'n':
            save_new_username()
    else:
        save_new_username()

greet_user()