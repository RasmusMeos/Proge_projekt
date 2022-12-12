import random

nimi=input("Mis sinu nimi on? ")
print(f"Tere tulemast {nimi}!")
print()
info=input("Kas soovid mängu infot lugeda('Jah' või 'Ei')? ")
if info == "Ei":
    print()
if info == "Jah":
    print(" insert mängu info ")


score = 0
#health = 100

if score == 0:
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
                mängija_skoor += mängija_tulemus
                arvuti_skoor += arvuti_tulemus
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
                
            if (mängija_skoor >= maksimum_punktid) or (arvuti_skoor >= maksimum_punktid) and mängija_skoor > arvuti_skoor:
                print("Hästi tehtud! Said arvutist enne 30 silma kokku ning seega kuulub mänguvõit sulle!")
                print("Lõpptulemuseks jäi",mängija_skoor,"silma teile ja",arvuti_skoor,"silma arvutile.")
                break
            elif (mängija_skoor >= maksimum_punktid  or arvuti_skoor >= maksimum_punktid) and mängija_skoor < arvuti_skoor:
                mängija_skoor = 0
                arvuti_skoor = 0
                print("Lõpptulemuseks jäi",mängija_skoor,"silma teile ja",arvuti_skoor,"silma arvutile.")
                print("Proovige uuesti! Arvuti sai teist enne 30 silma kokku.")
                
                
score = 1

if score == 1:
    võimalused = ["kivi", "paber", "käärid"]
    mängude_arv = 5
    võite_vaja = 3

    mäs = 0  # mängija võite
    ars = 0  # arvuti võite
    print("Järgmiseks ülesandeks on võita kolme võiduni kestev kivi-paber-käärid seeria. Võidu puhul teenid oma skoorile lisapunkti ja saad liikuda järgmise ülesandeni.")
    
    while True:
        mängija_valik = input("Vali kas kivi, paber või käärid: ")
        arvuti_valik = random.choice(võimalused)

        if mängija_valik == arvuti_valik:
            print("Tegid arvutiga sama valiku. Te jäite viiki!")
            print("Seis on", mäs, ":", ars)

        elif mängija_valik == "kivi" and arvuti_valik == "paber":
            ars += 1
            print("Paber katab kivi - arvuti võit!")
            print("Seis on", mäs, ":", ars)
        elif mängija_valik == "kivi" and arvuti_valik == "käärid":
            mäs += 1
            print("Kivi lõhub käärid - sinu võit!")
            print("Seis on", mäs, ":", ars)

        elif mängija_valik == "käärid" and arvuti_valik == "paber":
            mäs += 1
            print("Käärid lõikavad paberi - sinu võit!")
            print("Seis on", mäs, ":", ars)
        elif mängija_valik == "käärid" and arvuti_valik == "kivi":
            ars += 1
            print("Kivi lõhub käärid - arvuti võit!")
            print("Seis on", mäs, ":", ars)

        elif mängija_valik == "paber" and arvuti_valik == "kivi":
            mäs += 1
            print("Paber katab kivi - sinu võit!")
            print("Seis on", mäs, ":", ars)
        elif mängija_valik == "paber" and arvuti_valik == "käärid":
            ars += 1
            print("Käärid lõikavad paberi - arvuti võit!")
            print("Seis on", mäs, ":", ars)

        if (mäs == võite_vaja or ars == võite_vaja) and mäs > ars:
            print("Õnnitlused, oled võitnud kolme võiduni mängitava seeria!")
            print("Lõppseis jäi:", mäs, ":", ars)
            break

        elif (mäs == võite_vaja or ars == võite_vaja) and mäs < ars:
            print("Proovi uuesti! Arvuti võitis selle kolme võiduni mängitava seeria.")
            print("Lõppseis jäi:", mäs, ":", ars)
            mäs = 0
            ars = 0
            
score = 2

if score == 2:
    trivia_score=0
    trivia={
        'linn':'Tallinn',
        'vaba':'1918',
        'saar':'Saaremaa',
        'rekord':'-43.5',
        'juga':'30,5',
        'jõgi':'Võhandu',
        'mägi':'Suur Munamägi',
        'meri':'780',
        'arv':'2222'
        }
    print('Oled joudnud Eesti kohta Trivia mängu! Kui saate 10-st küsimusest vähemalt 8 õigesti, oled sa võitnud.')

    while trivia_score<11:
        üks=input('Mis on Eesti pealinn? ')
        if üks==trivia['linn']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if üks!=trivia['linn']:
            print('Valle vastus :(')

        kaks=input('Mis aastal kuulutati välja Eesti vabariik? ')
        if kaks==trivia['vaba']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if kaks!=trivia['vaba']:
            print('Valle vastus :(')

        kolm=input('Mis on Eestil kõige suurem saar? ')
        if kolm==trivia['saar']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if kolm!=trivia['saar']:
            print('Valle vastus :(')

        neli=input('Mis on Eestil kõige vanem linn? ')
        if neli==trivia['linn']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if neli!=trivia['linn']:
            print('Valle vastus :(')

        viis=input('Mis oli Eestil külmarekord? ')
        if viis==trivia['rekord']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if viis!=trivia['rekord']:
            print('Valle vastus :(')

        kuus=input('Mitu meetrit on kõige kõrgem juga Eestis? ')
        if kuus==trivia['juga']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if kuus!=trivia['juga']:
            print('Valle vastus :(')

        seitse=input('Mis on kõige pikem jõgi Eestis? ')
        if seitse==trivia['jõgi']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if seitse!=trivia['jõgi']:
            print('Valle vastus :(')

        kaheksa=input('Mis on Eesti kõige kõrgem mägi? ')
        if kaheksa==trivia['mägi']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if kaheksa!=trivia['mägi']:
            print('Valle vastus :(')

        üheksa=input('Kui pikk on Eesti merepiir? ')
        if üheksa==trivia['meri']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if üheksa!=trivia['meri']:
            print('Valle vastus :(')

        kümme=input('Mitu saart on Eestis? ')
        if kümme==trivia['arv']:
            trivia_score+=1
            print('Sa said õige vastus!')   
        if kümme!=trivia['arv']:
            print('Valle vastus :(')

        if trivia_score>7:
            print('Sa oled Trivia Pro :D Seekord oled võitja!')
            print('Nüüd edasi viimase mängu')
            break
        if trivia_score<8:
            print('Ei läinud nii hästi kui oleks võinud...\nOn veel arenguruumi... õpi rohkem Eesti kohta.')

score = 3

if score == 3:
    score=4 # <- annab error et indent on vaja siis pannin lihtsalt score on 4 et saada errorist lahti
    # siia eelviimane mäng

score = 4

if score == 4:
    skoor = 0
    fail_count = 0
    print("""Sattusid ukse taha, aga luuk on ukse ees! \nluku kood on 3 numbrit \nsaad lukku lahti ja oledki valjas!""")

    while skoor < 3 and fail_count != 5:
        valik = input('Vali number 1 kuni 3: ')
        arvut = random.randint(1, 3)
        if valik == arvut:
            skoor += 1
            print('WooHoo! Sa valisid samma number kui arvuti')
            print('Sul on nüüd', skoor, 'punkti')
        if valik != arvut:
            fail_count += 1
            print('oh man! Arvut oli valinud teine number!')
            print('See kord ei saa punkti :(')

        if skoor == 3:
            print('Sa oled võitja! :)')
            print("Jõudsid edukalt lõppu!")
            break
        if skoor < 3:
            print('Kahjuks oled kaotunud :(')
            print("Tuleb uuesti proovida.")
