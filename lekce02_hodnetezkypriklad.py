vstup1=input("Zadej první rozměr trojúhelníku: ")
vstup2=input("Zadej druhý rozměr trojúhelníku: " )
vstup3=input("Zadej třetí rozměr trojúhelníku: " )
a=float(vstup1)
b=float(vstup2)
c=float(vstup3)

if a+b>c and b+c>a and c+a>b:
    print("Tvůj trojúhelník je skonstruovatelný")
else:
    print("Tohle nenarýsuješ")