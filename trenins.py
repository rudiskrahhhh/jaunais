def rezultats(sk1, sk2):
    if sk1<6 and sk2<6:
        rez = sk1*sk2
    else:
        rez = sk1+sk2
        return rez


for skaitlis in range(1,11, 2): 
    for otrs in range(2,11):
        print("mūsu skaitlis:", skaitlis, "rezultāts:", rezultats(4, skaitlis))


def zvaigznites(skaits):
    for rindasNr in range(1, skaits+1):
        for zvaigzne in range(rindasNr):

        print("*")


skaitlis1 = 7
skaitlis2 = 3

print("pirmais skaitlis:", skaitlis1, "otrais skaitlis:", skaitlis2, "summa:", summa(skaitlis1,skaitlis2))

pirmais = "6"

print(pirmais)

vards2 = "Nē"

print(pirmais, vards2)

