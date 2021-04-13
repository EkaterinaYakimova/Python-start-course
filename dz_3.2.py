# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
name = input(' введите имя ')
surname = input('введите фамилию ')
year = int(input('введите год рождения '))
city = input('введите город проживания ')
email = input('введите email ')
telephone = input('введите телефон ')
def person_info(name, surname, year, city, email, telephone):
    result = f'{name} {surname},{year} года рождения проживает в городе {city},email - {email}, телефон - {telephone}'
    return result
print(person_info(name =name, surname =surname, year=year, city=city, email=email, telephone=telephone))