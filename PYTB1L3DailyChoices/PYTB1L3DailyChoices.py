import random
import time

def start():
    tijden = [
        6.30,
        6.45,
        7.00,
        7.15,

    ]
    a = random.choice(tijden)
    print('Je gaat iets heel spannends doen, je moet er voor zorgen dat je optijd in de klas zit!')
    print('alleen de dingen in het leven lukken niet echt duss ja zorg dat je optijd bent!')
    print('Ga je optijd opschool komen?')
    print('OKE GOGOGO!!!!!')
    time.sleep(3)
    print(' ')
    print("Je bent om",a,"uur wakker, wil je VERDER slapen of OPSTAAN?")
    antwoord = input('Jij gaat: ' )
    if antwoord == 'OPSTAAN':
        print("Oke je bent opgestaan! Je maakt je fris en begint de dag goed.")
        print(" ")
        print("Je hebt honger en wilt gaan eten, maak je een BOTERHAM of één TOSTI? ")
        antwoord1_2 = input('Je maakt een: ')
        if antwoord1_2 == 'BOTERHAM':
            print('Je hebt een' ,antwoord1_2, 'gemaakt, en je hebt er meeten ook een paar voor school gemaakt!')
            time.sleep(1)
            print('Nu dat je lekker optijd bent, vertrek je ook goed optijd voor de trein.  ')
            print('Pak je de FIETS of BUS naar het station')
            antwoord1_2_1 = input('Je gaat met de: ')
            if antwoord1_2_1 == 'BUS':
                print('Je hebt de bus gepakt alleen ja bussen zijn stom en laat effe afwachten of je de trein haalt.')
                time.sleep(1)
                print("Nou je stapt uit je bus maar je moet wel rennen om net je trein te pakken!")
            elif antwoord1_2_1 == 'FIETS':
                 print('Je hebt de fiets gepakt. Er is wel een klein windje maar optijd ben je wel.')
                 time.sleep(1)
                 print('Okeh je zit de trein pfff! Nu effe chille en hopen dat er niks misgaat ')
            else:
                print(antwoord1_2_1, "was geen goed antwoord, je bent nu al telaat!")
            print(' ')
            print('Je stapt uit in zuid om de metro te pakken.')
            print('Alleen die metro komt maar niet. ')
            antwoord2 = input('Ga je zitten WACHTEN of ga je ZOEKEN voor andere opties: ')
            if antwoord2 == 'WACHTEN':
             print("je hebt gewacht en de metro komt eindelijk!")
             print("je bent ook eindelijk opschool. En je hebt het gehaald!")
             print(" ")
            elif antwoord2 == 'ZOEKEN':
                print("Je hebt lopen zoeken voor een andere optie maar dat is niet gelukt helaas.")
                print("Dus je pakt de metrotje later!")
                print("Maar je bent nog optijd!!")

        elif antwoord1_2 == 'TOSTI':
                time.sleep(1)
                print('')
                print('Oew een',antwoord1_2, 'lekkah hoor maar kost wel veel tijd. ' )
                print('De bus is al vertrokken naar, maar je hebt wel genoeg tijd voor de fiets.')
                print("Fiets je SNEL of fiets je LANGZAAM?")
                antwoord1_3 =input('Je gaat: ')
                if antwoord1_3 == 'SNEL':
                    print("Je bent snel gegaan! ")
                    print("Daardoor haal je je trein net optijd.")
                elif antwoord1_3 == 'LANGZAAM':
                    print("Ownee je bent telaat omdat je je langzaam fietste maar je bent nog net optijd voor de trein.")
                    print('Je stapt uit in zuid om de metro te pakken.')
                    print('Alleen die metro komt maar niet. ')
                    antwoord1_4 = input('Ga je zitten WACHTEN of ga je ZOEKEN voor andere opties: ')
                    if antwoord1_4 == 'WACHTEN':
                        print("je hebt gewacht en de metro komt eindelijk!")
                        print("je bent ook eindelijk opschool. En je hebt het gehaald!")
                        print(" ")
                    else:
                        print("Je hebt lopen zoeken voor een andere optie maar dat is niet gelukt helaas.")
                        print("Dus je pakt de metrotje later!")
                        print("Maar je bent nog optijd!!")


        else:
            print(antwoord1_2, "was helaas geen goed antwoord, en je bent nu al af :(!")
    elif antwoord == 'VERDER':
        time.sleep(3)
        print(" ")
        print("Ow shit je hebt je verslapen")
        print("En gaat niet naar school!")


    else:
        print(antwoord, "was geen goed antwoord, je bent nu al telaat!")


start()