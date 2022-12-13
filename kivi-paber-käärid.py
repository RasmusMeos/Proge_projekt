
                    


võimalused = ["kivi", "paber","käärid"]
mängude_arv = 5
võite_vaja = 3

mäs = 0 # mängija võite
ars = 0 #arvuti võite

while True:
    mängija_valik = input("Vali kas kivi, paber või käärid: ")
    arvuti_valik = random.choice(võimalused)

    if mängija_valik == arvuti_valik:
        print("Tegid arvutiga sama valiku. Te jäite viiki!")
        print("Seis on",mäs,":",ars)

    elif mängija_valik == "kivi" and arvuti_valik == "paber":
        ars += 1
        print("Paber katab kivi - arvuti võit!")
        print("Seis on",mäs,":",ars)
    elif mängija_valik == "kivi" and arvuti_valik == "käärid":
        mäs += 1
        print("Kivi lõhub käärid - sinu võit!")
        print("Seis on",mäs,":",ars)
    
    elif mängija_valik == "käärid" and arvuti_valik == "paber":
        mäs += 1
        print("Käärid lõikavad paberi - sinu võit!")
        print("Seis on",mäs,":",ars)
    elif mängija_valik == "käärid" and arvuti_valik == "kivi":
        ars += 1
        print("Kivi lõhub käärid - arvuti võit!")
        print("Seis on",mäs,":",ars)

    elif mängija_valik == "paber" and arvuti_valik == "kivi":
        mäs += 1
        print("Paber katab kivi - sinu võit!")
        print("Seis on",mäs,":",ars)
    elif mängija_valik == "paber" and arvuti_valik == "käärid":
        ars += 1
        print("Käärid lõikavad paberi - arvuti võit!")
        print("Seis on",mäs,":",ars)

    if (mäs == võite_vaja or ars == võite_vaja) and mäs > ars:
        print("Õnnitlused, oled võitnud kolme võiduni mängitava seeria!")
        print("Lõppseis jäi:",mäs,":",ars)
        break
    elif (mäs == võite_vaja or ars == võite_vaja) and mäs < ars:
        print("Proovi uuesti! Arvuti võitis selle kolme võiduni mängitava seeria.")
        print("Lõppseis jäi:",mäs,":",ars)
        mäs = 0
        ars = 0

#if mäs > ars:
 #   print("Õnnitlused, oled võitnud kolme võiduni mängitava seeria!")
  #  print("Lõppseis jäi:",mäs,":",ars)
#else:
#    print("Proovi uuesti! Arvuti võitis selle kolme võiduni mängitava seeria.")





    # import random

# ars = 0 # arvuti skoor
# mäs = 0 # mängija skoor
# while True:

#     mängija_valik = input("Vali kas kivi, paber või käärid: ")
#     võimalused = ["kivi", "paber", "käärid"]
#     arvuti_valik = random.choice(võimalused)

#     print("Sinu valik: "+mängija_valik)
#     print("Arvuti valik: "+arvuti_valik)
    

#     if mängija_valik == arvuti_valik:
#         print("Tegid arvutiga sama valiku. Te jäite viiki!")
#         print("Seis on",mäs,":",ars)

#     elif mängija_valik == "kivi":
#         if arvuti_valik == "käärid":
#             mäs += 1
#             print("Kivi lõhub käärid - sinu võit!")
#             print("Seis on",mäs,":",ars)
#         else: 
#             ars += 1
#             print("Paber katab kivi - arvuti võit!")
#             print("Seis on",mäs,":",ars)
            

        
#     elif mängija_valik == "paber":
#         if arvuti_valik == "kivi":
#             mäs += 1
#             print("Paber katab kivi - sinu võit!")
#             print("Seis on",mäs,":",ars)
#         else:
#             ars += 1
#             print("Käärid lõikavad paberi - arvuti võit!")
#             print("Seis on",mäs,":",ars)
            
            
#     elif mängija_valik == "käärid":
#         if arvuti_valik == "paber":
#             mäs += 1
#             print("Käärid lõikavad paberi - sinu võit!")
#             print("Seis on",mäs,":",ars)
#         else:
#             ars += 1
#             print("Kivi lõhub käärid - arvuti võit!")
#             print("Seis on",mäs,":",ars)


    


            
   
        

