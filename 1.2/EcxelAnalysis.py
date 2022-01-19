from matplotlib import pyplot
from openpyxl import load_workbook

# Загрузить таблицу Excel из файла в переменную wb

wb = load_workbook('data_analysis_lab.xlsx')
# print(wb)
# Загрузить лист с именем "Data" в переменную sheet
sheet = wb['Data']
# print(sheet)
# Получить содержимое колонки A в виде списка
colum_a = sheet['A'][1:]
#sheet['A'][1:]
colum_c = sheet['C'][1:]
colum_d = sheet['D'][1:]
#print(colum_a)
#print(colum_c)
#print(colum_d)

#Создаем фнкцию
def getvalue(x):
    return x.value
#передаем функцию getvalue в функцию map и записываем в переменную
ra = map(getvalue, colum_a)
rc = map(getvalue, colum_c)
rd = map(getvalue, colum_d)

#Создаем список для каждого столбца
r1 = list(ra)
r2 = list(rc)
r3 = list(rd)

#Печатаем значения в виде списка для каждого столбца
print(r1)
print(r2)
print(r3)

#Построение графика по точкам, первый аргумент список со значениями по оси X, во втором — значениями по оси Y
pyplot.plot(r1, r2, label = 'Метка')

# показать график
pyplot.show()
