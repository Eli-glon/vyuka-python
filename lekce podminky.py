vek = 18
print ("Muj vek je: " + str(vek))
if vek >= 18:
    print("Jsem dospelý")
    print ("můžu chlastat")
elif vek >= 15:
    print("Jsem tělesně dospělý")
    print("můžu chlastat jenom když vypadam na 18")
else:
    print("Jsem dítě")
    print ("podle zákona nemůžu chlastat")
print ("tečka")




muj_vek = 18
if muj_vek >= 18: # když se nesplní jedem dál, když mám if a za ním další, tak jsou dvě různy podmínky (2if si spolu nepovídají)
    print("jsem dospělý")
if muj_vek >=65:
    print("dostávám peníze za to že krmím holuby")
else: 
    print("jsem mladý a zdravý")




if muj_vek >= 18: # IF mužu do sebe vnořit 
    print("jsem dospělý")
    if muj_vek >=65:
        print("dostávám peníze za to že krmím holuby")
    else:
        print("jsem mladý a zdravý") 
else:
    print("jsem dítě")