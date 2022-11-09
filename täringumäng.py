import random


mängija_skoor = 0
arvuti_skoor = 0
maksimum_punktid = 30
täringu_küljed = [1,2,3,4,5,6]
print("Selle teekonna alguses oled sattunud täringumängu laua taha. Ülesandeks on rinda pista arvutiga ning visata täringuid. \nKui saad enne arvutit 30 silma täis, oled mängu võitnud ning sinu skoorile lisandub 1. Seejärel saad edasi liikuda.")

while True:

        mängija_tulemus = random.choice(täringu_küljed)
        arvuti_tulemus = random.choice(täringu_küljed)
        veereta = input("Sisesta Enter, et veeretada täringut: ")
        if veereta == "":
            print("Sina veeretasid:",mängija_tulemus)
            print("Arvuti veeretas:",arvuti_tulemus)


            if mängija_tulemus == arvuti_tulemus:
                print("Viskasite sellel korral arvutiga sama arvu silmi.")
                print("Teil on vaja visata veel",maksimum_punktid-mängija_skoor,"silma ja arvutil on vaja vistata veel",maksimum_punktid-arvuti_skoor,"silma.")
            elif mängija_tulemus < arvuti_tulemus:
                mängija_skoor += mängija_tulemus
                arvuti_skoor += arvuti_tulemus
                print("Arvuti võitis selle korra visates teist rohkem silmi.")
                print("Teil on vaja visata veel",maksimum_punktid-mängija_skoor,"silma ja arvutil on vaja vistata veel",maksimum_punktid-arvuti_skoor,"silma.")
            elif mängija_tulemus > arvuti_tulemus:
                mängija_skoor += mängija_tulemus
                arvuti_skoor += arvuti_tulemus
                print("Võitsite selle korra, sest viskasite arvutist rohkem silmi.")
                print("Teil on vaja visata veel",maksimum_punktid-mängija_skoor,"silma ja arvutil on vaja vistata veel",maksimum_punktid-arvuti_skoor,"silma.")
                
            if ((mängija_skoor == maksimum_punktid or mängija_skoor > maksimum_punktid) or (arvuti_skoor == maksimum_punktid or arvuti_skoor > maksimum_punktid)) and mängija_skoor > arvuti_skoor:
                print("Hästi tehtud! Said arvutist enne 30 silma kokku ning seega kuulub mänguvõit sulle!")
                print("Lõpptulemuseks jäi",mängija_skoor,"silma teile ja",arvuti_skoor,"silma arvutile.")
                #score == 1
                break
            elif ((mängija_skoor == maksimum_punktid or mängija_skoor > maksimum_punktid) or (arvuti_skoor == maksimum_punktid or arvuti_skoor > maksimum_punktid)) and mängija_skoor > arvuti_skoor and mängija_skoor < arvuti_skoor:
                print("Lõpptulemuseks jäi",mängija_skoor,"silma teile ja",arvuti_skoor,"silma arvutile.")
                print("Proovige uuesti! Arvuti sai teist enne 30 silma kokku.")
                

            

