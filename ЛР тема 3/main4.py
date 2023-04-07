salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
total_spend = 0
need_money = 0  # количество денег, чтобы прожить 10 месяцев

for i in range(2, 11):  # TODO Оформить решение
    spend = spend + spend * 0.03
    total_spend +=spend
total_spend += 6000 #  добавим за первый месяц
total_salary = salary * months
need_money = total_spend - total_salary

print(round(need_money))
