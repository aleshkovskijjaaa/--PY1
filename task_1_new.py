import random
left_border = int(input("Введите левую границу отрезка: "))
right_border = int(input("Введите правую границу отрезка: "))
amount_of_numbers = int(input("Введите размер выходного списка"))
def get_unique_list_numbers() -> list[int]:
    spisok = [i for i in range(left_border, right_border, 1)]
    random.shuffle(spisok, random.random) #случайная последовательность чисел в списке
    random_values = spisok[:amount_of_numbers]
    return random_values
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
