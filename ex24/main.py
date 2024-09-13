from funzioni import *
import os

def main():
    periodo = 3
    print(os.getcwd())

    dati = carica_dati("dati.txt")
    dati_red = riduci_dati(dati, periodo)
    dati_shift = scorri_dati(dati, periodo)

    variazioni = dati_shift - dati_red
    print(dati)
    print(dati_red)
    print(dati_shift)

    print(variazioni)

    print_stat(variazioni, dati)



if __name__ == "__main__":
    main()