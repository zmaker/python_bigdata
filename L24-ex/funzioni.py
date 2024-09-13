import numpy as np

def carica_dati(filename):
    return np.genfromtxt(filename) 

def riduci_dati(dati, giorni):
    return dati[:-giorni+1]

def prt_stat(dati, dati_orig):
    min = np.amin(dati)
    max = np.amax(dati)
    print("delta min:", min)
    print("delta max:", max)
    #posizione del min
    p1 = np.where(dati==min)
    print(p1)
    print("idx min:", p1[0][0], "valore", dati_orig[p1[0][0]])


if __name__ == "__main__":
    print("non eseguibile!")