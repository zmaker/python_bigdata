
def saluta():
    print("ciao")
    
def somma(a, b):
    s = a + b
    return s

def modifica(m):
    return m + 10

def modl(ll):
    ll[0] = 100

def f2(*nomi):
    n = len(nomi)
    print("nomi: ", n)
    for n in nomi:
        print(n)

def saluta2(nome="Mario"):
    print ("ciao", nome)
    
def assetto(x, y, z):
    print(x, y, z)

saluta()
n = somma(10, 20)
print("1:", n)

modifica(n)
print("2:", n)

l = [1,2,3]
print("3:", l)
modl(l)
print("4:", l)

f2("Mario", "Luigi", "Anna")

saluta2()
saluta2("Luigi")

assetto(1,2,3)
assetto(z=23, y=12, x=0)

quadrato = lambda x : x*x
q = quadrato(2)
print(q)

fx = lambda x,y : x*y

def g():
    v = 0
    while True:
        yield v
        v += 1

gen = g()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

    
    
    

