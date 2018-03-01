class Worker:
    def __init__(self, name, pay):  # Инициализация при создании self - это сам обьект
        self.name = name
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]  # Разбить строку по символам пробела

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)  # Обновить сумму выплат


bob = Worker('Bob Smith', 50000)  # Создается два экземпляра и для каждого определяется имя и сумма выплат
sue = Worker('Sue Jones', 60000)
print(bob.lastName())  # Вызов метода - self это bob
print(sue.lastName())  # self - это sue
sue.giveRaise(.10)  # Обновить сумму выплат для sue
print(sue.pay)
print(12 << 2)
