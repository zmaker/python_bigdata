class Led:
    def __init__(self, col):
        self.colore = col
        self.stato = 0
    
    def __del__(self):
        print("distrutta!")
        
    def __str__(self):
        return f"Led: {self.colore} {self.stato}"
    
    def accendi(self):
        self.stato = 1
    
    def spegni(self):
        self.stato = 0
        
    def setColore(self, col):
        self.colore = col

led1 = Led("red")
led2 = Led("blu")

#led1.colore = "green"

print(led1.colore)
print(led2.colore)

led1.setColore("yellow")

led1.accendi()
print(led1)
led1.spegni()
print(led1)

del led1

    