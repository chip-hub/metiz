file_name = 'files_txt/learning_python.txt'

with open(file_name) as file_object:
    data = file_object.read()

print('".Read"')
print(data)

with open(file_name) as file_object:
    lines = file_object.readlines()

print('".readlines"')
for line in lines:
    print(line.rstrip())