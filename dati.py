def ierakstit(teksts):
    fails = open("teksts.txt", "w", encoding="utf-8") # r - read; w - write; a - append
    fails.write(teksts+"\n")
    fails.close()

ierakstit("hai")

def pierakstit_klat(teksts):
    fails = open("teksts.txt", "a", encoding="utf-8")
    fails.write(teksts+"\n")
    fails.close()

pierakstit_klat("meow")