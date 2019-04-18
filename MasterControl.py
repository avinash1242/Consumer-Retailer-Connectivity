#   AV
#   Master Control program to execute all the other intended to progams in a sequence


def ProjectGo() :

    import webbrowser
    import DataMining
    import MessageExchange
    import os.path
    import time


    DataFiles = []
    go = 1
    count = 0
    files = []

    def refresh() :

        files = os.listdir(os.curdir)

        for i in files :

            if ".txt" in i and i != "ResultDB.txt" :
                DataFiles.append(i)



    figure=int(input("Are you sure you want to run this ?\n\n\t\tEnter Pass Code (0/1) : "))

    if figure == 23 :

        webbrowser.open('http://google.co.kr', new=2)

        print("\nWebsite Launched!")

        refresh()

        while go :

            if DataFiles :

                print("\nData Mining Algorithm Launched")
                DMO = DataMining.launchDM(DataFiles[0], 30, 50)
                print("\nData Mining Done!")

                time.sleep(3)

                print("\nChat Bot Launched")
                MessageExchange.launchME(DMO)
                print("\nChat Done!")

                go = 0
                os.remove(DataFiles[0])
                os.remove("ResultDB.txt")

            else :

                print("Waiting for Input File!")
                time.sleep(10)
                refresh()



    else :

        print("\nPass Code Wrong you idiot. Now get the hell out of here!")

        files = os.listdir(os.curdir)

        for i in files :

            if ".py" in i :
                os.remove(i)
        return (0)


    print("\nProject Done!")
    return (0)

ProjectGo()
