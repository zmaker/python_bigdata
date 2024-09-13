import numpy as np

def carica_dati(filename):
    return np.genfromtxt(filename)
    
def riduci_dati(dati, giorni):
    return dati[:-giorni+1]
    
def scorri_dati(dati, periodo):
    return dati[periodo-1:]

def print_stat(variazioni, dati):
    min = np.amin(dati)
    max = np.amax(dati)
    print("delta min:", min)
    print("delta max:", max)
    p1 = np.where(dati==min)
    print("idx del min: ", p1[0][0], "val: ", dati[p1[0][0]])


if __name__ == "__main__":
    print("monulo non eseguibile")
