# cicli for while

import random

n = 0
while not (n == 7):
    n = random.randint(0, 10)
    print(n, end=" ")
    
print("end");

print("while: ")
n = 0
while (n < 10):
    print(n, end=" ")
    n += 1
    
print("\nfor: ")
for n in range(0, 10):
    print(n, end=" ")
    
print("\nfor array: ")
numeri = [1,10,23,34,45,56]
for el in numeri:
    print(el, end=" ")
    
# break continue
print("\nfor + break: ")
for n in range(0, 10):
    if n == 5:
        break
    print(n, end=" ")
    
print("\nfor + continue: ")
for n in range(0, 10):
    if n == 5:
        continue
    print(n, end=" ")
