import datefinder
import winsound
import datetime


def Alarm(text):
    dTimeA = datefinder.find_dates(text)
    for mat in dTimeA:
        print(mat)
    stringA = str(mat)
    timeA = stringA[11:]
    hourA = timeA[:-6]
    hourA = int(hourA)
    minA = timeA[3:-3]
    minA = int(minA)

    while True:

        if hourA == datetime.datetime.now().hour:
            if minA == datetime.datetime.now().minute:
                winsound.PlaySound(
                    'YOUR OWN MUSIC PATH FOR ALARM TUNE', winsound.SND_LOOP)
                print("Alarm is running")
            elif minA < datetime.datetime.now().minute:
                print("Alarm time is gone")
                break

        if hourA > datetime.datetime.now().hour:
            if minA == datetime.datetime.now().minute and hourA == datetime.datetime.now().hour:
                winsound.PlaySound(
                    'YOUR OWN MUSIC PATH FOR ALARM TUNE', winsound.SND_LOOP)
                print("Alarm is running")
            elif minA < datetime.datetime.now().minute and hourA == datetime.datetime.now().hour:
                print("Alarm time is gone")
                break

        if hourA < datetime.datetime.now().hour:
            print("Your Alarm time is gone")
            break
