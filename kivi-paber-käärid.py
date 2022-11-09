import random

while True:

    mängija_valik = input("Vali kas kivi, paber või käärid: ")
    võimalused = ["kivi", "paber", "käärid"]
    arvuti_valik = random.choice(võimalused)

    ars = 0 # arvuti skoor
    mäs = 0 # mängija skoor

    print("Sinu valik: "+mängija_valik)
    print("Arvuti valik: "+arvuti_valik)
    

    if mängija_valik == arvuti_valik:
        print("Tegid arvutiga sama valiku. Te jäite viiki!")
        print("Seis on",mäs,":",ars)

    elif mängija_valik == "kivi":
        if arvuti_valik == "käärid":
            mäs += 1
            print("Kivi lõhub käärid - sinu võit!")
            print("Seis on",mäs,":",ars)
        else: 
            ars += 1
            print("Paber katab kivi - arvuti võit!")
            print("Seis on",mäs,":",ars)
            

        
    elif mängija_valik == "paber":
        if arvuti_valik == "kivi":
            mäs += 1
            print("Paber katab kivi - sinu võit!")
            print("Seis on",mäs,":",ars)
        else:
            ars += 1
            print("Käärid lõikavad paberi - arvuti võit!")
            print("Seis on",mäs,":",ars)
            
            
    elif mängija_valik == "käärid":
        if arvuti_valik == "paber":
            mäs += 1
            print("Käärid lõikavad paberi - sinu võit!")
            print("Seis on",mäs,":",ars)
        else:
            ars += 1
            print("Kivi lõhub käärid - arvuti võit!")
            print("Seis on",mäs,":",ars)

            
    #mängi_uuesti = input("Kas soovid veel mängida?: (jah/ei): ")
   # if mängi_uuesti != "jah":
      #  break
        
