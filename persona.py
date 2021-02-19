privileges_list = ['просматривать сообщения',
                'добавлять сообщения',
                'удалять пользователей',
                'банить пользователей']

class Privileges():
    """Класс определяющий привелеги пользователя"""
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"Список прав: {self.privileges}")
            
class User():
    def __init__(self, first_name, last_name, privileges=[privileges_list[0]], **param):
        self.person_data = {}
        self.person_data['first_name'] = first_name
        self.person_data['last_name'] = last_name
        for key, val in param.items():
            self.person_data[key] = val
        self.login_attempts = 0
        self.privileges = Privileges(privileges)

    def describe_user(self):
        list_data = [(key, val) for key, val in self.person_data.items()]
        for i in list_data:
            print(f"{i[0]:<15}- {i[1]}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, privileges=privileges_list[:], **param):
        super().__init__(first_name, last_name, privileges=privileges_list[:], **param)
#        self.privileges = privileges_list[:]
    
user = User('Alex', 'Priv', age = '19', adress = 'Bryansk')
user.describe_user()
user.privileges.show_privileges()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Количество посещений {user.person_data['first_name']} - {user.login_attempts}")

user.reset_login_attempts()
print(f"Сброшено количество посещений {user.person_data['first_name']} - {user.login_attempts}")

admin = Admin('Sanya', 'Boss', age='34', adress='Bryansk', status='admin')
admin.describe_user()
admin.privileges.show_privileges()
