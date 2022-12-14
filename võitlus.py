import random

libahunt_elud = 250
hammusta = 10
kriimusta = 5
libahunt_rünnak = [hammusta, kriimusta]
mängija_elud = 100
tulista = 25
noahoop = 10
padruneid = 6
tervenda = 75
moona = 1

while libahunt_elud > 0 and mängija_elud > 0:
    tegevus = str(input("Vali sulgudes numbriga tegevus: lase revolvriga(1), torka noaga(2), tervenda ennast(3), lae revolvrit(4): "))
    rünnak = random.choices(libahunt_rünnak, weights=(30,70), k=1)
    if tegevus == "hõbekuul":
        libahunt_elud = 0
        print("Kasutasid revolvris hõbekuuli ning libahunt on haarab rinnust ning kukub selili. Oled tapnud libahundi!")
        break
    elif tegevus == "1" and padruneid > 0 and moona > 0 or moona == 0:
        libahunt_elud -= tulista
        padruneid -= 1
        print("Said libahundile pihta! Tal on alles veel",libahunt_elud,"punkti jagu elusid.")
    elif tegevus == "1" and padruneid == 0 and moona > 0:
        print("Revolvrist on kuulid otsas! Relv tegi ainult klõps, vaja laadida!")
    elif tegevus =="1" and padruneid == 0 and moona == 0:
        print("Revolvrist on kuulid otsas ja ka moon on otsas! Relv teeb vajutades klõps, sellest pole enam kasu!")
    elif tegevus == "2":
        libahunt_elud -= noahoop
        print("Haavasid noaga libahunti! Tal on alles veel",libahunt_elud,"punkti jagu elusid.")
    elif tegevus == "3" and tervenda == 75:
        mängija_elud += tervenda
        tervenda -= 75
        print("Jõid elu toovat võlujooki! Sul on nüüd", mängija_elud, "punkti jagu elusid.")
    elif tegevus == "3" and tervenda == 0:
        print("Haarasid taas võlujoogi järele, kuid pudel on tühi! Ennast ei õnnestunud tervendada.")
    elif tegevus == "4" and padruneid == 0 and moona > 0:
        padruneid += 6
        moona -= 1
        print("Relv on laetud!")
    elif tegevus == "4" and padruneid > 0 and moona > 0:
        print("Relvas on veel kuule! Laadida saad, kui relv on tühi!")
    elif tegevus == "4" and padruneid > 0 and moona == 0:
        print("Moon on otsas! Lasta saad veel nii palju, kui revolvris kuule!")
    elif tegevus == "4" and padruneid == 0 and moona == 0:
        print("Moon on otsas, relva enam kasutada ei saa!")
    if rünnak[0] == 5:
        mängija_elud -= 5
        print("Libahunt kriimustas sind! Sul on nüüd", mängija_elud, "punkti jagu elusid.")
    elif rünnak[0] == 10:
        mängija_elud -= 10
        print("Sattusid libahundile liiga lähedale ja ta hammustas sind! Sul on nüüd", mängija_elud, "punkti jagu elusid.")
        
    if libahunt_elud <= 0 and mängija_elud > 0:
        print("Libahunt tuigerdab ja kukub selili! Oled tapnud libahundi!")
        break
    elif libahunt_elud > 0 and mängija_elud <= 0:
        print("Libahunt sai sinust jagu! Paar hingetõmmet ja proovi uuesti!")
        mängija_elud = 100
        libahunt_elud = 250
        padruneid = 0
        moona = 0
        padruneid = 6
        moona = 1
        
    
        