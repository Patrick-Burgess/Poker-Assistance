def FacingRaiseFirstIN(cardsSTR,positionSTR,rivalpositionSTR,rivalbetINT):
    #EarlyToMiddlePosition
    if positionSTR == "U1" or positionSTR == "U2":
        if cardsSTR in ["AAo","AKs","AKo","KKo","QQo"]:
            print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
        elif cardsSTR in ["AQo", "KJs","ATs"]:
            print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
        elif cardsSTR in ["AQs","AJs","KQs","QJs","JJo","JTs","TTo","99o","88o"]:
            print("Call the raise, Call this much -> ",rivalbetINT)
        else:
            print("Fold Hand")
    elif positionSTR == "LJ":
        if rivalpositionSTR == "UT" or rivalpositionSTR == "U1":
            if cardsSTR in ["AAo","AKs","AKo","KKo","QQo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AQo", "KJs", "ATs","A5s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AQs","AJs","KQs","QJs","JJo","JTs","TTo","99o","88o","77o", "T9s"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold Hand")
        elif rivalpositionSTR == "U2":
            if cardsSTR in ["AAo", "AKs", "AKo", "KKo", "QQo"]:
                print("3 bet for a value, Bet this much -> ", 3 * rivalbetINT)
            elif cardsSTR in ["AQo", "KJs", "ATs", "A5s","98s","87s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AQs", "AJs", "KQs", "QJs", "JJo", "JTs", "TTo", "99o", "88o", "77o", "T9s","66o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold Hand")
    elif positionSTR == "HJ": #checkHJis right
        if rivalpositionSTR == "UT":
            if cardsSTR in ["AAo","AKs","AKo","KKo","QQo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AQo", "KJs", "ATs","A5s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AQs","AJs","KQs","QJs","JJo","JTs","TTo","99o","88o","77o", "T9s"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold Hand")
        elif rivalpositionSTR == "U1":
            if cardsSTR in ["AAo","AKs","AKo","KKo","QQo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AQo", "KJs", "ATs","A5s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AQs","AJs","KQs","QJs","JJo","JTs","TTo","99o","88o","77o","T9s","66o","98s"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold Hand")
        elif rivalpositionSTR == "U2":
            if cardsSTR in ["AAo","AKs","AKo","KKo","QQo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AQo", "KJs", "ATs","A5s","A4s","A3s","AQo","87s","76s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AQs", "AJs", "KQs", "QJs", "JJo", "JTs", "TTo", "99o", "88o", "77o", "T9s", "66o", "98s", "55o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold Hand")
        elif rivalpositionSTR == "LJ":
            if cardsSTR in ["AAo","AKs","AKo","KKo","QQo","AQo","KQs","QQo","AQs","AJs"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AJo","ATo","KQo","A5s", "A4s","A3s","A2s","76s","65s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["ATs","KJs","KTs","QJs","QTs","JJo","JTs","TTo","T9s","99o", "98s","88o","87s","77o","66o","55o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold Hand")
    elif positionSTR == "CO":
        if rivalpositionSTR == "UT" or rivalpositionSTR == "U1":
            if cardsSTR in ["AAo","AKs","AQs","AKo","KKo","QQo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AQo","AJo","A5s","A4s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AJs","ATs","KQs","KJs","KTs","QJs","QTs","JJo","JTs","TTo","T9s","99o", "98s","88o","77o","66o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold Hand")
        elif rivalpositionSTR == "U2":
            if cardsSTR in ["AAo","AKs","AQs","AKo","KKo","QQo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AQo","AJo","A5s","A4s","A3s","A2s","87s","76s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AJs","ATs","KQs","KJs","KTs","QJs","QTs","JJo","JTs","TTo","T9s","99o", "98s","88o","77o","66o","55o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold Hand")
        elif rivalpositionSTR == "LJ":
            if cardsSTR in ["AAo","AKs","AQs","AKo","KKo","QQo","AQo","KQs","AJs"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AJo","KQo","A5s","A4s","A3s","A2s","87s","76s","65s","54s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["ATs","KJs","KTs","QJs","QTs","JJo","JTs","TTo","T9s","99o", "98s","88o","77o","66o","55o","44o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold Hand")
        elif rivalpositionSTR == "HJ":
            if cardsSTR in ["AAo","AKs","AQs","AKo","KKo","QQo","AQo","KQs","AJs"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AJo","KQo","K9s","Q9s","J9s","A9s","A8s","A7s","A6s","A5s","A4s","A3s","A2s","76s","65s","54s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["ATs","KJs","KTs","QJs","QTs","JJo","JTs","TTo","T9s","99o","98s","88o","87s","66o","55o","44o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold Hand")
    elif positionSTR == "BT":
        if rivalpositionSTR == "UT":
            if cardsSTR in ["AAo", "KKo", "QQo", "AKs", "AKo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AQo", "A5s", "A4s", "KQo", "AJo", "76s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AQs", "AJs", "ATs","KQs","KJs", "KTs", "QTs", "QJs","JJo","JTs","TTo", "T9s","99o" ,"98s","88o", "87s","77o", "66o", "55o", "44o", "33o","22o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold Hand")
        elif rivalpositionSTR == "U1":
            if cardsSTR in ["AAo", "KKo", "QQo", "AKs", "AKo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AQo", "A5s", "A4s","A3s","A2s","KQo", "AJo"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AQs", "AJs", "ATs","KQs","KJs", "KTs", "QTs", "QJs","JJo","JTs","J9s","TTo", "T9s","99o" ,"98s","88o", "87s","77o", "76s", "66o", "55o", "44o", "33o","22o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold Hand")
        elif rivalpositionSTR == "U2":
            if cardsSTR in ["AAo", "KKo", "QQo", "AKs", "AQs","AKo","AQo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["ATo","KJo","A9s","A5s","A4s","A3s","A2s","65s","54s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AJo","KQo","KQs","AJs","ATs","KJs","KTs","QJs","QTs","JJo","JTs","J9s","TTo","T9s","99o","98s","88o","87s","77o","76s","66o","55o","44o","33o","22o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold Hand")
        elif rivalpositionSTR == "LJ":
            if cardsSTR in ["AAo", "KKo", "QQo", "AKs", "AQs","AKo","AQo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["ATo","KJo","A8s","A7s","A6s","A5s","A4s","A3s","A2s","65s","54s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AJo","KQo","KQs","AJs","ATs","A9s","KJs","KTs","QJs","QTs","JJo","JTs","J9s","TTo","T9s","99o","98s","88o","87s","77o","76s","66o","55o","44o","33o","22o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold Hand")
        elif rivalpositionSTR == "HJ":
            if cardsSTR in ["AAo","AKs","AQs","AJs","AKo","KKo","AQo","QQo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["A8s","A7s","A6s","A5s","A4s","A3s","A2s","KJo","ATo","86s","75s","65s","54s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["ATs","A9s","KQs","KJs","KTs","K9s","KQo","QJs","QTs","Q9s","AJo","JJo","JTs","J9s","TTo","T9s","T8s","99o","98s","97s","88o","87s","77o","76s","66o","55o","44o","33o","22o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold Hand")
        elif rivalpositionSTR == "CO":
            if cardsSTR in ["AAo","AKs","AQs","AJs","AKo","KKo","AQo","QQo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["A8s","A7s","A6s","A3s","A2s","K8s","Q8s","QJo","J8s","KTo","A9o","","ATo","86s","75s","65s","64s","54s","43s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["ATs","A9s","A5s","A4s","KQs","KJs","KTs","K9s","KQo","QJs","QTs","Q9s","AJo","KJo","JJo","JTs","J9s","ATo","TTo","T9s","T8s","99o","98s","97s","88o","87s","77o","76s","66o","55o","44o","33o","22o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold Hand")
    elif positionSTR == "SB":
        if rivalpositionSTR == "UT" or rivalpositionSTR == "U1":
            if cardsSTR in ["AAo", "KKo", "QQo", "AKs"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["A5s", "98s", "87s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AQs", "AJs", "ATs","AKo", "KQs", "KJs","AQo", "QJs","JJo", "JTs", "TTo","T9s", "99o", "88o", "77o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold")
        elif rivalpositionSTR == "U2":
            if cardsSTR in ["AAo", "KKo", "QQo", "AKs"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["A5s",  "87s", "76s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AQs", "AJs", "ATs","AKo", "KQs", "KJs","KTs","AQo", "QJs","QTs","JJo", "JTs", "TTo","T9s", "99o","98s", "88o", "77o","66o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold")
        elif rivalpositionSTR == "LJ":
            if cardsSTR in ["AAo", "KKo", "QQo", "AKs", "AQs", "AKo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["A5s", "A4s", "AJo", "87s", "76s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in [ "AJs", "ATs", "KQs", "KJs", "KTs","AQo", "QJs", "QTs", "JTs", "JJo", "TTo","T9s", "99o","98s", "88o", "77o","66o","55o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold")

        elif rivalpositionSTR == "HJ":
            if cardsSTR in ["AAo", "KKo", "QQo", "AKs", "AQs", "AKo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["A9s", "A5s", "A4s", "A3s","AJo", "76s", "65s", "54s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in [ "AJs", "ATs", "KQs", "KJs", "KTs","AQo", "QJs", "QTs", "JTs", "JJo", "TTo","T9s", "99o","98s", "88o","87s", "77o","66o","55o","44o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("Fold")

        elif rivalpositionSTR == "CO":
            if cardsSTR in ["AAo","AKs", "AQs", "AJs", "ATs","AKo", "KKo","KQs","AQo", "QQo", "JJo", "TTo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["A9s", "A8s", "A7s", "A6s", "A5s", "A4s", "A3s", "A2s", "KJs", "KTs", "K9s","KQo","QJs", "QTs", "Q9s", "AJo","JTs", "J9s","T9s", "99o", "98s", "88o", "87s", "77o", "76s", "66o", "65s", "55o", "54s", "44o"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            else:
                print("Fold")
        elif rivalpositionSTR == "BT":
            if cardsSTR in ["AAo", "AKs", "AQs", "AJs", "ATs","AKo", "KKo", "KQs", "KJs","AQo", "KQo", "QQo","AJo", "JJo","TTo",]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["A9s", "A8s", "A7s", "A6s", "A5s", "A4s", "A3s", "A2s","KTs", "K9s","QJs", "QTs", "Q9s","KJo", "QJo","JTs", "J9s","ATo","T9s","T8s","99o", "98s", "97s","88o", "87s", "86s","77o", "76s", "66o", "65s","55o", "54s","44o","33o","22o"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            else:
                print("Fold")
    elif positionSTR == "BB":
        if rivalpositionSTR == "UT" or rivalpositionSTR == "U1":
            if cardsSTR in ["AAo","AKs","AQs","KKo","QQo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["86s","76s","75s","65s","64s","54s","43s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AJs", "ATs", "A9s", "A8s", "A7s", "A6s", "A5s", "A4s", "A3s", "A2s",
                              "AKo","KQs", "KJs", "KTs", "K9s", "K8s", "K7s", "K6s", "K5s",
                              "AQo","KQo","QJs", "QTs", "Q9s", "Q8s", "Q7s",
                              "AJo", "KJo", "QJo", "JJo", "JTs", "J9s", "J8s", "J7s",
                              "ATo", "KTo", "QTo", "JTo", "TTo", "T9s", "T8s", "T7s",
                              "99o", "98s", "97s", "96s",
                              "88o", "87s",
                              "77o",
                              "66o",
                              "55o",
                              "44o",
                              "33o",
                              "22o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("fold")
        elif rivalpositionSTR == "U2":
            if cardsSTR in ["AAo", "AKs", "AQs", "AKo" , "KKo", "QQo","JJo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["86s","85s", "76s", "75s", "74s","65s", "64s", "54s","53s", "43s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["AJs", "ATs", "A9s", "A8s", "A7s", "A6s", "A5s", "A4s", "A3s", "A2s",
                              "KQs", "KJs", "KTs", "K9s", "K8s", "K7s", "K6s", "K5s","K4s",
                              "AQo", "KQo", "QJs", "QTs", "Q9s", "Q8s", "Q7s", "Q6s",
                              "AJo", "KJo", "QJo",  "JTs", "J9s", "J8s", "J7s","J6s",
                              "ATo", "KTo", "QTo", "JTo", "TTo", "T9s", "T8s", "T7s","T6s"
                              "99o", "98s", "97s", "96s",
                              "88o", "87s",
                              "77o",
                              "66o",
                              "55o",
                              "44o",
                              "33o",
                              "22o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("fold")
        elif rivalpositionSTR == "LJ":
            if cardsSTR in ["AAo", "AKs", "AQs","AJs", "AKo" , "KKo","KQs", "QQo","JJo","TTo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["85s", "75s", "74s","65s", "64s", "54s","53s", "43s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["ATs", "A9s", "A8s", "A7s", "A6s", "A5s", "A4s", "A3s", "A2s",
                              "KJs", "KTs", "K9s", "K8s", "K7s", "K6s", "K5s", "K4s", "K3s", "K2s"
                              "AQo", "KQo", "QJs", "QTs", "Q9s", "Q8s", "Q7s", "Q6s", "Q5s", "Q4s",
                              "AJo", "KJo", "QJo",  "JTs", "J9s", "J8s", "J7s","J6s", "J5s"
                              "ATo", "KTo", "QTo", "JTo", "T9s", "T8s", "T7s","T6s", "T5s",
                              "99o", "98s", "97s", "96s", "95s"
                              "88o", "87s", "86s"
                              "77o", "76s"
                              "66o",
                              "55o",
                              "44o",
                              "33o",
                              "22o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("fold")
        elif rivalpositionSTR == "HJ":
            if cardsSTR in ["AAo", "AKs", "AQs","AJs", "AKo" , "KKo","KQs","AQo" ,"QQo","JJo","TTo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["85s","76s" , "75s", "74s","65s", "64s","63s", "54s","53s", "43s","32s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["ATs", "A9s", "A8s", "A7s", "A6s", "A5s", "A4s", "A3s", "A2s",
                              "KJs", "KTs", "K9s", "K8s", "K7s", "K6s", "K5s", "K4s", "K3s", "K2s"
                              "KQo", "QJs", "QTs", "Q9s", "Q8s", "Q7s", "Q6s", "Q5s", "Q4s",
                              "AJo", "KJo", "QJo",  "JTs", "J9s", "J8s", "J7s","J6s", "J5s"
                              "ATo", "KTo", "QTo", "JTo", "T9s", "T8s", "T7s","T6s", "T5s",
                              "99o", "98s", "97s", "96s", "95s"
                              "88o", "87s", "86s"
                              "77o",
                              "66o",
                              "55o",
                              "44o",
                              "33o",
                              "22o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("fold")
        elif rivalpositionSTR == "CO":
            if cardsSTR in ["AAo", "AKs", "AQs", "AJs", "ATs","AKo", "KKo", "KQs", "KJs","AQo", "KQo", "QQo", "QJs","AJo","JJo","TTo"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["85s","84s","76s", "75s", "74s", "73s","65s", "64s", "63s","54s", "53s", "52s","A4o","43s", "42s","A3o","32s"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["A9s", "A8s", "A7s", "A6s", "A5s", "A4s", "A3s", "A2s",
                              "KTs", "K9s", "K8s", "K7s", "K6s", "K5s", "K4s", "K3s", "K2s"
                              "QTs", "Q9s", "Q8s", "Q7s", "Q6s", "Q5s", "Q4s",
                              "KJo", "QJo",  "JTs", "J9s", "J8s", "J7s","J6s", "J5s", "J4s"
                              "ATo", "KTo", "QTo", "JTo", "T9s", "T8s", "T7s","T6s", "T5s","T4s",
                              "A9o", "K9o", "Q9o", "J9o", "T9o", "99o", "98s", "97s", "96s", "95s", "94s",
                              "A8o","98o","88o", "87s", "86s"
                              "77o",
                              "66o",
                              "A5o","55o",
                              "44o",
                              "33o",
                              "22o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("fold")
        elif rivalpositionSTR == "BT":
            if cardsSTR in ["AAo", "AKs", "AQs", "AJs", "ATs","AKo", "KKo", "KQs", "KJs","KTs","AQo", "KQo", "QQo", "QJs","QTs","AJo","JJo","TTo","99o"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["76s", "75s", "74s", "73s","Q6o","65s", "64s", "63s","K5o", "Q5o","75o","65o","54s","53s","52s","K4o","43s","42s","A3o","K3o","32s","A2o","K2o"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["A9s", "A8s", "A7s", "A6s", "A5s", "A4s", "A3s", "A2s",
                              "K9s", "K8s", "K7s", "K6s", "K5s", "K4s", "K3s", "K2s"
                              "Q9s", "Q8s", "Q7s", "Q6s", "Q5s", "Q4s",
                              "KJo", "QJo", "J9s", "J8s", "J7s", "J6s", "J5s", "J4s", "J3s", "J2s",
                              "ATo", "KTo", "QTo", "JTo", "T9s", "T8s", "T7s", "T6s", "T5s", "T4s", "T3s", "T2s",
                              "A9o", "K9o", "Q9o", "J9o", "T9o", "98s", "97s", "96s", "95s", "94s","93s", "92s"
                              "A8o", "K8o", "Q8o", "J8o", "T8o", "98o", "88o", "87s", "86s", "85s", "84s", "83s", "82s",
                              "A7o", "K7o", "Q7o", "J7o", "T7o", "97o", "87o", "77o","72s",
                              "A6o", "K6o","J6o", "T6o", "96o", "86o", "76o", "66o","62s",
                              "A5o","55o",
                              "A4o","44o",
                              "33o",
                              "22o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("fold")
        elif rivalpositionSTR == "SB":
            if cardsSTR in ["AAo", "AKs", "AQs", "AJs", "ATs","AKo", "KKo", "KQs", "KJs","KTs","AQo", "KQo", "QQo", "QJs","QTs","AJo","JJo","TTo","99o"]:
                print("3 bet for a value, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["J9s","T9s","T8s","98s","87s","76s","76o","65s","J5o","T5o","75o","65o","54s","Q4o","64o","54o","K3o","Q3o","A2o","K2o","Q2o"]:
                print("3 bet as a bluff, Bet this much -> ",3*rivalbetINT)
            elif cardsSTR in ["A9s", "A8s", "A7s", "A6s", "A5s", "A4s", "A3s", "A2s",
                              "K9s", "K8s", "K7s", "K6s", "K5s", "K4s", "K3s", "K2s"
                              "Q9s", "Q8s", "Q7s", "Q6s", "Q5s", "Q4s",
                              "KJo", "QJo", "J8s", "J7s", "J6s", "J5s", "J4s", "J3s", "J2s",
                              "ATo", "KTo", "QTo", "JTo", "T7s", "T6s", "T5s", "T4s", "T3s", "T2s",
                              "A9o", "K9o", "Q9o", "J9o", "T9o", "97s", "96s", "95s", "94s","93s", "92s"
                              "A8o", "K8o", "Q8o", "J8o", "T8o", "98o", "88o", "86s", "85s", "84s", "83s", "82s",
                              "A7o", "K7o", "Q7o", "J7o", "T7o", "97o", "87o", "77o", "75s", "74s", "73s", "72s",
                              "A6o", "K6o", "Q6o", "J6o", "T6o", "96o", "86o", "66o",  "64s", "63s", "62s",
                              "A5o", "K5o", "Q5o","55o","53s","52s"
                              "A4o","K4o","44o","43s","42s",
                              "A3o","33o","32s"
                              "22o"]:
                print("Call the raise, Call this much -> ",rivalbetINT)
            else:
                print("fold")


cardsSTR = str(input("Enter your cards (AAo,AKs) -> "))
positionSTR = str(input("Enter your 2 letter position (UT/UndertheGun,U1/UndertheGun+1,U2/UndertheGun+2, LJ/Lojack, HJ/Hijack, CO/Cutoff, BT/Button, SB/Small Blind, BB/Big Blind) -> "))
rivalpositionSTR = str(input("Enter opponents 2 letter position (UT/UndertheGun,U1/UndertheGun+1,U2/UndertheGun+2, LJ/Lojack, HJ/Hijack, CO/Cutoff, BT/Button, SB/Small Blind, BB/Big Blind) -> "))
rivalbetINT = int(input("enter the amount the opponent bet -> "))

FacingRaiseFirstIN(cardsSTR,positionSTR,rivalpositionSTR,rivalbetINT)