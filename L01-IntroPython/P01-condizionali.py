n = int( input("dammi un numero: ") )
if n > 10:
    print("maggiore di 10")
    n = n + 1
    print(n)
else:
    print("minore di 10")
    n = n - 1
    print(n)
print("end")