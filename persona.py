from user import User, Admin 
    
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
