# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep
import os


# define our clear function


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# sleep for 0.5
sleep(0.5)

# now call function we defined above
clear()

import time

print("\u001b[92m██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░")
time.sleep(0.05)
print("\u001b[92m██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗")
time.sleep(0.05)
print("\u001b[92m██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║")
time.sleep(0.05)
print("\u001b[92m██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║")
time.sleep(0.05)
print("\u001b[92m██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝")
time.sleep(0.05)
print("\u001b[92m╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░")
time.sleep(0.05)
print("")
print("\u001b[92m░█████╗░░█████╗░███╗░░░███╗██████╗░██╗██╗░░░░░███████╗██████╗░")
time.sleep(0.05)
print("\u001b[92m██╔══██╗██╔══██╗████╗░████║██╔══██╗██║██║░░░░░██╔════╝██╔══██╗")
time.sleep(0.05)
print("\u001b[92m██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║██║░░░░░█████╗░░██████╔╝")
time.sleep(0.05)
print("\u001b[92m██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║██║░░░░░██╔══╝░░██╔══██╗")
time.sleep(0.05)
print("\u001b[92m╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░██║███████╗███████╗██║░░██║")
time.sleep(0.05)
print("\u001b[92m░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝")
print("")
print("\u001b[92mVersion: 1.7.3")
time.sleep(0.6)
print("")
print("\u001b[31m▒█▀▀█ █░░█ 　 █▀▀▄ █▀▀█ █░░█ ▀▀█▀▀ █▀▀ █▀▀█ █▀▄▀█ ")
print("\u001b[31m▒█▀▀▄ █▄▄█ 　 █▀▀▄ █▄▄▀ █░░█ ░░█░░ █▀▀ █▄▄█ █░▀░█ ")
print("\u001b[31m▒█▄▄█ ▄▄▄█ 　 ▀▀▀░ ▀░▀▀ ░▀▀▀ ░░▀░░ ▀▀▀ ▀░░▀ ▀░░░▀")
print("")
print("")

time.sleep(0.9)
print("\033[93mselect your language\033[0m")
print("1. \033[94mENGLISH\033[0m")
print("2. \033[94mITALIAN\033[0m")
print("3. \033[94mRUSSIAN (beta)\033[0m")
language = int(input())
print("")

while (language >= 4 or language <= 0):
    print("\u001b[31mERROR, invalid number")
    for i in range(5):
        print(".", end='')
        time.sleep(0.3)
    time.sleep(0.15)
    print(" ")
    print("\033[93mSelect your language:\033[0m")
    print("\033[94m1. ENGLISH\033[0m")
    print("\033[94m2. ITALIAN\033[0m")
    print("\033[94m3. RUSSIAN\033[0m")
    language = int(input())
    print("")

verifica = "n"

