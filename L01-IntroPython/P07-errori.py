str = 'abc'
try:
    n = int(str)
    print(n)
except ValueError as ve:
    print("errore")
    print(ve)
    
    
def elab(n):
    if n > 0:
        return n*10
    else:
        raise ValueError()

try: 
    elab(10/0)
except ValueError as ve:
    print("errore")
    print(ve)
except ZeroDivisionError:
    print("errore 0")
finally:
    pass

    