money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
def months_until_debt(money_capital, salary, spend, increase):
    months = 0

    while money_capital >= 0:
        # Добавляем зарплату к подушке безопасности
        money_capital += salary

        # Вычитаем текущие расходы
        money_capital -= spend

        # Увеличиваем количество месяцев
        months += 1

        # Увеличиваем расходы на 5% для следующего месяца
        spend *= (1 + increase)

    return months - 1  # Уменьшаем на 1, так как последний месяц некорректен

# Вычисляем количество месяцев, которые можно протянуть без долгов
months = months_until_debt(money_capital, salary, spend, increase)

print("Количество месяцев, которое можно протянуть без долгов:", months)
