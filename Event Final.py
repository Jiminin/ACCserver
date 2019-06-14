'''
!!!!!!!!!Tiedossa olevat bugit ja mitä tulee korjata/opetella!!!!!!!!!!!!!

-Ratojen valitsemisessa käytetään numeroita kirjoituksen siasta
-arvoja syöttäessä kirjaimia tai tyhjäksi jättäminen tilttaa

'''
import json
#Ladataan event tiedosto
with open('event.json', 'r') as f:
    data = json.load(f)
    

'''
    Perus muuttujat muistiinpanot
data['track']                           #Mikä rata
data['preRaceWaitingTimeSeconds']       #Pre racen odotteluaika sekunteina
data['cloudLevel']                      #Pilvisyys 0.0 - 1.0
data['rain']                            #Sateen määrä 0.0 - 1.0

    #1 Session muuttujat (qualifuing)
data["sessions"][0]['hourOfDay']                #Kellonaika 0-23
data["sessions"][0]['sessionDurationMinutes']   #Session data["sessions"][1]['sessionDurationMinutes'] minuteissa

    #2 Session muuttujat (race)
data["sessions"][1]['hourOfDay']                #Kellonaika 0-23
data["sessions"][1]['sessionDurationMinutes']   #Session data["sessions"][1]['sessionDurationMinutes'] minuteissa

'''
## kysytään uusi rata ja sille vaihtoehdot
#data['track'] = input('Uusi rata?: ')
## varmistetaan että tulee oikea arvo !!!!KESKEN!!!!

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
data['preRaceWaitingTimeSeconds'] = user_number('Odotteluaika (sek) 30-90: ', 30, 90, 30)

# Aika-ajon muuttujat
data["sessions"][0]['hourOfDay'] = user_number('Aika-ajon kellonaika 0-24: ', 0, 24, 14)
data["sessions"][0]['sessionDurationMinutes'] = user_number('Aika-ajon pituus min 10-60: ', 10, 60, 20)

# Kisan muuttujat
data["sessions"][1]['hourOfDay'] = user_number('Kisan kellonaika 0-24: ', 0, 24, 14)
data["sessions"][1]['sessionDurationMinutes'] = user_number("Kisan pituus min 10-240: ", 10, 240, 20)

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
print('Aika-ajon pituus(min): ', data["sessions"][0]['sessionDurationMinutes'])
print()
print('Kisan kellonaika: ', data["sessions"][1]['hourOfDay'])
print('Kisan pituus(min)', data["sessions"][1]['sessionDurationMinutes'])
print()







# Tallennetaan uudet arvot samaan tiedostoon ja muokataan rivitys
with open('event.json', 'w') as f:
    f.write(json.dumps(data, indent=2))