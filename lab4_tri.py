def delete(list_, index=None):
    if index is None:
        index = -1
        return list_[:index]
    if index > 0 or index < 0:
        return list_[:index]+list_[index+1:]
    if abs(index) > len(list_):
        return list_
    #else:
        #return list_[:index]+list_[index+1:]
        
print(delete([0, 1, 1, 2, 3], index=-6)) #[0, 1, 1, 2, 3]
print(delete([0, 1, 1, 2, 3], index=-3)) #[0, 1, 2, 3]

print(delete([0, 1, 1, 2, 3], index=-2)) #[0, 1, 1, 3]
print(delete([0, 1, 1, 2, 3], index=6))  #[0, 1, 1, 2, 3]

# Сейчас все работает прекрасно
# Если значение модуля индекса больше чем дляна списка, выводитмя исходный список
