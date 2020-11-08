import pandas as pd
import re, os, sys
from datetime import datetime as dt

MOSCOW = 1147
path = os.path.abspath(__file__)
WORK_AREA = os.path.split(path)[0]

def task1():
    df = pd.read_csv(os.path.join(WORK_AREA, 'moscow-buildings.csv'), index_col='house_id')
    df = df.drop(index=df[df.house_year == 'н.д.'].index)
    df.to_csv(os.path.join(WORK_AREA, 'df_build.csv'))
    print(pd.to_numeric(df['house_year']), end='\n\n')

def task2():
    df = pd.read_csv(os.path.join(WORK_AREA, 'df_build.csv'), index_col='house_id')
    #* минимальны и максиальный год
    house_min = df['house_year'].min()
    house_max = df['house_year'].max()
    print('house_year min =', house_min, ', house_year max =', house_max)
    #* странные даты, которые появились до появлени Москвы
    counter_deleted = len(df[df.house_year < MOSCOW].index)
    df = df.drop(df[df.house_year < MOSCOW].index)
    #* странные даты, которые появятся в "будущем"
    counter_deleted += len(df[df.house_year > dt.now().year].index)
    df = df.drop(df[df.house_year > dt.now().year].index)
    #* сохраняем без них
    df.to_csv(os.path.join(WORK_AREA, 'df_build.csv'))
    #* проверяем мин и мах уже на актуальных данных
    house_min = df['house_year'].min()
    house_max = df['house_year'].max()
    print('house_year min =', house_min, ', house_year max =', house_max, ', count deleted =', counter_deleted, end='\n\n')

def task3():
    df = pd.read_csv(os.path.join(WORK_AREA, 'df_build.csv'), index_col='house_id')
    ba = df[df.area_name == 'муниципальный округ Басманный']
    ba.to_csv(os.path.join(WORK_AREA, 'basm_data.csv'))
    print(ba, end='\n\n')

def task4():
    df = pd.read_csv(os.path.join(WORK_AREA, 'df_build.csv'), index_col='house_id')
    df = df.groupby(['area_name'])['building']
    dv = df.count()
    print('Районы:\n', dv, end='\n\n')

def task5():
    df = pd.read_csv(os.path.join(WORK_AREA, 'df_build.csv'), index_col='house_id')
    df['house_age'] = [dt.now().year - year for year in df['house_year']]
    print('Средний возраст дома =', round(df['house_age'].mean(), 2))
    vl = df.groupby(['area_name'])['house_age'].mean()
    print('Средний возраст района:\n', vl, end='\n\n')

def task6():
    df = pd.read_csv(os.path.join(WORK_AREA, 'df_build.csv'), index_col='house_id')
    house_min = df['house_year'].min()
    house = df[df.house_year == house_min]
    print(house, end='\n\n')

if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()