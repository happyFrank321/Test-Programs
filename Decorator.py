def cache_args(func): # декоратор
    _cash={} # создаем пустой лист, в котором будут храниться ранее вычиссленные чилса

    def return_number(num): #метод для поиска или вычисления чисел
        
        if num in _cash.keys(): # Сканируем список на поиск соответсвий

            return _cash[num] # Если оно есть, то возвращаем его

        else:
            
            _cash[num] = func(num) # Если числа нет, то обрабатывается функция подсчета
            return _cash[num]
            
    return return_number # вызов метода


@cache_args
def long_heavy(num):
     print(f"Долго и сложно {num}")
     return num**num


print(long_heavy(1))
print(long_heavy(1))
print(long_heavy(3))
print(long_heavy(2))
print(long_heavy(2))
print(long_heavy(3))