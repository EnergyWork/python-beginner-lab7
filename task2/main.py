import pandas as pd

def task1():
    data = pd.read_csv('E:\\myPy\\Lab7\\titanic.csv', index_col='PassengerId')
    alive = data['Survived'].value_counts()[1]
    dead = data['Survived'].value_counts()[0]
    total = alive + dead
    print('Доля выживших =', round((alive/total)*100.0, 2), '%')
    print()

def task2():
    data = pd.read_csv('E:\\myPy\\Lab7\\titanic.csv', index_col='PassengerId')
    womans = data['Sex'].value_counts()[1]
    mens = data['Sex'].value_counts()[0]
    print('Количество женщин =', womans)
    print('Количество мужчин =', mens)
    womans_a = len(data.loc[(data['Survived'] == 1) & (data['Sex'] == 'female')])
    mens_a = len(data.loc[(data['Survived'] == 1) & (data['Sex'] == 'male')])
    print(womans_a)
    print('Доля выживших женщин =', round(womans_a/womans*100.0, 2), '%')
    print('Доля выживших мужчин =', round(mens_a/mens*100.0, 2), '%')
    print()

def task3():
    data = pd.read_csv('E:\\myPy\\Lab7\\titanic.csv', index_col='PassengerId')
    first = len(data.loc[data['Pclass'] == 1, 'Pclass'])
    first_a = len(data.loc[(data['Survived'] == 1) & (data['Pclass'] == 1)])
    second = len(data.loc[data['Pclass'] == 2, 'Pclass'])
    second_a = len(data.loc[(data['Survived'] == 1) & (data['Pclass'] == 2)])
    third = len(data.loc[data['Pclass'] == 3, 'Pclass'])
    third_a = len(data.loc[(data['Survived'] == 1) & (data['Pclass'] == 3)])
    total = sum(data['Pclass'].value_counts())
    print('Доля первого класса =', round((first/total)*100.0, 2), '%')
    print('Доля выживших первого класса =', round((first_a/first)*100.0, 2), '%')
    print('Доля второго класса =', round((second/total)*100.0, 2), '%')
    print('Доля выживших второго класса =', round((second_a/second)*100.0, 2), '%')
    print('Доля третьего класса =', round((third/total)*100.0, 2), '%')
    print('Доля выживших третье класса =', round((third_a/third)*100.0, 2), '%')
    print()

def task4():
    data = pd.read_csv('E:\\myPy\\Lab7\\titanic.csv', index_col='PassengerId')
    avg = data['Age'].mean()
    med = data['Age'].median()
    print('Среднее всех =', avg)
    print('Медиана всех =', med)
    avg_a = data.loc[data['Survived'] == 1, 'Age'].mean()
    med_a = data.loc[data['Survived'] == 1, 'Age'].median()
    print('Среднее выживших =', avg_a)
    print('Медиана выживших =', med_a)
    avg_d = data.loc[data['Survived'] == 0, 'Age'].mean()
    med_d = data.loc[data['Survived'] == 0, 'Age'].median()
    print('Среднее мертвых =', avg_d)
    print('Медиана мертвых =', med_d)
    print()

def parse_wfname(n):
    first = n.str.extract(r'Mrs\.\s+[^(]*\((\w+)', expand=False)
    first.loc[first.isna()] = n.str.extract(r'\.\s+(\w+)', expand=False)
    return first

def parse_gfname(n):
    first = n.str.extract(r'Miss\.\s+(\w+)', expand=False)
    first.loc[first.isna()] = n.str.extract(r'\.\s+(\w+)', expand=False)
    return first

def womans_names(data):
    wnames = parse_wfname(data.loc[data['Sex'] == 'female', 'Name'])
    #gnames = parse_gfname(data.loc[data['Sex'] == 'female', 'Name'])
    #tnames = pd.concat([wnames, gnames])
    #print(tnames.value_counts())
    print(wnames.value_counts().index[0], wnames.value_counts()[0])
    print('\nUnique:')
    a = []
    for i in range(wnames.value_counts().count()):
        if wnames.value_counts()[i] == 1:
            a.append(wnames.value_counts().index[i])
    print(sorted(a))
    print()

def parse_mfname(n):
    first = n.str.extract(r'[Mr\.|Master\.]\s+(\w+)', expand=False)
    first.loc[first.isna()] = n.str.extract(r'\.\s+(\w+)', expand=False)
    return first

def mens_names(data):
    mnames = parse_mfname(data.loc[data['Sex'] == 'male', 'Name'])
    print(mnames.value_counts().index[0], mnames.value_counts()[0])
    a = []
    print('\nUnique:')
    for i in range(mnames.value_counts().count()):
        if mnames.value_counts()[i] == 1:
            a.append(mnames.value_counts().index[i])
    print(sorted(a))
    print()

def task5():
    data = pd.read_csv('E:\\myPy\\Lab7\\titanic.csv', index_col='PassengerId')
    womans_names(data)
    mens_names(data)

if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()
    task5()
