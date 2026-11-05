vstup = input("Zadej něco: ")

print(vstup)
print(type(vstup)) # input je vždy string, takže musím převést na int


vstup1=input("Zadej číslo: ") #když napíšu slovo - vyhodí chybu když se to bude snažit převést na číslo
vstup2=input("Zadej číslo: ")# když budu chtít desetiný čistla místo int musím použít float, protože int neumí desetiný čísla

print(type(vstup1)) #toto je string, takže musím převést na int aby bylo číslo a mohl jsem s ním počítat
cislo1 = int(vstup1)
print(type(cislo1)) #tohle je už číslo
cislo2 = int(vstup2)
vysledek = cislo1 + cislo2
v=vstup1 + vstup2 

print("Součet je: " + str(v)) #tady to je string, takže sečte jako string, takže 1+1=11

print("Součet je: " + str(vysledek))#musime převést na string, protože jinak by to vyhodilo chybu (neumí se sčítat string a int) (nejlepší ze začátku)
print(f"Součet je: {vysledek}") #tady se to převede na string automaticky, takže nemusíme převádět na string (formátovaný string)
print("Součet je: {}".format(vysledek)) #tady se to převede na string automaticky, takže nemusíme převádět na string(jedlovo speciál)
