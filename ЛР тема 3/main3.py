money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

counter = 0  # TODO Оформить решение
while money_capital > 0:
    spend = spend + spend * 0.05
    money_capital = (money_capital + salary) - spend
    month += 1
print(month)
