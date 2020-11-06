import os, re
'''удаление у файлов паттерна, который добавляется для файлов с такимиже именами > (цифра)'''
path = os.path.abspath(__file__)
print(path)
for file in os.listdir(os.path.split(path)[0]):
    new_name = re.sub(r'\s*\(\d+\)', '', file)
    print('rename', file, 'to', new_name)
    os.rename(file, new_name)
stop = input('\nstop')
