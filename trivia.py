# 10 ? ja 8 peab olema õige et võita


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

    üheksa=input('Mitu kilomeetrit on Eesti merepiir? ')
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