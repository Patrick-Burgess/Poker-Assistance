def RaiseFirstIn(cardsSTR,positionSTR,bigblindINT):
    if positionSTR == "UT":
        if cardsSTR in ["AAo", "KKo", "QQo", "JJo", "TTo", "99o", "88o", "77o","AKs", "AQs", "AJs", "ATs", "KQs","AKo", "AQo"]:
            print("Raise ",2.5*bigblindINT)
            print("~10.1% range")
        else:
            print("Fold Hand")
            print("~89.9% range")

    elif positionSTR == "U1":
        if cardsSTR in ["AAo", "KKo", "QQo", "JJo", "TTo", "99o", "88o", "77o", "AKs", "AQs", "AJs", "ATs", "A5s", "KQs", "KJs", "QJs", "JTs", "T9s", "AKo", "AQo"]:
            print("Raise ",2.5*bigblindINT)
            print("~14.3% range")
        else:
            print("Fold Hand")
            print("~85.7% range")
    elif positionSTR == "U2":
        if cardsSTR in ["AAo", "KKo", "QQo", "JJo", "TTo", "99o", "88o", "77o", "66o","AKs", "AQs", "AJs", "ATs", "A5s","KQs", "KJs", "QJs", "JTs", "T9s", "98s", "87s","AKo", "AQo"]:
            print("Raise ",2.5*bigblindINT)
            print("~15.7% range")
        else:
            print("Fold Hand")
            print("~84.3% range")
    elif positionSTR == "LJ":
        if cardsSTR in ["AAo", "KKo", "QQo", "JJo", "TTo", "99o", "88o", "77o", "66o", "55o", "AKs", "AQs", "AJs", "ATs", "A5s", "A4s", "KQs", "KJs", "QJs", "JTs", "T9s", "98s", "87s", "76s", "AKo", "AQo", "AJo", "KQo"]:
            print("Raise ",2.5*bigblindINT)
            print("~18.3% range")
        else:
            print("Fold Hand")
            print("~81.7% range")
    elif positionSTR == "HJ":
        if cardsSTR in ["AAo", "KKo", "QQo", "JJo", "TTo", "99o", "88o", "77o", "66o", "55o", "44o", "AKs", "AQs", "AJs", "ATs", "A5s", "A4s", "KQs", "KJs", "QJs", "JTs", "T9s", "98s", "87s", "76s", "65s","AKo", "AQo", "AJo", "KQo"]:
            print("Raise ",2.5*bigblindINT)
            print("~21.3% range")
        else:
            print("Fold Hand")
            print("~78.7% range")
    elif positionSTR == "CO":
        if cardsSTR in ["AAo", "KKo", "QQo", "JJo", "TTo", "99o", "88o", "77o", "66o", "55o", "44o", "33o", "22o", "AKs", "AQs", "AJs", "ATs", "A5s", "A4s", "A3s", "A2s", "KQs", "KJs", "KTs", "QJs", "QTs", "JTs", "J9s", "T9s", "T8s", "98s", "97s", "87s", "86s", "76s", "75s", "65s", "54s", "AKo", "AQo", "AJo", "ATo", "KQo", "KJo", "QJo"]:
            print("Raise ",2.5*bigblindINT)
            print("~27.0% range")
        else:
            print("Fold Hand")
            print("~73.0% range")
    elif positionSTR == "BT":
        if cardsSTR in ["AAo", "KKo", "QQo", "JJo", "TTo", "99o", "88o", "77o", "66o", "55o", "44o", "33o", "22o", "AKs", "AQs", "AJs", "ATs", "A5s", "A4s", "A3s", "A2s", "KQs", "KJs", "KTs", "K9s", "K8s", "QJs", "QTs", "Q9s", "JTs", "J9s", "J8s", "T9s", "T8s", "98s", "97s", "87s", "86s", "76s", "75s", "65s", "64s", "54s", "53s", "43s", "AKo", "AQo", "AJo", "ATo", "A9o", "A8o", "KQo", "KJo", "KTo", "QJo", "QTo", "JTo", "J9o", "T9o", "98o", "87o"]:
            print("Raise ",2.5*bigblindINT)
            print("~51.1% range")
        else:
            print("Fold Hand")
            print("~48.9% range")
    elif positionSTR == "SB":
        if cardsSTR in ["AAo", "KKo", "QQo", "JJo", "TTo", "99o", "88o", "77o", "66o", "AKs", "AQs", "AJs", "ATs", "KQs","AKo", "AQo"]:
            print("Raise ",2.5*bigblindINT)
            print("~8.9% range")
        elif cardsSTR in ["65s", "54s", "43s"]:
            print("Raise as a Bluff ",3.5*bigblindINT)
            print("~13.0% range")
        elif cardsSTR in ["KJs", "QJs", "JTs", "T9s", "98s", "87s","A5s", "A4s", "A3s", "A2s"]:
            print("Limp/Call ",1*bigblindINT)
            print("~48.6% e")
        else:
            print("Fold Hand")
            print("~29.6% range")
    else:
        print("Error with Position entered")
#Call for RFI Function
cardsSTR = str(input("Enter your cards (AAo,AKs) -> "))
positionSTR = str(input("Enter your 2 letter position (UT/UndertheGun,U1/UndertheGun+1,U2/UndertheGun+2, LJ/Lojack, HJ/Hijack, CO/Cutoff, BT/Button, SB/Small Blind) -> "))
bigblindINT = 0.5

RaiseFirstIn(cardsSTR,positionSTR, bigblindINT)

