import random

        
mängija_skoor = 0
arvuti_skoor = 0
maksimum_punktid = 21
täringu_küljed = [1,2,3,4,5,6]
print("Selle teekonna alguses oled sattunud täringumängu laua taha. Ülesandeks on rinda pista arvutiga ning visata täringuid. \nKui saad enne arvutit 21 silma täis, oled mängu võitnud ning sinu skoorile lisandub 1. Seejärel saad edasi liikuda.")

while True:
    
    mängija_tulemus = random.choice(täringu_küljed)
    arvuti_tulemus = random.choice(täringu_küljed)
    veereta = input("Sisesta Enter, et veeretada täringut: ")
    if veereta == "":
        print("Sina veeretasid:",mängija_tulemus)
        print("Arvuti veeretas:",arvuti_tulemus)


        if mängija_tulemus == arvuti_tulemus:
            mängija_skoor += mängija_tulemus
            arvuti_skoor += arvuti_tulemus
            if mängija_skoor < maksimum_punktid and arvuti_skoor < maksimum_punktid:
                print("Teil on vaja visata veel",maksimum_punktid-mängija_skoor,"silma ja arvutil on vaja vistata veel",maksimum_punktid-arvuti_skoor,"silma.")
            elif mängija_skoor < maksimum_punktid and arvuti_skoor > maksimum_punktid:
                print("Teil on vaja visata veel",maksimum_punktid-mängija_skoor,"silma, aga arvuti läks lõhki! Tal tuleb uuesti alustada.")
            elif mängija_skoor > maksimum_punktid and arvuti_skoor < maksimum_punktid:
                print("Läksite lõhki ja teil tuleb uuesti alustada! Arvutil vaja visata veel", maksimum_punktid-arvuti_skoor, "silma.")
            elif mängija_skoor > maksimum_punktid and arvuti_skoor > maksimum_punktid:
                print("Läksite mõlemad lõhki ning teil tuleb uuesti alustada!")
                
                
        elif mängija_tulemus < arvuti_tulemus:
            mängija_skoor += mängija_tulemus
            arvuti_skoor += arvuti_tulemus
            if mängija_skoor < maksimum_punktid and arvuti_skoor < maksimum_punktid:
                print("Teil on vaja visata veel",maksimum_punktid-mängija_skoor,"silma ja arvutil on vaja vistata veel",maksimum_punktid-arvuti_skoor,"silma.")
            elif mängija_skoor < maksimum_punktid and arvuti_skoor > maksimum_punktid:
                print("Teil on vaja visata veel",maksimum_punktid-mängija_skoor,"silma, aga arvuti läks lõhki! Tal tuleb uuesti alustada.")
            elif mängija_skoor > maksimum_punktid and arvuti_skoor < maksimum_punktid:
                print("Läksite lõhki ja teil tuleb uuesti alustada! Arvutil vaja visata veel", maksimum_punktid-arvuti_skoor, "silma.")
            elif mängija_skoor > maksimum_punktid and arvuti_skoor > maksimum_punktid:
                print("Läksite mõlemad lõhki ning teil tuleb uuesti alustada!")
                

        elif mängija_tulemus > arvuti_tulemus:
            mängija_skoor += mängija_tulemus
            arvuti_skoor += arvuti_tulemus
            if mängija_skoor < maksimum_punktid and arvuti_skoor < maksimum_punktid:
                print("Teil on vaja visata veel",maksimum_punktid-mängija_skoor,"silma ja arvutil on vaja vistata veel",maksimum_punktid-arvuti_skoor,"silma.")
            elif mängija_skoor < maksimum_punktid and arvuti_skoor > maksimum_punktid:
                print("Teil on vaja visata veel",maksimum_punktid-mängija_skoor,"silma, aga arvuti läks lõhki! Tal tuleb uuesti alustada.")
            elif mängija_skoor > maksimum_punktid and arvuti_skoor < maksimum_punktid:
                print("Läksite lõhki ja teil tuleb uuesti alustada! Arvutil vaja visata veel", maksimum_punktid-arvuti_skoor, "silma.")
            elif mängija_skoor > maksimum_punktid and arvuti_skoor > maksimum_punktid:
                print("Läksite mõlemad lõhki ning teil tuleb uuesti alustada!")
                

            
        if mängija_skoor > maksimum_punktid:
            mängija_skoor = 0
            
        if arvuti_skoor > maksimum_punktid:
            arvuti_skoor = 0           
        
        if mängija_skoor == maksimum_punktid and arvuti_tulemus != maksimum_punktid:
            print("Hästi tehtud! Said arvutist enne täpselt 21 silma kokku ning seega kuulub mänguvõit sulle!")
            print("Lõpptulemuseks jäi",mängija_skoor,"silma teile ja",arvuti_skoor,"silma arvutile.")
            break
        if mängija_skoor != maksimum_punktid and arvuti_tulemus == maksimum_punktid:
            mängija_skoor = 0
            arvuti_skoor = 0
            print("Lõpptulemuseks jäi",mängija_skoor,"silma teile ja",arvuti_skoor,"silma arvutile.")
            print("Proovige uuesti! Arvuti sai teist enne täpselt 21 silma kokku.")
        if mängija_skoor == maksimum_punktid and arvuti_tulemus == maksimum_punktid:
            mängija_skoor = 0
            arvuti_skoor = 0
            print("Ime, te jäite viiki! Kahjuks tuleb siiski mäng võita.")
            
            

        
            
            
#         if (mängija_skoor >= maksimum_punktid) or (arvuti_skoor >= maksimum_punktid) and mängija_skoor > arvuti_skoor:
#             print("Hästi tehtud! Said arvutist enne 30 silma kokku ning seega kuulub mänguvõit sulle!")
#             print("Lõpptulemuseks jäi",mängija_skoor,"silma teile ja",arvuti_skoor,"silma arvutile.")
#             break
#         elif (mängija_skoor >= maksimum_punktid  or arvuti_skoor >= maksimum_punktid) and mängija_skoor < arvuti_skoor:
#             mängija_skoor = 0
#             arvuti_skoor = 0
#             print("Lõpptulemuseks jäi",mängija_skoor,"silma teile ja",arvuti_skoor,"silma arvutile.")
#             print("Proovige uuesti! Arvuti sai teist enne 30 silma kokku.")                

            


