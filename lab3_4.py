salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев



def minimal_capital(salary, spend, months, increase):
    capital = 0
    for i in range(1, 11):
        capital -= spend
        capital += salary
        spend *= (1 + increase)
    return (round(-capital))
print(minimal_capital(salary, spend, months, increase))
