money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
i = 0
while money_capital + salary > spend*(1+i*increase):
    money_capital += salary
    money_capital -= spend*(1+i*increase)
    i += 1

print("Количество месяцев, которое можно протянуть без долгов:", i-1)
