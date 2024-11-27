def months_until_debt(money_capital, salary, spend):
    months = 0

    # Вычисляем, сколько месяцев можно продержаться, учитывая увеличение расходов
    while money_capital >= 0:
        # Обновляем расходы на 5%
        spend *= 1.05

        # Рассчитываем, сколько денег останется после покрытия расходов
        money_capital += salary - spend

        # Увеличиваем количество месяцев
        months += 1

    return months  # Уменьшаем на 1, так как последний месяц некорректен


money_capital = 100000  # Примерная подушка безопасности
salary = 30000  # Ежемесячная зарплата
spend = 35000  # Ежемесячные расходы

months = months_until_debt(money_capital, salary, spend)

print(f"Количество месяцев, которое можно протянуть без долгов: {months}")
