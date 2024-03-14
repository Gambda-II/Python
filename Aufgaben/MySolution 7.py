class Kaffeemaschine:
    _wasserstand = 0
    _bohnenMenge = 0
    _maxWasserstand = 2000
    _maxBohnenMenge = 1000

    _wasserverbrauchProKaffee = 200
    _bohnenverbrauchProKaffee = 50

    def __init__(self, bohnenMenge, wasserstand):
        self._bohnenMenge = bohnenMenge
        self._wasserstand = wasserstand

    
    def WieVielWasserFehlt(self):
        menge = Kaffeemaschine._maxWasserstand - self._wasserstand
        print(f"Die Maschine ist gefüllt mit {self._wasserstand} ml von {Kaffeemaschine._maxWasserstand} ml Wasser")
        # print(f"Es fehlen noch {menge} ml Wasser!\n")
        return menge
    
    def WieVieleBohnenFehlen(self):
        menge = Kaffeemaschine._maxBohnenMenge - self._bohnenMenge
        print(f"Die Maschine ist gefüllt mit {self._bohnenMenge} von {Kaffeemaschine._maxBohnenMenge} Bohnen")
        # print(f"Es fehlen noch {menge} Bohnen!\n")
        return menge

    @staticmethod
    def UeberpruefeWasserstand(self):
        return self._wasserstand >= Kaffeemaschine._wasserverbrauchProKaffee
    
    @staticmethod
    def UeberpruefeBohnenmenge(self):
        return self._bohnenMenge >= Kaffeemaschine._bohnenverbrauchProKaffee

    def BrueheKaffe(self):
        
        wasserReicht = Kaffeemaschine.UeberpruefeWasserstand(self) == True
        bohnenReichen = Kaffeemaschine.UeberpruefeBohnenmenge(self) == True
        print("Maschine startet!\n\n")
        if (wasserReicht and bohnenReichen):
            self._wasserstand -= Kaffeemaschine._wasserverbrauchProKaffee
            self._bohnenMenge -= Kaffeemaschine._bohnenverbrauchProKaffee
            print("Mmmmh, lecker Kaffee!\n\n")
            return
        
        if (not wasserReicht):
            print(f"Eine Tasse benötigt {Kaffeemaschine._wasserverbrauchProKaffee} ml Wasser.")
            self.WieVielWasserFehlt()
            print("Das Wasser in der Maschine reicht nicht für einen köstlichen Kaffee. Schade!\n")
            
        if (not bohnenReichen):
            print(f"Eine Tasse benötigt {Kaffeemaschine._bohnenverbrauchProKaffee} Bohnen.")
            self.WieVieleBohnenFehlen()
            print("Die Anzahl der Bohnenstücke in der Maschine sind nicht suffizient für eine delikate Tasse Kaffee. Welch' ein Jammer!\n")

    # Meine Methoden
    def WasserAuffuellen(self, menge):
        if (menge <= 0 or menge > Kaffeemaschine._maxWasserstand):
            print("Das geht so nicht.")
        if (self._wasserstand + menge <= Kaffeemaschine._maxWasserstand):
            self._wasserstand += menge
            print(f"Es wurden {menge} ml Wasser hinzugefügt.\nDer neue Wasserstand beträgt {self._wasserstand} ml/{Kaffeemaschine._maxWasserstand} ml")
            return
        print("Das ist zu viel Wasser! Bitte neu versuchen.\n")

    def BohnenAuffuellen(self, menge):
        if (menge <= 0 or menge > Kaffeemaschine._maxBohnenMenge):
            print("Das geht so nicht.")
        if (self._bohnenMenge + menge <= Kaffeemaschine._maxBohnenMenge):
            self._bohnenMenge += menge
            print(f"Es wurden {menge} Bohnen hinzugefügt.\nDer neue Stand beträgt {self._bohnenMenge}/{Kaffeemaschine._maxBohnenMenge}")
            return
        print("Das sind zu viele Bohnen! Bitte neu versuchen.\n")
        
    def MengeEingeben(self):
        eingabeDesNutzers = input("Bitte eine Zahl eingeben:\n\n")
        try:
            return int(eingabeDesNutzers)
        except:
            print("Das ist doch keine Zahl! Bitte nochmal versuchen.\n")
            self.MengeEingeben()
            

    def AuffuellprogrammAuswaehlen(self):
        eingabeDesNutzers = input("Möchten Sie [W]asser oder [B]ohnen einfüllen?\n\n")

        if (eingabeDesNutzers.startswith("W")):
            menge = self.MengeEingeben()
            self.WasserAuffuellen(menge)
            return
        if (eingabeDesNutzers.startswith("B")):
            menge = self.MengeEingeben()
            self.BohnenAuffuellen(menge)
            return
        print("Das war doch genuschelt! Bitte nochmal probieren.\n")
        self.AuffuellprogrammAuswaehlen()

    def Programm(self):
        eingabeDesNutzers = input("Bitte wählen Sie aus: \n\t[K]affee brühen \n\t[W]asserstand prüfen \n\t[B]ohnenstand prüfen \n\t[A]uffüllen \n\t[R]aus aus der Maschine\n\n")
        
        if (eingabeDesNutzers.startswith("K")):
            self.BrueheKaffe()
        elif (eingabeDesNutzers.startswith("W")):
            self.WieVielWasserFehlt()
        elif (eingabeDesNutzers.startswith("B")):
            self.WieVieleBohnenFehlen()
        elif (eingabeDesNutzers.startswith("A")):
            self.AuffuellprogrammAuswaehlen()
        elif (eingabeDesNutzers.startswith("R")):
            quit()
        else:
            print("Das habe ich nicht verstanden.\n")

        self.Programm()
        



myKaffemaschine = Kaffeemaschine(0,0)

# myKaffemaschine.WieVielWasserFehlt()
# myKaffemaschine.WieVieleBohnenFehlen()
# myKaffemaschine.WasserAuffuellen(250)
# myKaffemaschine.WasserAuffuellen(250)
# myKaffemaschine.BohnenAuffuellen(200)
# myKaffemaschine.BrueheKaffe()
# myKaffemaschine.WasserAuffuellen(1000)
# myKaffemaschine.BrueheKaffe()
# myKaffemaschine.BrueheKaffe()
# myKaffemaschine.BrueheKaffe()
# myKaffemaschine.BrueheKaffe()
# myKaffemaschine.WieVielWasserFehlt()
# myKaffemaschine.WieVieleBohnenFehlen()

myKaffemaschine.Programm()