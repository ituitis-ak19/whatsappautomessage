import pywhatkit as kit
import pandas as pd

s = pd.read_csv('numara.csv')
total_rows = int(s.size / 3)

def f_option():
    option = str(input("Do you want to send message to all your contacts ? Y/N"))
    if option == 'Y' or option == 'y':
        time=str(input("When will you send ? (XX.XX)"))
        firsttwo = int(time[0:2])
        lasttwo = int(time[3:5])
        for i in range(total_rows):
            numara = '+' + str(s['Phone_Numbers'][i])
            kit.sendwhatmsg(numara, "Your Message",firsttwo,lasttwo)
            lasttwo=lasttwo+1
    elif option == 'N' or option == 'n':
        count = int(input("How many contacts dou want to send message ?"))
        names = []
        for x in range(count):
            namex = str(input("What is the name of " + str(x+1) + "th contact ?"))
            names.append(namex)

        time = str(input("When will you send ? (XX.XX)"))
        firsttwo = int(time[0:2])
        lasttwo = int(time[3:5])

        for x in names:
            for i in range(total_rows):
                if str(x) == str(s['Names'][i]):
                    numara = '+' + str(s['Phone_Numbers'][i])
                    kit.sendwhatmsg(numara, "Your Message", firsttwo, lasttwo)
                    lasttwo = lasttwo + 1
    else:
        print("Wrong Input")
        f_option()

f_option()

