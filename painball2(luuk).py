import random

skoor=0
fail_count=0
kood=[]
kood.append(random.randint(1,3))
kood.append(random.randint(1,3))
kood.append(random.randint(1,3))


while skoor<3 and fail_count<5:   
    if skoor == 0:
        valik=int(input('Vali number 1 läbi 3: '))
        if valik!=int(kood[0]):
            fail_count+=1
            print('Valisid vale number! Proovige uuesti!')
        if valik==int(kood[0]):
            skoor+=1
            print('WooHoo! Sa valisid õige number')
    if skoor == 1:
        valik=int(input('Vali number 1 läbi 3: '))
        if valik!=int(kood[1]):
            fail_count+=1
            print('Valisid vale number! Proovige uuesti!')
        if valik==int(kood[1]):
            skoor+=1
            print('WooHoo! Sa valisid õige number')
    if skoor == 2:
        valik=int(input('Vali number 1 läbi 3: '))
        if valik!=int(kood[2]):
            fail_count+=1
            print('Valisid vale number! Proovige uuesti!')
        if valik==int((kood[2])):
            skoor+=1
            print('WooHoo! Sa valisid õige number')


if skoor==3:
    print('Sa oled võitja! :)')
if skoor<3:
    print('kahjuks oled kaotunud :(')