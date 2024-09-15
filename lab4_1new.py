def get_count_char(str_):
    s=str_.lower()
    dict = {}
    for i in s:
        if i.isalpha():
            if i in dict.keys():
                number = dict[i]
                number+=1
                dict[i] = number
            else:
                dict[i] = 1
    return dict

def persent(new_values):
    new_value = get_count_char(new_values) #берем значение из первой функции
    total = sum(new_value.values()) #сумма значений словаря из предыдущей функции (257)
    for key in new_value:
        new_value[key]/= total
        new_value[key]*=100 #переводим в проценты
        new_value[key] = round(new_value[key]) #округляем до одного знака после запятой
    return new_value

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(persent(main_str))
