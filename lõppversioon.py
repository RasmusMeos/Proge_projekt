import random
import time

def mängu_käivitamine():
    seljakott = ["revolver", "nuga"]
    while True:
        alusta = str(input("Tere tulemast aardejahi mängule! Kas soovid mängu alustada? (jah/ei): "))
        time.sleep(2)
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
    print("Selles mängus oled sina, mängija, Eestis seiklev aardeotsija, kes otsib kadunud laegast, milles peitub suur rikkus!")
    time.sleep(2)
    print("Kõigepealt astud sa lähedal olevasse kõrtsi, et saada vihjeid aarde asukoha kohta...")
    time.sleep(2)
    print("Kõrtsi astudes näed laudasid, mille taga saab mängida erinevaid mänge.")
    print(""""Tere võõras! Tule mängime ühe kivi-paber-käärid mängu!" kostab esimese laua tagant.""" )
    time.sleep(2)
    print(""""Mul on sulle ka kuldmündi tasku, kui mind võidad!" Raha tuleb kindlasti kasuks - mängime!""")
    time.sleep(2)
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
    print("See kivi-paber-käärid mäng kestab kuni kolme võiduni. Kui võidame, saame kuldmünte. Kes teab, ehk läheb hiljem vaja... ")
    time.sleep(2)
    while True:
        mängija_valik = input("Vali kas kivi, paber või käärid: ")
        time.sleep(1)
        arvuti_valik = random.choice(võimalused)

        if mängija_valik == arvuti_valik:
            print("Tegid vastasega sama valiku. Te jäite viiki!")
            time.sleep(0.5)
            print("Seis on",mäs,":",ars)
            time.sleep(0.5)
            
        elif mängija_valik == "kivi" and arvuti_valik == "paber":
            ars += 1
            print("Paber katab kivi - vastase võit!")
            time.sleep(0.5)
            print("Seis on",mäs,":",ars)
            time.sleep(0.5)
            
        elif mängija_valik == "kivi" and arvuti_valik == "käärid":
            mäs += 1
            print("Kivi lõhub käärid - sinu võit!")
            time.sleep(0.5)
            print("Seis on",mäs,":",ars)
            time.sleep(0.5)
        
        elif mängija_valik == "käärid" and arvuti_valik == "paber":
            mäs += 1
            print("Käärid lõikavad paberi - sinu võit!")
            time.sleep(0.5)
            print("Seis on",mäs,":",ars)
            time.sleep(0.5)
            
        elif mängija_valik == "käärid" and arvuti_valik == "kivi":
            ars += 1
            print("Kivi lõhub käärid - vastase võit!")
            time.sleep(0.5)
            print("Seis on",mäs,":",ars)
            time.sleep(0.5)

        elif mängija_valik == "paber" and arvuti_valik == "kivi":
            mäs += 1
            print("Paber katab kivi - sinu võit!")
            time.sleep(0.5)
            print("Seis on",mäs,":",ars)
            time.sleep(0.5)
            
        elif mängija_valik == "paber" and arvuti_valik == "käärid":
            ars += 1
            print("Käärid lõikavad paberi - vastase võit!")
            time.sleep(0.5)
            print("Seis on",mäs,":",ars)
            time.sleep(0.5)

        if (mäs == võite_vaja or ars == võite_vaja) and mäs > ars:
            print("Õnnitlused, oled võitnud kolme võiduni mängitava seeria!")
            time.sleep(2)
            print("Lõppseis jäi:",mäs,":",ars)
            time.sleep(2)
            break
        
        elif (mäs == võite_vaja or ars == võite_vaja) and mäs < ars:
            print("Proovi uuesti! Vastane võitis selle kolme võiduni mängitava seeria.")
            time.sleep(2)
            print("Lõppseis jäi:",mäs,":",ars)
            time.sleep(2)
            mäs = 0
            ars = 0