while verifica=="n" or verifica=="N":
    if language == 1:
        print("\033[93mwrite the name (lowercase)\033[0m")
        nome = input()
        print("")
        print("\33[93mwrite the surname (lowercase)\033[0m")
        cognome = input()
        print("")
        print("\033[93mwrite the birth (DDMMYYYY)\033[0m")
        nascita = input()
        print("")
        print("\033[93mInserisci il nome dell'animale domestico\033[0m")
        animale = input()
        print("")
        print("\33[93mwrite the EMAIL without domain (es. NO @gmail.com)\033[0m")
        email = input()
        print("")
        print("\033[93myou want to add special characters ( . , ! _ )? (Y/N)\033[0m")
        caratteri = input()


    elif language == 2:
        print("\033[93mScrivi il nome (minuscolo)\033[0m")
        nome = input()
        print("")
        print("\033[93mScrivi il cognome (minuscolo)\033[0m")
        cognome = input()
        print("")
        print("\033[93mScrivi la data di nascita (GGMMAAAA)\033[0m")
        nascita = input()
        print("")
        print("\033[93mInserisci il nome dell'animale domestico\033[0m")
        animale = input()
        print("")
        print("\033[93mInserisci l'EMAIL senza dominio (es. senza @gmail.com)\033[0m")
        email = input()
        print("")
        print("\033[93mVuoi aggiungere i caratteri speciali ( . , ! _ )? (Y/N)\033[0m")
        caratteri = input()



    else:
        print("\033[93mнапишите имя (строчная буква)\033[0m")
        nome = input()
        print("")
        print("\033[93mнапиши фамилию (строчная буква)\033[0m")
        cognome = input()
        print("")
        print("\033[93mвведите дату рождения (ДДММГГГГ)\033[0m")
        nascita = input()
        print("")
        print("\033[93mвведите EMAIL без домена (@ gmail.com)\033[0m")
        email = input()
        print("")
        print("\033[93mвыберите, нужно ли вставлять специальные символы\033[0m")
        caratteri = input()

    print("")
    print("")
    time.sleep(0.15)

    if language == 1:

        print("\033[96mNAME: \033[0m", end='')
        print(nome)
        time.sleep(0.05)
        print("\033[96mSURNAME: \033[0m", end='')
        print(cognome)
        time.sleep(0.05)
        if nascita != "":
            print("\033[96mBIRTH DAY: \033[0m", end='')
            print(nascita[:2]+"/"+nascita[2:4]+"/"+nascita[4:8])
            time.sleep(0.05)
        if animale != "":
            print("\033[96mPET: \033[0m", end='')
            print(animale)
            time.sleep(0.05)
        if email != "":
            print("\033[96mEMAIL ADDRESS: \033[0m", end='')
            print(email)
            time.sleep(0.05)

        print("\033[96mSPECIAL CHARACTER: \033[0m", end='')
        if caratteri == "Y" or caratteri == "y":
                print("Yes")
        else:
            print("No")
        time.sleep(0.65)
        print("")
        print("\033[95mAll value are correct? (Y/N): \033[0m")
        verifica = input()


    elif language == 2:

        print("\033[96mNOME: \033[0m", end='')
        print(nome)
        time.sleep(0.05)
        print("\033[96mCOGNOME: \033[0m", end='')
        print(cognome)
        time.sleep(0.05)
        if nascita!="":
            print("\033[96mDATA DI NASCITA: \033[0m", end='')
            print(nascita[:2]+"/"+nascita[2:4]+"/"+nascita[4:8])
            time.sleep(0.05)
        if animale != "":
            print("\033[96mANIMALE DOMESTICO: \033[0m", end='')
            print(animale)
            time.sleep(0.05)
        if email!="":
            print("\033[96mEMAIL: \033[0m", end='')
            print(email)
            time.sleep(0.05)

        print("\033[96mCARATTERI SPECIALI: \033[0m", end='')
        if caratteri=="Y" or caratteri=="y":
            print("Si")
        else:
            print("no")
        time.sleep(0.65)
        print("")
        print("\033[95mTutti i dati sono corretti? (Y/N): \033[0m")
        verifica = input()

    else:
        print("russo")


maiuscnome = (nome.capitalize())
maiusccognome = (cognome.capitalize())
fullmaiuscnome = (nome.swapcase())
fullmaiusccognome = (cognome.swapcase())
shortname3 = nome[:3]
shortname4 = nome[:4]

combinazioni = [nome, cognome, maiuscnome, maiusccognome, fullmaiuscnome, fullmaiusccognome, shortname4, shortname3]

if nascita != "":
    anno = nascita[4:8]
    mese = nascita[2:4]
    giorno = nascita[:2]
    abbrevanno = anno[2:]
    combinazioni.append(anno)
    combinazioni.append(mese)
    combinazioni.append(giorno)
    combinazioni.append(abbrevanno)
    combinazioni.append(mese[1:])
  
if animale != "":
    combinazioni.append(animale)

if email != "":
    combinazioni.append(email)

if caratteri == "y" or caratteri == "Y":
    combinazioni.append(".")
    combinazioni.append(",")
    combinazioni.append("!")
    combinazioni.append("_")
    combinazioni.append("1")
    combinazioni.append("2")
    combinazioni.append("3")
    combinazioni.append("4")

