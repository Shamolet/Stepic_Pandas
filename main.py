import pandas as pd

df = pd.read_csv('lesson_1_data.csv', encoding='Windows-1251', sep=';')  # parse_dates=['create_data', 'payment_data'])

# print(df.columns)
# print(df.shape)  # атрибут, хранящий данные о размере таблицы в виде кортежа
# print(df.dtypes)  # атрибут возвращает серию с описанием типа каждой колонки
# print(df.describe())  # метод для вывода описания числовых колонок в датафрейме
# (число строк, среднее значение, стандартное отклонение, мин, макс и
# значения 25, 50, 75 квартилей)
# print(df.head())  # посмотреть первые 5 строк
# print(df.tail())  # посмотреть последние 5 строк

df = df.rename(columns={'Номер': 'number', 'Дата создания': 'date', 'Заработано': 'money'})
print(df.dtypes)

taxi = pd.read_csv('2_taxi_nyc.csv')
# print(taxi.shape, taxi.head(), taxi.dtypes)
taxi = taxi.rename(columns={'pcp 01': 'pcp_01', 'pcp 06': 'pcp_06', 'pcp 24':'pcp_24'})
print(taxi.dtypes)