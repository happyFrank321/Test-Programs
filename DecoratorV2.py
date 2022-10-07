def cache_args(func):  # декоратор

    _cash = {} # создаем пустой хэш

    def return_number():  # метод для поиска или вычисления чисел

        if _cash=={}:
            
            _cash["first"] = func()
            _cash["secodn"] = _cash["first"]
            return  _cash["first"]
        
        else:
            
            _cash['secodn']+=1
            if _cash['secodn']>3:
                
                _cash["first"] = func()
                _cash["secodn"] = _cash["first"]
                print("Кэш забился, опять считать")
            return _cash["first"]

    
    return return_number  # вызов метода


@cache_args
def heavy():
    print("Cложные вычисления")
    return 1


print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
