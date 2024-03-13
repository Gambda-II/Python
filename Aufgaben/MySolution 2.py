def BerechneAufgenommeneMengeAlkohol(getrunkeneMengeInMilliliter, alkoholgehalt = 0.05, dichteDesEthanols = 0.8):
    return getrunkeneMengeInMilliliter * alkoholgehalt * dichteDesEthanols

def BerechnePromilleWert(Alkoholmenge, Koerpergwicht):
    try:
        return Alkoholmenge / (0.65 * Koerpergwicht)
    except ZeroDivisionError:
        print("Körpergewicht kann nicht Null sein.")

minGewicht = 50
maxGewicht = 600

def GewichtAbfrage():
    while (True):
        userInput_GewichtInKilogramm = input("Bitte Gewicht in kg angeben.\n")
        
        try:
            gewichtInKilogramm = int(userInput_GewichtInKilogramm)
            
            if (gewichtInKilogramm > minGewicht and gewichtInKilogramm < maxGewicht):
                return gewichtInKilogramm
                
            print("Das angegebene Gewicht ist nicht realistisch. Bitte Eingabe überprüfen und wiederholen.")
        except:
            print("Die Eingabe muss eine Zahl sein. Bitte Eingabe wiederholen.")

minMilliliter = 0
maxMilliliter = 3000

def GetrunkeneMengeAbfrage():
    while (True):
        userInput_GetrunkeneMenge = input("Wie viel Milliliter Bier wurde getrunken?\n")
        
        try:
            getrunkeneMenge = int(userInput_GetrunkeneMenge)
            
            if (getrunkeneMenge >= minMilliliter and getrunkeneMenge <= maxMilliliter):
                return getrunkeneMenge
                
            print("Die getrunkene Menge darf keine negative Zahl sein und soll realistisch sein. Bitte Eingabe überprüfen und wiederholen.")
        except:
            print("Die Eingabe muss eine Zahl sein. Bitte Eingabe wiederholen.")                    

def AuswertungPromillewert(promillewert):

    if (promillewert <= 0.3):
        print("Noch akzeptabel. Dennoch vorsichtig sein!")
    elif (promillewert <= 0.5):
        print("Achtung! Hände weg vom Steuer!")
    elif (promillewert <= 0.8):
        print("Das ist jetzt schon ganz schön ordentlich.")
    else:
        print("Kein Kommentar...")


def Programm():
    getrunkeneMengeInMilliliter = GetrunkeneMengeAbfrage()
    alkoholmenge = BerechneAufgenommeneMengeAlkohol(getrunkeneMengeInMilliliter)
    gewicht = GewichtAbfrage()
    promillewert = BerechnePromilleWert(alkoholmenge, gewicht)

    print(f"{getrunkeneMengeInMilliliter} ml")
    print(f"menge: {alkoholmenge.__round__(2)}")
    print(f"{gewicht} kg")
    print(f"{promillewert.__round__(3)} ‰")
    AuswertungPromillewert(promillewert)

Programm()