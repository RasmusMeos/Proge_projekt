import random

skoor=0
fail_count=0

while skoor<3 and fail_count!=5:
    valik=input('Vali number 1 läbi 3: ')
    arvut=random.randint(1,3)
    if valik==arvut:
        skoor+=1
        print('WooHoo! Sa valisid samma number kui arvuti')
        print('Sul on nüüd',skoor,'punkti')