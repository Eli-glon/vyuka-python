vstup = input("Zadej svůj věk: ")
vek = int(vstup)
if vek >= 65:
    print("Jsi důchodec")
elif vek >= 18:
    print("Jsi dospělý")#obráceně to spadne do první podmínky - do druhý se to nikdy nedostane
    print("Je ti: "+str(vek))
else: 
    print("Jsi dítě")
    print("Do dospělosti ti chybí: " + str(18-vek) + " let")# chybi=18-vek     print(f"do dospělosti ti chybí: {chybi} let")


    if vek >= 18:
        print("Jsi dospělý")
        print("Je ti: " + str(vek))
    elif vek >= 65:
        print("Jsi důchodce")
    else:
        print ("jsi dítě")
        zbyva=18-vek
        if zbyva == 1: #musí být 2 == protože je to číslo, ne string
            print("Do dospělosti ti chybí: " + str(zbyva) + " rok")
        elif 1 < zbyva < 5:
            print(" Do dospělosti ti zbývý: " + str(zbyva) + "roky")
        else:
            print("Do dospělosti ti zbývá: "+str(zbyva) + "let")

    