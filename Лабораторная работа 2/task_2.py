def calculate_safety_net(salary, spend, months, increase):
    total_shortage = 0
    for month in range(months):
        if month > 0:  # Расходы увеличиваются только со второго месяца
            spend *= (1 + increase)

        shortage = max(spend - salary, 0)  # Нехватка средств
        total_shortage += shortage

    return round(total_shortage)


# Пример использования
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев
increase = 0.03  # Ежемесячный рост цен

required_money_capital = calculate_safety_net(salary, spend, months, increase)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", required_money_capital)
