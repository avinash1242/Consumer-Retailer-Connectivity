#   AV
#   Hardcoded message retrieval and some math!


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

        keydata = "There is very good chance your customers will buy the below items when they buy "+text+"\n\n"

        for i in x :

            if text == i :
                keydata = keydata + y[j] + " - " + cxy[j]
                xtext=sx[j]
                count += 1
            j += 1

        if count == 0 :

            return("There is a "+xtext+"chance that your customers will buy "+text+" everytime they shop at your store.")

        return (keydata+"\nThere is a "+xtext+"chance that your customers will buy "+text+" everytime they shop at your store.")



    def GeneralQ() :


        if "hello" in text or "Hello" in text:
            return ("Hi "+name+"!")

        elif "cool" in text or "Cool" in text:
            return ("Yeah right!\nI know")

        elif "Shit" in text or "shit" in text:
            return ("Yeah, this is some cool shit!")

        elif "Okay" in text or "okay" in text:
            return ("Don't Settle, you can ask me more!\nTry 'Help'")

        elif "haha" in text or "Haha" in text :
            return ("hehehe!")

        elif "hehe" in text or "Hehe" in text :
            return ("hahaha!")

        elif "Nice" in text or "nice" in text :
            return ("Thanks "+name)

        elif text == "/start":
            return ("Hi " + name+"\nHope you are doing great!\n\nI can help you with your queries regarding your customers Transactions.\nIf in case you do not know what to message, try messaging 'help' and i will message you back the options available.\n\nLets get started!")

        elif "team" in text or "Team" in text :
            return ("Mr. Avinash Varma! Ohh Yeah!!!")

        elif "Great" in text or "great" in text :
            return ("Thanks.\nI can do a lot more! Try 'Help'")

        elif text == "End" or text == "end":
            return ("Bye "+name+"!\nWish to see you back soon.I will always be here to help you")

        elif "Bye" in text or "bye" in text :
            return ("Good Bye "+name+",Just say 'End', and we will be done for good!")

        elif "Support" in text or "support"in text :
            return ("Consider a basket containing 10 items.\n( 5 Apples, 3 Eggs, 2 Pens )\n\nSupport of any precise item say apple can be 5 as mentioned. Support is the frequency or the number of times it has repeated in given dataset. Since we have 5 apples in our basket, we have a 50% chance of finding it.\nTherefore, Support percentage is 50.")

        elif "Confidence" in text or "confidence" in text:
            return ("Consider two baskets containing 10 items each.\n( 5 Apples, 3 Eggs, 2 Pens )\n( 3 Eggs, 2 Carrots, 5 Apples )\n\nWhen we observe closely, we find that every time there are apples in the basket, there are also eggs.\nBy this we can say, that there is a Confidence of 100%,In finding en egg when we have an apple in the basket.")

        elif "Help"  in text or "help" in text:
            return ("Hey "+name+"!\n\nEnter Keys to get a list of keywords\nYou can also learn what is Support, Confidence, Visual Design, Store Setting.\nMessage 'end' to say good bye")

        elif "hi" in text or "Hi" in text :
            return ("Hello " + name + "!")

        else:
            return ("I don't know that,Sorry!\nTry 'Help'")



    def strig() :

        if trig == 8:
            return (" Hello " + name + " !\nWe have analysed your data and could not recognise any patterns becuse the amount of transaction data you have given is insufficient\nPlease come back with a bit more data and we are always here to help you.\nThanks,bye!")



    while i < lines :

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


    elif "Keys" in text or "keys" in text or "Key" in text or "key" in text :

        return ("Hey, I found some specific keywords which i feel will be interesting to you!\n\n{k}\n\nJust type in a keyword from the keys and i will tell you all about it.".format(k=keys))


    if trig > 1 :

        return (strig())


    return (GeneralQ())