def täringumäng():

    mängija_skoor = 0
    arvuti_skoor = 0
    maksimum_punktid = 21
    täringu_küljed = [1,2,3,4,5,6]
    print("Istume salapärase isiku laua taha. Viskame koos täringuid kuni üks meist saab enne täpselt 21 silma.")
    time.sleep(2)
    print("""Üle 21 silma visates lähed "lõhki" ja tuleb uuesti alustada.""")
    time.sleep(2)
    print("Kaotades tuleb taaskord uuesti mängida kuni oleme võidukad.")
    time.sleep(2)

    while True:
        
        mängija_tulemus = random.choice(täringu_küljed)
        arvuti_tulemus = random.choice(täringu_küljed)
        veereta = input("Sisesta Enter, et veeretada täringut: ")
        if veereta == "":
            print("Sina veeretasid:",mängija_tulemus)
            time.sleep(0.5)
            print("Tundmatu veeretas:",arvuti_tulemus)
            time.sleep(0.5)


            if mängija_tulemus == arvuti_tulemus:
                mängija_skoor += mängija_tulemus
                arvuti_skoor += arvuti_tulemus
                if mängija_skoor < maksimum_punktid and arvuti_skoor < maksimum_punktid:
                    print("Teil on vaja visata veel",maksimum_punktid-mängija_skoor,"silma ja tundmatul on vaja vistata veel",maksimum_punktid-arvuti_skoor,"silma.")
                    time.sleep(1)
                elif mängija_skoor < maksimum_punktid and arvuti_skoor > maksimum_punktid:
                    print("Teil on vaja visata veel",maksimum_punktid-mängija_skoor,"silma, aga tundmatu läks lõhki! Tal tuleb uuesti alustada.")
                    time.sleep(1)
                elif mängija_skoor > maksimum_punktid and arvuti_skoor < maksimum_punktid:
                    print("Läksite lõhki ja teil tuleb uuesti alustada! Tundmatul vaja visata veel", maksimum_punktid-arvuti_skoor, "silma.")
                    time.sleep(1)
                elif mängija_skoor > maksimum_punktid and arvuti_skoor > maksimum_punktid:
                    print("Läksite mõlemad lõhki ning teil tuleb uuesti alustada!")
                    time.sleep(1)
                    
                    
            elif mängija_tulemus < arvuti_tulemus:
                mängija_skoor += mängija_tulemus
                arvuti_skoor += arvuti_tulemus
                if mängija_skoor < maksimum_punktid and arvuti_skoor < maksimum_punktid:
                    print("Teil on vaja visata veel",maksimum_punktid-mängija_skoor,"silma ja tundmatul on vaja vistata veel",maksimum_punktid-arvuti_skoor,"silma.")
                    time.sleep(1)
                elif mängija_skoor < maksimum_punktid and arvuti_skoor > maksimum_punktid:
                    print("Teil on vaja visata veel",maksimum_punktid-mängija_skoor,"silma, aga tundmatu läks lõhki! Tal tuleb uuesti alustada.")
                    time.sleep(1)
                elif mängija_skoor > maksimum_punktid and arvuti_skoor < maksimum_punktid:
                    print("Läksite lõhki ja teil tuleb uuesti alustada! Tundmatul vaja visata veel", maksimum_punktid-arvuti_skoor, "silma.")
                    time.sleep(1)
                elif mängija_skoor > maksimum_punktid and arvuti_skoor > maksimum_punktid:
                    print("Läksite mõlemad lõhki ning teil tuleb uuesti alustada!")
                    time.sleep(1)
                    

            elif mängija_tulemus > arvuti_tulemus:
                mängija_skoor += mängija_tulemus
                arvuti_skoor += arvuti_tulemus
                if mängija_skoor < maksimum_punktid and arvuti_skoor < maksimum_punktid:
                    print("Teil on vaja visata veel",maksimum_punktid-mängija_skoor,"silma ja tundmatul on vaja vistata veel",maksimum_punktid-arvuti_skoor,"silma.")
                    time.sleep(1)
                elif mängija_skoor < maksimum_punktid and arvuti_skoor > maksimum_punktid:
                    print("Teil on vaja visata veel",maksimum_punktid-mängija_skoor,"silma, aga tundmatu läks lõhki! Tal tuleb uuesti alustada.")
                    time.sleep(1)
                elif mängija_skoor > maksimum_punktid and arvuti_skoor < maksimum_punktid:
                    print("Läksite lõhki ja teil tuleb uuesti alustada! Tundmatul vaja visata veel", maksimum_punktid-arvuti_skoor, "silma.")
                    time.sleep(1)
                elif mängija_skoor > maksimum_punktid and arvuti_skoor > maksimum_punktid:
                    print("Läksite mõlemad lõhki ning teil tuleb uuesti alustada!")
                    time.sleep(1)
                    

                
            if mängija_skoor > maksimum_punktid:
                mängija_skoor = 0
                
            if arvuti_skoor > maksimum_punktid:
                arvuti_skoor = 0           
            
            if mängija_skoor == maksimum_punktid and arvuti_tulemus != maksimum_punktid:
                print("Hästi tehtud! Said tundmatust enne täpselt 21 silma kokku ning seega kuulub mänguvõit sulle!")
                time.sleep(2)
                print("Lõpptulemuseks jäi",mängija_skoor,"silma teile ja",arvuti_skoor,"silma tundmatule.")
                time.sleep(2)
                break
            if mängija_skoor != maksimum_punktid and arvuti_tulemus == maksimum_punktid:
                mängija_skoor = 0
                arvuti_skoor = 0
                print("Lõpptulemuseks jäi",mängija_skoor,"silma teile ja",arvuti_skoor,"silma tundmatule.")
                time.sleep(2)
                print("Proovige uuesti! Tundmatu sai teist enne täpselt 21 silma kokku.")
                time.sleep(2)
            if mängija_skoor == maksimum_punktid and arvuti_tulemus == maksimum_punktid:
                mängija_skoor = 0
                arvuti_skoor = 0
                print("Ime, te jäite viiki! Kahjuks tuleb siiski mäng võita.")
                time.sleep(2)


