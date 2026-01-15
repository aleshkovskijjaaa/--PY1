list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
maxi = max(list_numbers)
index_max = list_numbers.index(maxi)     #Индекс максимального элемента
index_last = list_numbers.index(25)  #Индекс последнего элемента

list_numbers[index_max], list_numbers[index_last] = list_numbers[index_last], list_numbers[index_max]




print(list_numbers)
