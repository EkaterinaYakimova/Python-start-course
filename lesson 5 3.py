with open('salary.txt', 'r', encoding='utf-8') as my_file:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in my_file}
    print(employees_dict)
    poor = [e[0] for e in employees_dict.items() if e[1] < 20000]
    print('Зарплата меньше 20 тыс', poor)
    average_salary = sum(employees_dict.values()) / len(employees_dict)
    print('Средняя зарплата', average_salary)