def võitlus():
    
    libahunt_elud = 250
    hammusta = 10
    kriimusta = 5
    libahunt_rünnak = [hammusta, kriimusta]
    mängija_elud = 100
    tulista = 20
    noahoop = 5
    padruneid = 6
    tervenda = 75
    moona = 1
    print("Tee naaberkülani viib läbi paksu laane. Vahepeal on kätte jõudnud öö ning taevas särab täiskuu...")
    time.sleep(2)
    print("Järsku on kuulda tarduma panevat ulgumist ja seejärel möiret! Läbi paksu metsa hüppab teele libahunt!")
    time.sleep(2)
    print("Vöö pealt on võtta revolver ja nuga, millega end kaitsta. Moona jagub sul 12 lasuks, kusjuures revolver on juba 6 kuuliga valmis laetud.")
    time.sleep(3)
    print("Ennast saad ühe korra tervendada ka võlujoogiga, mis põues leidub. Ehk on abi ka kõrtsist saadud esemetest ;)")
    time.sleep(2)
    print("Libahundist tuleb jagu saada, vastasel juhul on lood kehvasti...")
    time.sleep(2)
    

    while libahunt_elud > 0 and mängija_elud > 0:
        tegevus = str(input("Vali sulgudes numbriga tegevus: lase revolvriga(1), torka noaga(2), tervenda ennast(3), lae revolvrit(4): "))
        rünnak = random.choices(libahunt_rünnak, weights=(30,70), k=1)
        if tegevus == "hõbekuul":
            libahunt_elud = 0
            print("Kasutasid revolvris hõbekuuli ning *põmm* - libahunt haarab rinnust ning langeb vaikselt. Oled tapnud libahundi!")
            time.sleep(1)
            break
        if tegevus == "1" and padruneid > 0 and (moona > 0 or moona == 0):
            libahunt_elud -= tulista
            padruneid -= 1
            print("Said libahundile pihta! Tal on alles veel",libahunt_elud,"punkti jagu elusid.")
            time.sleep(1)
        elif tegevus == "1" and padruneid == 0 and moona > 0:
            print("Revolvrist on kuulid otsas! Relv tegi ainult klõps, vaja laadida!")
            time.sleep(1)
        elif tegevus =="1" and padruneid == 0 and moona == 0:
            print("Revolvrist on kuulid otsas ja ka moon on otsas! Relv teeb vajutades klõps, sellest pole enam kasu!")
            time.sleep(1)
        if tegevus == "2":
            libahunt_elud -= noahoop
            print("Haavasid noaga libahunti! Tal on alles veel",libahunt_elud,"punkti jagu elusid.")
            time.sleep(1)
        if tegevus == "3" and tervenda == 75:
            mängija_elud += tervenda
            tervenda -= 75
            print("Jõid elu toovat võlujooki! Sul on nüüd", mängija_elud, "punkti jagu elusid.")
            time.sleep(1)
        elif tegevus == "3" and tervenda == 0:
            print("Haarasid taas võlujoogi järele, kuid pudel on tühi! Ennast ei õnnestunud tervendada.")
            time.sleep(1)
        if tegevus == "4" and padruneid == 0 and moona > 0:
            padruneid += 6
            moona -= 1
            print("Relv on laetud!")
            time.sleep(1)
        elif tegevus == "4" and padruneid > 0 and moona == 1:
            print("Relvas on veel kuule! Laadida saad, kui relv on tühi!")
            time.sleep(1)
        elif tegevus == "4" and padruneid > 0 and moona == 0:
            print("Moon on otsas! Lasta saad veel nii palju, kui revolvris kuule!")
            time.sleep(1)
        elif tegevus == "4" and padruneid == 0 and moona == 0:
            print("Moon on otsas, relva enam kasutada ei saa!")
            time.sleep(1)
        if rünnak[0] == 5 and libahunt_elud > 0:
            mängija_elud -= 5
            print("Libahunt kriimustas sind! Sul on nüüd", mängija_elud, "punkti jagu elusid.")
            time.sleep(1)
        elif rünnak[0] == 10 and libahunt_elud > 0:
            mängija_elud -= 10
            print("Sattusid libahundile liiga lähedale ja ta hammustas sind! Sul on nüüd", mängija_elud, "punkti jagu elusid.")
            time.sleep(1)
            
        if libahunt_elud <= 0 and mängija_elud > 0:
            print("Libahunt on nähtavalt kurnatud ja haavatud. Ta tuigerdab ja kukub selili! Oled tapnud libahundi!")
            time.sleep(2)
            break
        elif libahunt_elud > 0 and mängija_elud <= 0:
            print("Libahunt sai sinust jagu! See oli kõigest halb uni ning leiad end taas libahundi eest...")
            time.sleep(2)
            mängija_elud = 100
            libahunt_elud = 250
            padruneid = 0
            moona = 0
            padruneid = 6
            moona = 1







