L = [123, 'spam', 1.23]  # Список из трех обьектов разных типов
print(len(L))
print(L[0])  # Доступ к элементу списка по его индексу
print(L[:-1])  # Операция получения среза возвращает новый список
print(L + [4, 5, 6])  # Операция конкатенации также возвращает новый список
print(L)  # Наши действия не привели к изменению оригинального списка
L.append('NI')  # Увеличение в конце списка добавляем новый обьект
print(L)
print(L.pop(2))  # Уменьшение удаляем элемент из середины списка
print(L)
del L[2]  # также удаляет элемент списка
print(L)

M = ['cc', 'aa', 'bb']
M.sort()
print(M)
M.reverse()  # В обоих случаях происходит изменение списка
print(M)
# M[99]  # Error выход за пределы списка

# Вложенные списки
M = [[1, 2, 3],  # Матрица 3 x 3 в виде вложенных списков
     [4, 5, 6],  # Выражение в квадратных скобках может
     [7, 8, 9]]  # занимать несколько строк
print(M)
print(M[2])  # Получаем строку 2
print(M[1][2])  # Получаем строку 2 затем 3 элемент в этой строке

# Генераторы списков
colTwo = [row[1] for row in M]  # Выбираем элементы второго столбца
print(colTwo)
print(M)  # Матрица не изменилась
col = [row[1] + 1 for row in M]  # Добавляем 1 к каждому элементу второго столбца
print(col)
print(M)
colTree = [row[1] for row in M if row[1] % 2 == 0]  # Отфильтровать нечетные значения
print(colTree)
print(M)
diag = [M[i][i] for i in [0, 1, 2]]  # Выборка элементор диагонали матрицы [1, 5, 9]
print(diag)
doubles = [c * 2 for c in 'spam']  # Дублирование символов в строке
print(doubles)
G = (sum(row) for row in M)  # Генератор возвращает сумму элементов строк
print(next(G))  # Вызов в соответствии с протоколом итераций
print(next(G))

print(list(map(sum, M)))  # Отобразить sum на элементы в M
print({sum(row) for row in M})  # Создает множиство сумм строк
print({i: sum(M[i]) for i in range(3)})  # Таблица пар ключь/значение сумм строк
print([ord(x) for x in 'spaam'])  # Список кодов символов
print({ord(x) for x in 'spaam'})  # Множиства ликвидируют дубликаты
print({x: ord(x) for x in 'spaam'})  # Ключи словарей являются уникальными


