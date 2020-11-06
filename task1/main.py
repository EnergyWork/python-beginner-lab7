import pandas as pd
import re, os, sys
from datetime import datetime as dt

def task1():
    df = pd.read_csv('E:\\myPy\\Lab7\\moscow-buildings.csv', index_col='house_id')
    df = df.drop(df[df.house_year == 'н.д.'].index)
    df.to_csv('E:\\myPy\\Lab7\\df_build.csv')
    print(pd.to_numeric(df['house_year']))
    print()

def task2():
    df = pd.read_csv('E:\\myPy\\Lab7\\df_build.csv', index_col='house_id')
    house_min = df['house_year'].min()
    house_max = df['house_year'].max()
    print('House year min =', house_min, ', house year max =', house_max)
    val = len(df[df.house_year < 1147].index)
    df = df.drop(df[df.house_year < 1147].index)
    val += len(df[df.house_year > dt.now().year].index)
    df = df.drop(df[df.house_year > dt.now().year].index)
    df.to_csv('E:\\myPy\\Lab7\\df_build.csv')
    house_min = df['house_year'].min()
    house_max = df['house_year'].max()
    print('House year min =', house_min, ', house year max =', house_max, ', deleted items =', val)
    print()

def task3():
    df = pd.read_csv('E:\\myPy\\Lab7\\df_build.csv', index_col='house_id')
    ba = df[df.area_name == 'муниципальный округ Басманный']
    ba.to_csv('E:\\myPy\\Lab7\\basm_data.csv')
    print(ba)
    print()

def task4():
    df = pd.read_csv('E:\\myPy\\Lab7\\df_build.csv', index_col='house_id')
    df = df.groupby(['area_name'])['building']
    dv = df.count()
    #df.to_csv('E:\\myPy\\Lab7\\df_grouped.csv')
    print('Areas:\n', dv)
    print()

def task5():
    df = pd.read_csv('E:\\myPy\\Lab7\\df_build.csv', index_col='house_id')
    df['house_age'] = [dt.now().year - a for a in df['house_year']]
    print('House average age =', round(df['house_age'].mean(), 2))
    vl = df.groupby(['area_name'])['house_age'].mean()
    print('Areas average age =', round(vl, 2))
    print()

def task6():
    df = pd.read_csv('E:\\myPy\\Lab7\\df_build.csv', index_col='house_id')
    house_min = df['house_year'].min()
    house = df[df.house_year == house_min]
    print(house)
    print()

if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()