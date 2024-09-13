import os
import numpy as np
from funzioni import *

def main():    
    periodo = 3
    cwd = os.getcwd()
    print("dir corrente:", cwd)
    dati = carica_dati("./L24-ex/valori.txt")
    print("dati", dati)

    #riduco i dati a seconda del periodo scelto
    dati_red = riduci_dati(dati, periodo)
    print("dati ridotti", dati_red, dati_red.size)
    
    #creo un array "shiftato"
    dati_shift = dati[periodo-1:]
    print("dati shiftati", dati_shift, dati_shift.size)

    #calcolo le variazioni (delta)
    variazioni = dati_shift - dati_red
    print(variazioni)

    #stampa statistiche
    prt_stat(variazioni, dati)

if __name__ == "__main__":
    main()