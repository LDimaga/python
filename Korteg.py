# Основное отличие кортежей - это невозможность их изменения после создания. Кортежи являются не изменяемыми колекциями
T = (1, 2, 3, 4)  # Кортеж из 4 элементов
print(len(T))  # Длина
T += (5, 6)  # Конкатенация
print(T)
print(T[0])  # Извлечение элемента среза и так далее
print(T.index(4))  # Методы кортежей: значение 4 находится в позиции 3
print(T.count(4))  # Значение 4 присутствует в единственом экземпляре
# T[0] = 2  # <-- Error Кортежи являются неизменяемыми
T = ('spam', 3.0, [1, 2, 3])  # Кортежы могут хранить обьекты разных типов
print(T[0])
print(T[2][1])
# T.append(4)  # Error Кортежи являются неизменяемыми, добавление также не доступны.


