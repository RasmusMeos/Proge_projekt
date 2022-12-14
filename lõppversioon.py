import random
import time

def mängu_käivitamine():
    seljakott = []
    while True:
        alusta = str(input("Tere tulemast aardejahi mängule! Kas soovid mängu alustada? (jah/ei): "))
        if alusta == "jah":
            aardemäng()
            mängi_uuesti()
            break
        elif alusta == "ei":
            print("Nägemist! Taaskäivita programm, kui soovid mängimist alustada.")
            break
        else:
            print("Sisend ei sobi. Palun vali uuesti.")
            
def aardemäng():
    
    seljakott = []
    kivi_paber_käärid()
    seljakott.append("münditasku")
    print("Liigud nüüd edasi") # teksti saab hiljem täiustada
    time.sleep(1)
    täringumäng()
    seljakott.append("salapärane kivim")
    time.sleep(5) #pikkem time sleep ennem mängija satub elukaga kokku
    #siia käib 1 vs 1 elukaga minimäng
    seljakott.append("kihv") #monster's tusk that can be used to locate the treasure on the magical map.
    time.sleep(1)
    trivia()
    seljakott.append("aardekaart")
    print("Sain nüüd kaarti katte! hakkasid otsima chest'i")
    time.sleep(3)
    chest() # dialoog chest mängus võib muuta hiljem ka


def kivi_paber_käärid():
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

def täringumäng():

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


def trivia():
   
   # 10 ? ja 8 peab olema õige et võita  Jah


    trivia_score=0
    trivia={
        'linn':'Tallinn',
        'vaba':'1918',
        'saar':'Saaremaa',
        'rekord':'-43,5',
        'juga':'30,5',
        'jõgi':'Võhandu',
        'mägi':'Suur Munamägi',
        'meri':'780',
        'arv':'2222'
        }

    print('Lõpuks jõudsid külla kus leijad üks vanatädi kes teab kuidas leida see varandus mis sa otsid, ')
    time.sleep(.5)
    print('ta ütleb sulle')
    time.sleep(.5)
    print('"Kui soovid varandus leida, on sul aardekaart vaja. \nKui saate 10-st küsimusest vähemalt 8 õigesti, ma annan seda sulle"')

    while trivia_score<11:
        üks=input('Mis on Eesti pealinn? ')
        if üks==trivia['linn']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if üks!=trivia['linn']:
            print('Valle!')

        kaks=input('Mis aastal kuulutati välja Eesti vabariik? ')
        if kaks==trivia['vaba']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if kaks!=trivia['vaba']:
            print('Valle!')

        kolm=input('Mis on Eestil kõige suurem saar? ')
        if kolm==trivia['saar']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if kolm!=trivia['saar']:
            print('Valle!')

        neli=input('Mis on Eestil kõige vanem linn? ')
        if neli==trivia['linn']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if neli!=trivia['linn']:
            print('Valle!')

        viis=input('Mis oli Eesti külmarekord? ')
        if viis==trivia['rekord']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if viis!=trivia['rekord']:
            print('Valle!')

        kuus=input('Mitu meetrit on kõige kõrgem juga Eestis? ')
        if kuus==trivia['juga']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if kuus!=trivia['juga']:
            print('Valle!')

        seitse=input('Mis on kõige pikem jõgi Eestis? ')
        if seitse==trivia['jõgi']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if seitse!=trivia['jõgi']:
            print('Valle!')

        kaheksa=input('Mis on Eesti kõige kõrgem mägi? ')
        if kaheksa==trivia['mägi']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if kaheksa!=trivia['mägi']:
            print('Valle!')

        üheksa=input('Mitu kilomeetrit pikk on Eesti merepiir? ')
        if üheksa==trivia['meri']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if üheksa!=trivia['meri']:
            print('Valle!')

        kümme=input('Mitu saart on Eestis? ')
        if kümme==trivia['arv']:
            trivia_score+=1
            print('Sa said õige vastus!')   
        if kümme!=trivia['arv']:
            print('Valle!')

        if trivia_score>7:
            print('"Noh nii, vastasid õigest... siin on sinu kaart nagu ma lubasin"')
            break
        if trivia_score<8:
            print('Ei läinud nii hästi kui oleks võinud...')
            time.sleep(.5)
            print('On veel arenguruumi... õpi rohkem Eesti kohta.')

def chest():
    luuk_skoor=0
    fail_count=0
    kood=[]
    kood.append(random.randint(1,3))
    kood.append(random.randint(1,3))
    kood.append(random.randint(1,3))

    print('Leidsid treasure chest!')
    time.sleep(.5)
    print('Aga chest on luukus')
    time.sleep(.5)
    print('luku kood on 3 numbrit')
    time.sleep(.5)
    print('saad lukku lahti ja oledki leidnud lõpp auhinna')
    time.sleep(.5)
    print('\n')*5

    while luuk_skoor<3 or fail_count<5:   
        if luuk_skoor == 0:
            valik=int(input('Vali number 1 läbi 3: '))
            if valik!=int(kood[0]):
                fail_count+=1
                print('Valisid vale number! Proovige uuesti!')
            if valik==int(kood[0]):
                luuk_skoor+=1
                print('Sa valisid õige number!')
        if luuk_skoor == 1:
            valik=int(input('Vali number 1 läbi 3: '))
            if valik!=int(kood[1]):
                fail_count+=1
                print('Valisid vale number! Proovige uuesti!')
            if valik==int(kood[1]):
                luuk_skoor+=1
                print('Sa valisid õige number!')
        if luuk_skoor == 2:
            valik=int(input('Vali number 1 läbi 3: '))
            if valik!=int(kood[2]):
                fail_count+=1
                print('Valisid vale number! Proovige uuesti!')
            if valik==int((kood[2])):
                luuk_skoor+=1
                print('Sa valisid õige number!')


    if luuk_skoor==3:
        print('Imeline! Said luuk lahti!')
    if luuk_skoor<3:
        print('kahjuks ei saanud luuk lahti, pead uuesti proovima')

def mängi_uuesti():
    while True:
        küsimus = str(input("Kas soovid uuesti mängida? (jah/ei): "))
        if küsimus == "jah":
            aardemäng()
        elif küsimus == "ei":
            print("Täname mängimast, järgmise korrani!")
            break
        else:
            print("Sisend ei sobi. Palun sisesta uuesti.")
            
mängu_käivitamine()