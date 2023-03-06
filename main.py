import pandas as pd

df = pd.read_csv('lesson_1_data.csv', encoding='Windows-1251', sep=';')  # parse_dates=['create_data', 'payment_data'])

print(df.columns)
print(df.shape)  # атрибут, хранящий данные о размере таблицы в виде кортежа
print(df.dtypes)  # атрибут возвращает серию с описанием типа каждой колонки
print(df.describe())  # метод для вывода описания числовых колонок в датафрейме
# (число строк, среднее значение, стандартное отклонение, мин, макс и
# значения 25, 50, 75 квартилей)
print(df.head())  # посмотреть первые 5 строк
print(df.tail())  # посмотреть последние 5 строк