def trivia():
   
   # 10 ? ja 8 peab olema õige et võita  Jah
#     print("Kohapeal selgub, et mälumängus osalemiseks on vaja sisenemistasu.")
#     time.sleep(2)
#     print("Pärast kuldmündi tasku tühjendamist lubatakse sind mängima.")
#     time.sleep(2)
#     print("Maagilise kaardi võitmiseks on vaja vastata 8-le küsimusele 10-st õigesti. Vastasel juhul tuleb uuesti mängu proovida.")

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
    time.sleep(2)
    print('ta ütleb sulle')
    time.sleep(2)
    print('"Kui soovid varandus leida, on sul aardekaart vaja. \nKui saate 10-st küsimusest vähemalt 8 õigesti, ma annan seda sulle"')

    while trivia_score<11:
        üks=input('Mis on Eesti pealinn? ')
        if üks==trivia['linn']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if üks!=trivia['linn']:
            print('Vale vastus!')

        kaks=input('Mis aastal kuulutati välja Eesti vabariik? ')
        if kaks==trivia['vaba']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if kaks!=trivia['vaba']:
            print('Vale vastus!')

        kolm=input('Mis on Eestil kõige suurem saar? ')
        if kolm==trivia['saar']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if kolm!=trivia['saar']:
            print('Vale vastus!')

        neli=input('Mis on Eestil kõige vanem linn? ')
        if neli==trivia['linn']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if neli!=trivia['linn']:
            print('Vale vastus!')

        viis=input('Mis oli Eesti külmarekord? ')
        if viis==trivia['rekord']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if viis!=trivia['rekord']:
            print('Vale vastus!')

        kuus=input('Mitu meetrit on kõige kõrgem juga Eestis? ')
        if kuus==trivia['juga']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if kuus!=trivia['juga']:
            print('Vale vastus!')

        seitse=input('Mis on kõige pikem jõgi Eestis? ')
        if seitse==trivia['jõgi']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if seitse!=trivia['jõgi']:
            print('Vale vastus!')

        kaheksa=input('Mis on Eesti kõige kõrgem mägi? ')
        if kaheksa==trivia['mägi']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if kaheksa!=trivia['mägi']:
            print('Vale vastus!')

        üheksa=input('Mitu kilomeetrit pikk on Eesti merepiir? ')
        if üheksa==trivia['meri']:
            trivia_score+=1
            print('Sa said õige vastus!')
        if üheksa!=trivia['meri']:
            print('Vale vastus!')

        kümme=input('Mitu saart on Eestis? ')
        if kümme==trivia['arv']:
            trivia_score+=1
            print('Sa said õige vastus!')   
        if kümme!=trivia['arv']:
            print('Vale vastus!')

        if trivia_score>7:
            print('"Noh nii, vastasid õigesti... siin on sinu kaart nagu ma lubasin"')
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
    time.sleep(2)
    print('Aga chest on luukus')
    time.sleep(2)
    print('luku kood on 3 numbrit')
    time.sleep(2)
    print('saad lukku lahti ja oledki leidnud lõpp auhinna')
    time.sleep(2)
    print('\n')*5

    while luuk_skoor<3 or fail_count<5:   
        if luuk_skoor == 0:
            valik=int(input('Vali number 1 kuni 3: '))
            if valik!=int(kood[0]):
                fail_count+=1
                print('Valisid vale number! Proovige uuesti!')
            if valik==int(kood[0]):
                luuk_skoor+=1
                print('Sa valisid õige number!')
        if luuk_skoor == 1:
            valik=int(input('Vali number 1 kuni 3: '))
            if valik!=int(kood[1]):
                fail_count+=1
                print('Valisid vale number! Proovige uuesti!')
            if valik==int(kood[1]):
                luuk_skoor+=1
                print('Sa valisid õige number!')
        if luuk_skoor == 2:
            valik=int(input('Vali number 1 kuni 3: '))
            if valik!=int(kood[2]):
                fail_count+=1
                print('Valisid vale number! Proovige uuesti!')
            if valik==int((kood[2])):
                luuk_skoor+=1
                print('Sa valisid õige number!')


        if luuk_skoor==3:
            print('Imeline! Said luku lahti!')
            break
        if luuk_skoor<3:
            print('kahjuks ei saanud lukku lahti, pead uuesti proovima')

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