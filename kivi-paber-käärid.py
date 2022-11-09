import random

while True:

    mängija_valik = input("Vali kas kivi, paber või käärid: ")
    võimalused = ["kivi", "paber", "käärid"]
    arvuti_valik = random.choice(võimalused)

    print("Sinu valik: "+mängija_valik)
    print("Arvuti valik: "+arvuti_valik)
    

    if mängija_valik == arvuti_valik:
        print("Tegid arvutiga sama valiku. Te jäite viiki!")
        
    elif mängija_valik == "kivi":
        if arvuti_valik == "käärid":
            print("Kivi lõhub käärid - sinu võit!")
        else: print("Paber katab kivi - arvuti võit!")
        
    elif mängija_valik == "paber":
        if arvuti_valik == "kivi":
            print("Paber katab kivi - sinu võit!")
        else:
            print("Käärid lõikavad paberi - arvuti võit!")
            
    elif mängija_valik == "käärid":
        if arvuti_valik == "paber":
            print("Käärid lõikavad paberi - sinu võit!")
        else:
            print("Kivi lõhub käärid - arvuti võit!")
            
    mängi_uuesti = input("Kas soovid veel mängida?: (jah/ei): ")
    if mängi_uuesti != "jah":
        break
        
