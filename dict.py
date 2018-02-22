# Словари
D = {'food': 'spam', 'quantity': 4, 'color': 'pink'}
print(D['food'])  # Получить значение связаное с ключем 'food'
D['quantity'] += 1  # Прибавить 1 к значению ключа 'quantity'
print(D['quantity'])
print(D)

Dic = {}
Dic['name'] = 'bob'  # В результате  присваевания создается ключь
Dic['job'] = 'dev'
Dic['age'] = 40
print(Dic)
print(Dic['name'])

rec = {'name': {'firstName': 'Bob', 'lastName': 'Smith'},
       'job': ['dev', 'mrg'],
       'age': 40.5}
print(rec)
print(rec['name'])  # Name - это вложенный словарь
print(rec['name']['lastName'])  # Обращение к элементу вложенного словаря
print(rec['job'])  # Job - это вложенный список
print(rec['job'][-1])  # Обращение к элементу вложенного списка
rec['job'].append('janitor')  # Расширение списка должностей Боба
print(rec)

di = {'a': 1, 'c': 3, 'b': 2}
print(di)
Ks = list(di.keys())  # Не упорядочный список ключей
print(Ks)
Ks.sort()  # Сортировка списка ключей
print(Ks)
for key in Ks:  # Обход отсортированного списка ключей
    print(key, ' => ', di[key])
print(di)
for key in sorted(di):
    print(key, '=>', di[key])
for c in 'spam':
    print(c.upper(), end=' ')
print()
x = 4
while x > 0:
    print('spam ' * x)
    x -= 1

squares = [2 ** x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]  # Генератор списков вычисляющий степень 2
print(squares)

squares2 = []
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:  # Эти же операции выполняет и генератор списков,
    squares2.append(2 ** x)  # следуя протоколу итерации
print(squares2)

print(di)
di['e'] = 99  # Присваивание по новому ключу приводит к раширению словаря
print(di)
# di['f']  #  Error такова ключа не существует
if not 'f' in di:
    print('Missing')

value = di.get('x', 0)  # Попытка получить значение указав значение поумолчанию
print(value)
value = di['x'] if 'x' in di else 0  # Выражение if/else
print(value)