print("\033[95mEXTEND PASSWORD? (Y/N): \033[0m")
extend = input()
f = open("password.txt", "w")
if extend =="N" or extend =="n":


    for i in range(len(combinazioni)):
        for j in range(len(combinazioni)):
            if i != j:
                f.write(combinazioni[i] + combinazioni[j] + "\n")

    for i in range(len(combinazioni)):
        for j in range(len(combinazioni)):
            for k in range(len(combinazioni)):
                if i != j and i != k and j != k:
                    f.write(combinazioni[i] + combinazioni[j] + combinazioni[k] + "\n")


    for i in range(len(combinazioni)):
        for j in range(len(combinazioni)):
            for k in range(len(combinazioni)):
                for o in range(len(combinazioni)):
                    if i != j and i != k and i != o and j != k and j != o and k != o:
                        f.write(combinazioni[i] + combinazioni[j] + combinazioni[k] + combinazioni[o] + "\n")

  #  for i in range(len(combinazioni)):
   #     for j in range(len(combinazioni)):
    #        for k in range(len(combinazioni)):
     #           for o in range(len(combinazioni)):
      #              for x in range(len(combinazioni)):
       #                 if i != j and i != k and i != o and i != x and j != k and j != o and j != x and k != o and k != x \
        #                and o != x:
         #                   f.write(
          #                  combinazioni[i] + combinazioni[j] + combinazioni[k] + combinazioni[o] + combinazioni[x] + "\n")
else:
    for i in range(len(combinazioni)):
        for j in range(len(combinazioni)):
            f.write(combinazioni[i] + combinazioni[j] + "\n")

    for i in range(len(combinazioni)):
        for j in range(len(combinazioni)):
            for k in range(len(combinazioni)):
                f.write(combinazioni[i] + combinazioni[j] + combinazioni[k] + "\n")

    for i in range(len(combinazioni)):
        for j in range(len(combinazioni)):
            for k in range(len(combinazioni)):
                for o in range(len(combinazioni)):
                    f.write(combinazioni[i] + combinazioni[j] + combinazioni[k] + combinazioni[o] + "\n")

    #for i in range(len(combinazioni)):
     #   for j in range(len(combinazioni)):
      #      for k in range(len(combinazioni)):
       #         for o in range(len(combinazioni)):
        #            for x in range(len(combinazioni)):
         #               f.write(combinazioni[i] + combinazioni[j] + combinazioni[k] + combinazioni[o] + combinazioni[
          #                          x] + "\n")
f.close()

print("\033[91m----------------------------------------------------------------------")
print("")
print("")
if language == 1:
    print("\u001b[92mTHE FILE password.txt HAS BEEN CREATED HERE: \033[0m", end='')
elif language == 2:
    print("\u001b[92mIL FILE password.txt É STATO CREATO QUI': \033[0m", end='')
else:
    print("\u001b[92mв этой папке был создан файл password.txt: \033[0m", end='')
directory = os.getcwd()

print(directory, end='')
print("\password.txt")
print("")
print("")
if language == 1:
    print("\u001b[92mDo you want to open the text file? (Y/N): \033[0m", end='')
elif language == 2:
    print("\u001b[92mVuoi aprire il file? (Y/N): \033[0m", end='')
else:
    print("\u001b[92mВы хотите открыть текстовый файл? (Y/N): \033[0m", end='')

openf = input()

while openf != "Y" and openf != "y" and openf != "N" and openf != "n":
    print("\u001b[31mERROR, invalid value")
    for i in range(5):
        print(".", end='')
        time.sleep(0.3)
    time.sleep(0.15)
    print(" ")
    if language == 1:
        print("\u001b[92mDo you want to open the text file? (Y/N): \033[0m", end='')
    elif language == 2:
        print("\u001b[92mVuoi aprire il file? (Y/N): \033[0m", end='')
    else:
        print("\u001b[92mВы хотите открыть текстовый файл? (Y/N): \033[0m", end='')
    openf = input()
if openf == "Y" or openf == "y":
    os.startfile("password.txt")
else:
    print("")

print("")
print("")
print("\033[91m----------------------------------------------------------------------")
print("")
print("")
