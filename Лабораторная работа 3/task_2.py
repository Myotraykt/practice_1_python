def find_common_participants(group1, group2, separator=','):
    participants_set1 = set(group1.split(separator))
    participants_set2 = set(group2.split(separator))

    common_participants = participants_set1 & participants_set2

    return list(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print("Общие участники:", common_participants)

participants_first_group_csv = "Иванов,Петров,Сидоров"
participants_second_group_csv = "Петров,Сидоров,Смирнов"
common_participants_csv = find_common_participants(participants_first_group_csv, participants_second_group_csv)
print("Общие участники (с запятой):", common_participants_csv)
