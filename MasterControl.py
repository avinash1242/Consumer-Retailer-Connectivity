import webbrowser
import DataMining
import MessageExchange

figure=int(input("Are you sure you want to run this (0/1) : "))
if figure == 1 :

    webbrowser.open('http://google.co.kr', new=2)

    DMO = DataMining.launchDM("food.txt", 50, 50)
    print (DMO)
    MessageExchange.launchME(DMO)

