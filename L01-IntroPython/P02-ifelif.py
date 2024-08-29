voto = int( input("dammi un voto (1 a 10): ") )
if voto >= 8:
    print("ottimo")
elif voto >= 6:
    print("suff")
elif voto >= 5:
    print("insuff")
else:
    print("grav insuff")