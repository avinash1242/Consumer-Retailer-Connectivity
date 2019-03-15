import webbrowser
import DataMining
import MessageExchange
import os.path


figure=int(input("Are you sure you want to run this (0/1) : "))

if figure == 1 :

   # webbrowser.open('http://google.co.kr', new=2)

    if os.path.exists('Data.txt') == True :

        DMO = DataMining.launchDM("Data.txt",40, 50)
        MessageExchange.launchME(DMO)
        print("Done")

    else :

        print(" Input Data file not found !")