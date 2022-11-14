import random
def get_unique_list_numbers() -> list[int]:
    spisok = [i for i in range(-10, 11, 1)] #список с числами от -10 до 10
    random.shuffle(spisok, random.random) #случайная последовательность чисел в списке
    random_values = spisok[:15]
    return random_values

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
