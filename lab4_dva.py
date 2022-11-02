def get_count_char(str_):
    s = str_.lower()
    dict_ = {}
    for i in s:
        if i.isalpha():
            if i in dict_.keys():
                dict_[i]+=1
            else:
                dict_[i] = 1
    return dict_


def persent(new_value):
    count = 0
    total = sum(new_value.values())  
    for key in new_value:
        new_value[key]= round((new_value[key]*100/total), 2) #округляем до двух знаков
        count += new_value[key]  
    if round(count) == 100:   #условие вывода
        return new_value

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(persent(get_count_char(main_str)))
