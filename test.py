class MyBanc:
    def __init__(self, name_banc, name_client, balance):
        self.name_banc = name_banc
        self.name_client = name_client
        self.balance = balance

    def plus(self):
        x = int(input("Внесите сумму для пополнения: "))
        self.balance += x

    def minus(self):
        x = int(input("Внесите сумму для снятия: "))
        if self.balance < x:
            print("Недостаточно средств")
        else:
            self.balance -= x

    def info_data(self):
        print("Банк:", self.name_banc)
        print("Имя:", self.name_client)
        print("Баланс:", self.balance)

    def menu(self):
        print("1-Снять\n2-Пополнить\n3-Проверить баланс\n4-Выход")
        ans = input("Ваш выбор: ")
        return ans


banc = MyBanc("Сбербанк", "Юнус", 1000)

while True:
    ans = banc.menu()
    if ans == '1':
        banc.minus()
    elif ans == '2':
        banc.plus()
    elif ans == '3':
        banc.info_data()
    elif ans == '4':
        break
    else:
        print("Неправильный ввод!!!")

