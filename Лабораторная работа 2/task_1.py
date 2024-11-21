def months_until_debt(money_capital, salary, spend):
    months = 0

    while money_capital >= 0:
        budget = money_capital + salary

        if budget >= spend:
            months += 1
            money_capital -= (spend - salary)  # Уменьшаем подушку безопасности
            spend *= 1.05  # Увеличиваем расходы на 5%
        else:
            break  # Не хватает бюджета для покрытия расходов

    return months

money_capital = 100000  # Примерная подушка безопасности
salary = 30000          # Ежемесячная зарплата
spend = 35000           # Ежемесячные расходы

months = months_until_debt(money_capital, salary, spend)

print(f"Количество месяцев, которое можно протянуть без долгов: {months}")
