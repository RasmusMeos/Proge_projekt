# 10 ? ja 8 peab olema õige et võita

trivia_score=0
trivia={
    'linn':'Tallinn',
    'vaba':'1918',
    'saar':'Saaremaa',
    'rekord':'-43.5'
    }

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

viis=input('Mis oli Eesti külmrekord? ')
if viis==trivia['rekord']:
    trivia_score+=1
    print('Sa said õige vastus!')
if viis!=trivia['rekord']:
    print('Valle vastus :(')


