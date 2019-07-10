# Radan valintaa ei vielä ole

import csv
import json

#Ladataan event tiedosto lukumuotoon
with open('event.json', 'r') as f:
    data = json.load(f)

'''
    Perus muuttujat muistiinpanot
data['track']                                   #Radan nimi
data['preRaceWaitingTimeSeconds']               #Pre racen odotteluaika sekunteina
data['cloudLevel']                              #Pilvisyys 0.0 - 1.0
data['rain']                                    #Sateen määrä 0.0 - 1.0
data["sessions"][0]['hourOfDay']                #Aika-ajon kellonaika 0-23
data["sessions"][0]['sessionDurationMinutes']   #Aika-ajon kesto minuteissa
data["sessions"][1]['hourOfDay']                #Kisan Kellonaika 0-23
data["sessions"][1]['sessionDurationMinutes']   #Kisan kesto minuuteissa

'''

# Ladataan tiedosto ja tulostetaan lista ratojen ID numero sekä radan nimi
with open('radat.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    trackid = []
    trackname = []
    for row in readCSV:
        print(row)
        trackid.append(row[0])
        trackname.append(row[1])

# Kysytään mikä rata halutaan
def uusi_rata(ratanumero):
    while True:
        try:
            arvo = int(input('Radan numero = '))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    return arvo
track = uusi_rata(0)
# Tallennetaan uusi tieto
data['track'] = (trackname[track])


# Kysellään muut arvot
# Defaultti arvo ei vielä ole toiminnossa
def user_number(prompt, min_num, max_num, default):
    # Looppi pyörimään kunnes tulee oikeat arvot syötettyä
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        # Tarkistetaan että arvo on min ja max välissä
        if value < min_num or value > max_num:
            print("Wrong value.")
            continue
        else:
            break
    return value



#######################################################################################################
# Yleiset muuttujat mihin kysytään arvot
data['rain'] = user_number("Sateen määrä 0.0 - 1.0: ", 0, 1, 0)
data['cloudLevel'] = user_number("Pilvien määrä 0.0 - 1.0: ", 0, 1, 0)
data['preRaceWaitingTimeSeconds'] = user_number('Odotteluaika sessioiden välissä 30-90(min): ', 30, 90, 30)

data["sessions"][0]['hourOfDay'] = user_number('Aika-ajon kellonaika 0-24: ', 0, 24, 14)
data["sessions"][0]['sessionDurationMinutes'] = user_number('Aika-ajon kesto 10-60(min): ', 10, 60, 20)

data["sessions"][1]['hourOfDay'] = user_number('Kisan kellonaika 0-24: ', 0, 24, 14)
data["sessions"][1]['sessionDurationMinutes'] = user_number("Kisan kesto 10-240(min): ", 10, 240, 20)


#######################################################################################################
# Muunnetaan tietyt arvot arvot int muotoon

data['preRaceWaitingTimeSeconds'] = int(data['preRaceWaitingTimeSeconds'])

data["sessions"][0]['hourOfDay'] = int(data["sessions"][0]['hourOfDay'])
data["sessions"][0]['sessionDurationMinutes'] = int(data["sessions"][0]['sessionDurationMinutes'])

data["sessions"][1]['hourOfDay'] = int(data["sessions"][1]['hourOfDay'])
data["sessions"][1]['sessionDurationMinutes'] = int(data["sessions"][1]['sessionDurationMinutes'])


#######################################################################################################
#printtaillaan uudet asetukset vielä näytölle
print()
print('Rata: ', data['track'])
print('Sade: ', data['rain'])
print('Pilvisyys: ', data['cloudLevel'])
print('Odotteluaika (sek): ', data['preRaceWaitingTimeSeconds'])
print()
print('Aika-ajon kellonaika: ', data["sessions"][0]['hourOfDay'])
print('Aika-ajon kesto(min): ', data["sessions"][0]['sessionDurationMinutes'])
print()
print('Kisan kellonaika: ', data["sessions"][1]['hourOfDay'])
print('Kisan kesto(min)', data["sessions"][1]['sessionDurationMinutes'])
print()

#######################################################################################################


# Tallennetaan uudet arvot samaan tiedostoon ja muokataan rivitys
with open('event.json', 'w') as f:
    f.write(json.dumps(data, indent=2))