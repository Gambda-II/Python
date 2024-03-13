weatherOptions = ["regnerisch", "sonnig"]
temperatureBoundary = 20

while (True):
    userInput_Weather = input("Wie ist das Wetter heute? Sonnig oder regnerisch?\n")
    weather = userInput_Weather.lower()

    if (weatherOptions.__contains__(weather)):
        break
    print(f"\nEingabe \"{userInput_Weather}\" konnte nicht erkannt werden.\nBitte Eingabe wiederholen.\n")

while (True):
    userInput_Temperature = input("\nWelche Temperatur (Celsius) herscht in dieser Zeit? Bitte eine Zahl eingeben.\n")

    try:
        temperature = int(userInput_Temperature)
        break
    except:
        print(f"\nEingabe \"{userInput_Temperature}\" konnte nicht erkannt werden.\nBitte eine Zahl eingeben!\n")

def advice(temparature, weather):
    print(f"Eure Exzellenz, das Wetter ist {weather} und es herrschen {temperature} °C.\nSo empfehle ich Ihnen")

    if (temparature >= temperatureBoundary):  
        print("ein T-Shirt zu tragen!")
    else:
        print("eine Jacke zu tragen!")
    
    if (weather == "regnerisch"):
        print("Vergesset nicht euer Regenschirm!")

advice(temperature,weather)