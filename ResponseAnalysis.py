def launchRA(text,name,trig):

    lines = 0
    lines = len(open("ResultDB.txt").readlines())
    x = [];
    y = [];
    sx = [];
    sxy = [];
    cxy = [];
    keys = [];
    i = 0


    def word(p) :
        xp = p.split("'")
        i = 1
        a = xp[i]

        while i < len(xp) - 2:
            i += 2
            a = a + "," + xp[i]

        return (a)


    def KeyWord (text) :
        j = 0
        count = 0
        xtext = 0

        keydata = "There is good chance your customers will buy the below items when they buy "+text+"\n\n"
        for i in x :

            if text == i :
                keydata = keydata + y[j] + " - " + cxy[j]
                xtext=sx[j]
                count += 1
            j += 1

        if count == 0 :
            return("There is a "+xtext+" chance that your customers will buy "+text+" everytime they shop at your store.")

        return (keydata+"\nThere is a "+xtext+"chance that your customers will buy "+text+" everytime they shop at your store.")


    def GeneralQ() :

        if text == "hi" or text == "Hi":
            return ("Hello!")

        elif text == "hello" or text == "Hello":
            return ("Hi!")

        elif text == "cool" or text == "Cool":
            return ("Yeah right!\nI know")

        elif text == "Okay" or text == "okay":
            return ("Don't Settle, you can ask me more!")

        elif "haha" in text or "Haha" in text :
            return ("hehehe!")

        elif "hehe" in text or "Hehe" in text :
            return ("hahaha!")

        elif text == "/start":
            return ("Hi " + name+"\nHope you are doing great!\n\nI can help you with your queries regarding your customers Transactions.\nIf in case you do not know what to message, try messaging 'help' and i will message you back the options available.\n\nLets get started!")

        elif text == "Our Team" or text == "Our team" or text == "our team":
            return "Avinash Varma"

        elif text == "End" or text == "end":
            return ("Bye "+name+"!\nWish to see you back soon.I will always be here to help you")

        elif text == "Help" or text == "help":
            return ("Hey "+name+"!\n\nEnter 1 to get a list of keywords\nEnter 2 to get Support Priorities\nEnter 3 to get Confidence Priorities\nEnter 'end' to say good bye")

        else:
            return ("I don't know that,Sorry!\nTry : Help")

    def strig() :

        if trig == 8:
            return (" Hello " + name + " !\nWe have analysed your data and could not recognise any patterns becuse the amount of transaction data you have given is insufficient\nPlease come back with a bit more data and we are always here to help you.\nThanks,bye!")

    while i < lines:
        sx.append(open("ResultDB.txt", "r").readlines()[i].split(" ")[4])
        sxy.append(open("ResultDB.txt", "r").readlines()[i + 1].split(" ")[6])
        cxy.append(open("ResultDB.txt", "r").readlines()[i + 2].split(" ")[6])
        f = open('ResultDB.txt')
        line = f.readlines()
        parts = line[i+3].split("------>")
        x.append(word(parts[0]))
        y.append(word(parts[1]))
        i += 5

    for i in x :
        if i in keys :
            continue
        else :
            keys.append(i)



    if text in keys :
        keydata = KeyWord(text)
        return(keydata)


    elif text == "1" :
        return ("The below are specific keywords we found in your data which we feel you might be interested!\n\n{k}\n\nJust type in a word from the key words to know more about it.".format(k=keys))


    if trig > 1 :
        return (strig())


    return (GeneralQ())
