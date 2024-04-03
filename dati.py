def ierakstit(teksts):
    fails = open("teksts.txt", "w", encoding="utf-8") # r - read; w - write; a - append
    fails.write(teksts+"\n")
    fails.close()

ierakstit("hai")

def pierakstit_klat(teksts):
    fails = open("teksts.txt", "a", encoding="utf-8")
    fails.write(teksts+"\n")
    fails.close()

    return

pierakstit_klat("meow")

def nolasit_visu():
    fails = open("teksts.txt", "r", encoding="utf-8")
    teksts = fails.read()
    return teksts

print(nolasit_visu())

def dabut_rindinas():
    fails = open("teksts.txt", "r", encoding="utf-8")
    rindas = fails.readlines()

    for i in range(len(rindas)):
        rindas[i] = rindas[i].strip()

    return rindas

saraksts = dabut_rindinas()
for i in range(len(saraksts)):
    saraksts[i] = saraksts[i].strip()
print(saraksts)

ierakstit("rudis", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/da12389f-0da6-4412-82ca-d32a2fbfdcc1/d2jb2cz-aa9e6968-d2ac-4206-837f-3a2f1c1688f3.jpg/v1/fill/w_900,h_675,q_75,strp/fat_ass_cat_2_by_pyro_boyxyz13_d2jb2cz-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9Njc1IiwicGF0aCI6IlwvZlwvZGExMjM4OWYtMGRhNi00NDEyLTgyY2EtZDMyYTJmYmZkY2MxXC9kMmpiMmN6LWFhOWU2OTY4LWQyYWMtNDIwNi04MzdmLTNhMmYxYzE2ODhmMy5qcGciLCJ3aWR0aCI6Ijw9OTAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.NJPtRDZjyRD0BOpC5mZevjhZKdll7AzqNmEUDy66wOo")
pierakstit_klat("roberts", "https://t4.ftcdn.net/jpg/03/60/70/11/360_F_360701167_9dolp6h5cfm5i9uC8QObRzhog1mc1gI0.jpg")
pierakstit_klat("janis", "https://i.ytimg.com/vi/pVbtFP40E50/maxresdefault.jpg")