import random

score = 1
#health = 100

if score == 0:
  täringu_mäng = "game of dice"

if score == 1:
  võimalused = ["kivi", "paber", "käärid"]
  mängude_arv = 5
  võite_vaja = 3

  mäs = 0  # mängija võite
  ars = 0  # arvuti võite
  print("Järgmiseks ülesandeks on võita kolme võiduni kestev kivi-paber-käärid. Võidu puhul teenid oma skoorile lisapunkti ja saad liikuda järgmise ülesandeni")
  while True:
      mängija_valik = input("Vali kas kivi, paber või käärid: ")
      arvuti_valik = random.choice(võimalused)

      if mängija_valik == arvuti_valik:
          print("Tegid arvutiga sama valiku. Te jäite viiki!")
          print("Seis on", mäs,":",ars)

      elif mängija_valik == "kivi" and arvuti_valik == "paber":
          ars += 1
          print("Paber katab kivi - arvuti võit!")
          print("Seis on", mäs,":",ars)
      elif mängija_valik == "kivi" and arvuti_valik == "käärid":
          mäs += 1
          print("Kivi lõhub käärid - sinu võit!")
          print("Seis on", mäs,":",ars)

      elif mängija_valik == "käärid" and arvuti_valik == "paber":
          mäs += 1
          print("Käärid lõikavad paberi - sinu võit!")
          print("Seis on", mäs,":",ars)
      elif mängija_valik == "käärid" and arvuti_valik == "kivi":
          ars += 1
          print("Kivi lõhub käärid - arvuti võit!")
          print("Seis on", mäs,":",ars)

      elif mängija_valik == "paber" and arvuti_valik == "kivi":
          mäs += 1
          print("Paber katab kivi - sinu võit!")
          print("Seis on", mäs,":",ars)
      elif mängija_valik == "paber" and arvuti_valik == "käärid":
          ars += 1
          print("Käärid lõikavad paberi - arvuti võit!")
          print("Seis on", mäs,":",ars)

      if (mäs == võite_vaja or ars == võite_vaja) and mäs > ars:
          print("Õnnitlused, oled võitnud kolme võiduni mängitava seeria!")
          print("Lõppseis jäi:", mäs,":",ars)
          score == 2
          break
          
      elif (mäs == võite_vaja or ars == võite_vaja) and mäs < ars:
          print("Proovi uuesti! Arvuti võitis selle kolme võiduni mängitava seeria.")
          print("Lõppseis jäi:", mäs,":",ars)
          mäs = 0
          ars = 0
