# liste

lista = [1,2,45,67,89,3]

tupla = (1,2,45,67,89,3)

s1 = {1,2,45,67,89,3}

for el in lista:
    print(el, end=' ')

print("\n")

for el in tupla:
    print(el, end=' ')

print("\n")

for el in s1:
    print(el, end=' ')

print("\n")

telefoni = {'mario':'213345', 'luigi':'324234'}
for k in telefoni.keys():
    print(k, end=' ')
    
print("\n")
for v in telefoni.values():
    print(v, end=' ')

print("\n")
for k in telefoni.keys():
    print(telefoni[k], end=' ')

