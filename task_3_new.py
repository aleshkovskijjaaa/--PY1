import random
def get_random_password() -> str:
    big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lit_letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    summ = ''.join((big_letters, lit_letters, numbers)) #объединение трех строк в одну
    a = random.sample(summ, 8)
    itog = (''.join(a))
    return itog
print(get_random_password())
