import datetime
import time
import sys

BP1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
BP2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
BP3 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
BP4 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

BL1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
BL2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
BL3 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
BL4 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

EP1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
EP2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
EP3 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
EP4 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

EL1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
EL2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
EL3 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
EL4 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

PEN01 = [BP1, EP1]
PEN02 = [BP2, EP2]
PEN03 = [BP3, EP3]
PEN04 = [BP4, EP4]


LAN01 = [BL1, EL1]
LAN02 = [BL2, EL2]
LAN03 = [BL3, EL3]
LAN04 = [BL4, EL4]

PF = [PEN01, PEN02, PEN03, PEN04]
LF = [LAN01, LAN02, LAN03, LAN04]

F = [PF, LF]

currentday = datetime.date.today()

def bclass(d,s, feid):
    print("----------------------------------------------------------------------------------")
    print("| Ferry ID:", feid, "                                             Date:", currentday.strftime('%d-%m-%Y'), " |")
    print("----------------------------------------------------------------------------------")
    print("| 	                        Business class 	                                 |")
    print("----------------------------------------------------------------------------------")
    print("1: ", "\t", F[d][s][0][0][0], "\t", "\t", F[d][s][0][0][1], "\t", "\t", F[d][s][0][0][2], "\t", "\t", F[d][s][0][0][3], "\t", "\t", F[d][s][0][0][4], "\t", "|")
    print("----------------------------------------------------------------------------------")
    print("2: ", "\t", F[d][s][0][1][0], "\t", "\t", F[d][s][0][1][1], "\t", "\t", F[d][s][0][1][2], "\t", "\t", F[d][s][0][1][3], "\t", "\t", F[d][s][0][1][4], "\t", "|")
    print("----------------------------------------------------------------------------------")

def eclass(d,s, feid):
    print("----------------------------------------------------------------------------------")
    print("| Ferry ID:", feid, "                                             Date:", currentday.strftime('%d-%m-%Y'), " |")
    print("----------------------------------------------------------------------------------")
    print("| 	                        Economy class 	                                 |")
    print("----------------------------------------------------------------------------------")
    print("1: ", "\t", F[d][s][1][0][0], "\t", "\t", F[d][s][1][0][1], "\t", "\t", F[d][s][1][0][2], "\t", "\t", F[d][s][1][0][3], "\t", "\t", F[d][s][1][0][4], "\t", "|")
    print("2: ", "\t", F[d][s][1][1][0], "\t", "\t", F[d][s][1][1][1], "\t", "\t", F[d][s][1][1][2], "\t", "\t", F[d][s][1][1][3], "\t", "\t", F[d][s][1][1][4], "\t", "|")
    print("3: ", "\t", F[d][s][1][2][0], "\t", "\t", F[d][s][1][2][1], "\t", "\t", F[d][s][1][2][2], "\t", "\t", F[d][s][1][2][3], "\t", "\t", F[d][s][1][2][4], "\t", "|")
    print("4: ", "\t", F[d][s][1][3][0], "\t", "\t", F[d][s][1][3][1], "\t", "\t", F[d][s][1][3][2], "\t", "\t", F[d][s][1][3][3], "\t", "\t", F[d][s][1][3][4], "\t", "|")
    print("5: ", "\t", F[d][s][1][4][0], "\t", "\t", F[d][s][1][4][1], "\t", "\t", F[d][s][1][4][2], "\t", "\t", F[d][s][1][4][3], "\t", "\t", F[d][s][1][4][4], "\t", "|")
    print("6: ", "\t", F[d][s][1][5][0], "\t", "\t", F[d][s][1][5][1], "\t", "\t", F[d][s][1][5][2], "\t", "\t", F[d][s][1][5][3], "\t", "\t", F[d][s][1][5][4], "\t", "|")
    print("7: ", "\t", F[d][s][1][6][0], "\t", "\t", F[d][s][1][6][1], "\t", "\t", F[d][s][1][6][2], "\t", "\t", F[d][s][1][6][3], "\t", "\t", F[d][s][1][6][4], "\t", "|")
    print("8: ", "\t", F[d][s][1][7][0], "\t", "\t", F[d][s][1][7][1], "\t", "\t", F[d][s][1][7][2], "\t", "\t", F[d][s][1][7][3], "\t", "\t", F[d][s][1][7][4], "\t", "|")
    print("----------------------------------------------------------------------------------")

def wferry(d,s, feid):
    print("----------------------------------------------------------------------------------")
    print("| Ferry ID:", feid, "                                             Date:", currentday.strftime('%d-%m-%Y'), " |")
    print("----------------------------------------------------------------------------------")
    print("| 	                        Business class 	                                 |")
    print("----------------------------------------------------------------------------------")
    print("1: ", "\t", F [d][s][0][0][0], "\t", "\t", F [d][s][0][0][1], "\t", "\t", F [d][s][0][0][2], "\t", "\t", F [d][s][0][0][3], "\t", "\t", F [d][s][0][0][4], "\t", "|")
    print("----------------------------------------------------------------------------------")
    print("2: ", "\t", F [d][s][0][1][0], "\t", "\t", F [d][s][0][1][1], "\t", "\t", F [d][s][0][1][2], "\t", "\t", F [d][s][0][1][3], "\t", "\t", F [d][s][0][1][4], "\t", "|")
    print("----------------------------------------------------------------------------------")
    print("| 	                        Economy class 	                                 |")
    print("----------------------------------------------------------------------------------")
    print("1: ", "\t", F [d][s][1][0][0], "\t", "\t", F [d][s][1][0][1], "\t", "\t", F [d][s][1][0][2], "\t", "\t", F [d][s][1][0][3], "\t", "\t", F [d][s][1][0][4], "\t", "|")
    print("2: ", "\t", F [d][s][1][1][0], "\t", "\t", F [d][s][1][1][1], "\t", "\t", F [d][s][1][1][2], "\t", "\t", F [d][s][1][1][3], "\t", "\t", F [d][s][1][1][4], "\t", "|")
    print("3: ", "\t", F [d][s][1][2][0], "\t", "\t", F [d][s][1][2][1], "\t", "\t", F [d][s][1][2][2], "\t", "\t", F [d][s][1][2][3], "\t", "\t", F [d][s][1][2][4], "\t", "|")
    print("4: ", "\t", F [d][s][1][3][0], "\t", "\t", F [d][s][1][3][1], "\t", "\t", F [d][s][1][3][2], "\t", "\t", F [d][s][1][3][3], "\t", "\t", F [d][s][1][3][4], "\t", "|")
    print("5: ", "\t", F [d][s][1][4][0], "\t", "\t", F [d][s][1][4][1], "\t", "\t", F [d][s][1][4][2], "\t", "\t", F [d][s][1][4][3], "\t", "\t", F [d][s][1][4][4], "\t", "|")
    print("6: ", "\t", F [d][s][1][5][0], "\t", "\t", F [d][s][1][5][1], "\t", "\t", F [d][s][1][5][2], "\t", "\t", F [d][s][1][5][3], "\t", "\t", F [d][s][1][5][4], "\t", "|")
    print("7: ", "\t", F [d][s][1][6][0], "\t", "\t", F [d][s][1][6][1], "\t", "\t", F [d][s][1][6][2], "\t", "\t", F [d][s][1][6][3], "\t", "\t", F [d][s][1][6][4], "\t", "|")
    print("8: ", "\t", F [d][s][1][7][0], "\t", "\t", F [d][s][1][7][1], "\t", "\t", F [d][s][1][7][2], "\t", "\t", F [d][s][1][7][3], "\t", "\t", F [d][s][1][7][4], "\t", "|")
    print("----------------------------------------------------------------------------------")

def ticket(ferrid, seat1, destination, time1, class1, source):
    name = input("Please enter your name: ")
    print("""            ================================================================================
            ----*************************************************************************----
            | - *                                                                       * - |
            | - * Ferry ID: """, ferrid, """                                  Date: """, currentday.strftime('%d-%m-%Y'), """ * - |
            | - *                                                                       * - |
            | - * Full name: """, name, "\t", "\t", "\t", "\t", "\t", """Time: """, time1,  """ * - |
            | - *                                                                       * - |
            | - * Seat number: """, seat1, """                                  Class: """, class1, """ * - |
            | - *                                                                       * - |
            | - * Destination: """, destination, """                              Source: """, source,""" * - |
            | - *                                                                       * - |
            ----*************************************************************************----
            =================================================================================""")
    tick = open("Ticket.txt", "w")
    tick.write("Ferry ID: " + str(ferrid) + "     " + "Date: " + str(currentday.strftime('%d-%m-%Y')))
    tick = open("Ticket.txt", "a")
    tick.write("\nFull name: " + str(name) + "     " + "Time: " + str(time1))
    tick.write("\nSeat number: " + str(seat1) + "     " + "Class: " + str(class1))
    tick.write("\nDestination: " + str(destination) + "     " + "Source: " + str(source))
    tick.close()
    
def mainmenu():
    print("                                   ")
    print("  █   █ █▀▀ █   █▀▀ █▀▀█ █▀▄▀█ █▀▀ ")
    print("  █ █ █ █▀▀ █   █   █  █ █ ▀ █ █▀▀ ")
    print("  █▄▀▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀   ▀ ▀▀▀ ")
    print("                                   ")

    m = input("""Please select:
                                P to Purchasing ticket
                                V to Viewing Seating Arrangement
                                Q to Quit the System
                                """).upper()
    if m == "P":
        pselected()
    elif m == "V":
        vselected()
    elif m == "Q":
        print("                                  ")
        print("█▀▀█ █▀▀█ █▀▀█ █▀▀▄ █▀▀▄ █  █ █▀▀ ")
        print("█ ▄▄ █  █ █  █ █  █ █▀▀▄ █▄▄█ █▀▀ ")
        print("█▄▄█ ▀▀▀▀ ▀▀▀▀ ▀▀▀  ▀▀▀  ▄▄▄█ ▀▀▀ ")
        print("                                  ")
        time.sleep(3)
        sys.exit()
    else:
        print("Invalid entry")
        mainmenu()

def mainmenu2():
    m = input("""Please select:
                                P to Purchasing ticket
                                V to Viewing Seating Arrangement
                                Q to Quit the System
                                """).upper()
    if m == "P":
        pselected()
    elif m == "V":
        vselected()
    elif m == "Q":
        print("                                  ")
        print("█▀▀█ █▀▀█ █▀▀█ █▀▀▄ █▀▀▄ █  █ █▀▀ ")
        print("█ ▄▄ █  █ █  █ █  █ █▀▀▄ █▄▄█ █▀▀ ")
        print("█▄▄█ ▀▀▀▀ ▀▀▀▀ ▀▀▀  ▀▀▀  ▄▄▄█ ▀▀▀ ")
        print("                                  ")
        time.sleep(3)
        sys.exit()
    else:
        print("Invalid entry")
        mainmenu2()

def pselected():
    x = input("""Please select:
                                B to Purchase a Ticket for Business class
                                E to Purchase a ticket for Economy class
                                M to Return to Mainmenu
                                """).upper()
    if x == "B":
        bselected()
    elif x == "E":
        eselected()
    elif x == "M":
        mainmenu2()
    else:
        print("Invalid Entry")
        pselected()

def vselected():
    print("1.", "\t", "PEN01", "\t", "10:00AM")
    print("2.", "\t", "PEN02", "\t", "11:00AM")
    print("3.", "\t", "PEN03", "\t", "12:00PM")
    print("4.", "\t", "PEN04", "\t", "1:00PM")
    print("5.", "\t", "LAN01", "\t", "2:00PM")
    print("6.", "\t", "LAN02", "\t", "3:00PM")
    print("7.", "\t", "LAN03", "\t", "4:00PM")
    print("8.", "\t", "LAN04", "\t", "5:00PM")
    s1 = input("Please select ferry ID, (e.g. 5): ")
    if s1 == "1":
        wferry(0, 0, "PEN01")
        print("Loading...")
        time.sleep(4)
        mainmenu2()
    elif s1 == "2":
        wferry(0, 1, "PEN02")
        print("Loading...")
        time.sleep(4)
        mainmenu2()
    elif s1 == "3":
        wferry(0, 2, "PEN03")
        print("Loading...")
        time.sleep(4)
        mainmenu2()
    elif s1 == "4":
        wferry(0, 3, "PEN04")
        print("Loading...")
        time.sleep(4)
        mainmenu2()
    elif s1 == "5":
        wferry(1, 0, "LAN01")
        print("Loading...")
        time.sleep(4)
        mainmenu2()
    elif s1 == "6":
        wferry(1, 1, "LAN02")
        print("Loading...")
        time.sleep(4)
        mainmenu2()
    elif s1 == "7":
        wferry(1, 2, "LAN03")
        print("Loading...")
        time.sleep(4)
        mainmenu2()
    elif s1 == "8":
        wferry(1, 3, "LAN04")
        print("Loading...")
        time.sleep(4)
        mainmenu2()
    else:
        print("Invalid entry")
        vselected()

def bselected():
    y = input("""Please select:
                                F to select FerryID
                                T to select time
                                """).upper()
    if y == "F":
        print("1.", "\t", "PEN01", "\t", "10:00AM")
        print("2.", "\t", "PEN02", "\t", "11:00AM")
        print("3.", "\t", "PEN03", "\t", "12:00PM")
        print("4.", "\t", "PEN04", "\t", "1:00PM")
        print("5.", "\t", "LAN01", "\t", "2:00PM")
        print("6.", "\t", "LAN02", "\t", "3:00PM")
        print("7.", "\t", "LAN03", "\t", "4:00PM")
        print("8.", "\t", "LAN04", "\t", "5:00PM")
        x = input("""*Note ferries begin with "PEN" is going from Langkawi to Penang,
                      ferries begin with "LAN" is going from Penang to Langkawi*
                      Please select FerryID (e.g. 5):
                      """)
        if x == "1":
            business(0, 0, "PEN01", BP1, "PEN01", "Penang", "10:00AM", "Langkawi")
        elif x == "2":
            business(0, 1, "PEN02", BP2, "PEN02", "Penang", "11:00AM", "Langkawi")
        elif x == "3":
            business(0, 2, "PEN03", BP3, "PEN03", "Penang", "12:00PM", "Langkawi")
        elif x == "4":
            business(0, 3, "PEN04", BP4, "PEN04", "Penang", "1:00PM", "Langkawi")
        elif x == "5":
            business(1, 0, "LAN01", BL1, "LAN01", "Langkawi", "2:00PM", "Penang")
        elif x == "6":
            business(1, 1, "LAN02", BL2, "LAN02", "Langkawi", "3:00PM", "Penang")
        elif x == "7":
            business(1, 2, "LAN03", BL3, "LAN03", "Langkawi", "4:00PM", "Penang")
        elif x == "8":
            business(1, 3, "LAN04", BL4, "LAN04", "Langkawi", "5:00PM", "Penang")
        else:
            print("Invalid Entry")
            bselected()


    elif y == "T":
        print("1. ", "\t", "10:00AM", "\t", "PEN01")
        print("2. ", "\t", "11:00AM", "\t", "PEN02")
        print("3. ", "\t", "12:00PM", "\t", "PEN03")
        print("4. ", "\t", "1:00PM", "\t", "PEN04")
        print("5. ", "\t", "2:00PM", "\t", "LAN01")
        print("6. ", "\t", "3:00PM", "\t", "LAN02")
        print("7. ", "\t", "4:00PM", "\t", "LAN03")
        print("8. ", "\t", "5:00PM", "\t", "LAN04")
        x = input("""*Note ferries begin with "PEN" is going from Langkawi to Penang,
                      ferries begin with "LAN" is going from Penang to Langkawi*
                      Please select FerryID (e.g. 5):
                      """)
        if x == "1":
            business(0, 0, "PEN01", BP1, "PEN01", "Penang", "10:00AM", "Langkawi")
        elif x == "2":
            business(0, 1, "PEN02", BP2, "PEN02", "Penang", "11:00AM", "Langkawi")
        elif x == "3":
            business(0, 2, "PEN03", BP3, "PEN03", "Penang", "12:00PM", "Langkawi")
        elif x == "4":
            business(0, 3, "PEN04", BP4, "PEN04", "Penang", "1:00PM", "Langkawi")
        elif x == "5":
            business(1, 0, "LAN01", BL1, "LAN01", "Langkawi", "2:00PM", "Penang")
        elif x == "6":
            business(1, 1, "LAN02", BL2, "LAN02", "Langkawi", "3:00PM", "Penang")
        elif x == "7":
            business(1, 2, "LAN03", BL3, "LAN03", "Langkawi", "4:00PM", "Penang")
        elif x == "8":
            business(1, 3, "LAN04", BL4, "LAN04", "Langkawi", "5:00PM", "Penang")
        else:
            print("Invalid Entry")
            bselected()
    else:
        print("Invalid entry")
        bselected()

def eselected():
    y = input("""Please select:
                                F to select FerryID
                                T to select time
                                """).upper()
    if y == "F":
        print("1.", "\t", "PEN01", "\t", "10:00AM")
        print("2.", "\t", "PEN02", "\t", "11:00AM")
        print("3.", "\t", "PEN03", "\t", "12:00PM")
        print("4.", "\t", "PEN04", "\t", "1:00PM")
        print("5.", "\t", "LAN01", "\t", "2:00PM")
        print("6.", "\t", "LAN02", "\t", "3:00PM")
        print("7.", "\t", "LAN03", "\t", "4:00PM")
        print("8.", "\t", "LAN04", "\t", "5:00PM")
        x = input("""*Note ferries begin with "PEN" is going from Langkawi to Penang,
                      ferries begin with "LAN" is going from Penang to Langkawi*
                      Please select FerryID (e.g. 5):
                      """)
        if x == "1":
            economy(0, 0, "PEN01", EP1, "PEN01", "Penang", "10:00AM", "Langkawi")
        elif x == "2":
            economy(0, 1, "PEN02", EP2, "PEN02", "Penang", "11:00AM", "Langkawi")
        elif x == "3":
            economy(0, 2, "PEN03", EP3, "PEN03", "Penang", "12:00PM", "Langkawi")
        elif x == "4":
            economy(0, 3, "PEN04", EP4, "PEN04", "Penang", "1:00PM", "Langkawi")
        elif x == "5":
            economy(1, 0, "LAN01", EL1, "LAN01", "Langkawi", "2:00PM", "Penang")
        elif x == "6":
            economy(1, 1, "LAN02", EL2, "LAN02", "Langkawi", "3:00PM", "Penang")
        elif x == "7":
            economy(1, 2, "LAN03", EL3, "LAN03", "Langkawi", "4:00PM", "Penang")
        elif x == "8":
            economy(1, 3, "LAN04", EL4, "LAN04", "Langkawi", "5:00PM", "Penang")
        else:
            print("Invalid Entry")
            eselected()


    elif y == "T":
        print("1. ", "\t", "10:00AM", "\t", "PEN01")
        print("2. ", "\t", "11:00AM", "\t", "PEN02")
        print("3. ", "\t", "12:00PM", "\t", "PEN03")
        print("4. ", "\t", "1:00PM", "\t", "PEN04")
        print("5. ", "\t", "2:00PM", "\t", "LAN01")
        print("6. ", "\t", "3:00PM", "\t", "LAN02")
        print("7. ", "\t", "4:00PM", "\t", "LAN03")
        print("8. ", "\t", "5:00PM", "\t", "LAN04")
        x = input("""*Note ferries begin with "PEN" is going from Langkawi to Penang,
                      ferries begin with "LAN" is going from Penang to Langkawi*, "\n",
                      Please select FerryID (e.g. 5):
                      """)
        if x == "1":
            economy(0, 0, "PEN01", EP1, "PEN01", "Penang", "10:00AM", "Langkawi")
        elif x == "2":
            economy(0, 1, "PEN02", EP2, "PEN02", "Penang", "11:00AM", "Langkawi")
        elif x == "3":
            economy(0, 2, "PEN03", EP3, "PEN03", "Penang", "12:00PM", "Langkawi")
        elif x == "4":
            economy(0, 3, "PEN04", EP4, "PEN04", "Penang", "1:00PM", "Langkawi")
        elif x == "5":
            economy(1, 0, "LAN01", EL1, "LAN01", "Langkawi", "2:00PM", "Penang")
        elif x == "6":
            economy(1, 1, "LAN02", EL2, "LAN02", "Langkawi", "3:00PM", "Penang")
        elif x == "7":
            economy(1, 2, "LAN03", EL3, "LAN03", "Langkawi", "4:00PM", "Penang")
        elif x == "8":
            economy(1, 3, "LAN04", EL4, "LAN04", "Langkawi", "5:00PM", "Penang")
        else:
            print("Invalid Entry")
            eselected()
    else:
        print("Invalid Entry")
        eselected()


    

def business(d, s, feid, listb, id, dest, ts, sour):
    bclass(d, s, feid)
    bsr = input ("Please select your row (e.g. enter 1 or 2: ")
    bsc = input ("Choose your prefered seat (e.g. enter 1 for the first seat from the left): ")
    if bsr == "1" and bsc == "1":
        if listb == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in business class are taken.
            Please choose different class or trip""")
            pselected()
        elif listb[0][0] == 1:
            print ("Unfortunately seat is taken.")
            business(d, s, feid, listb, id, dest, ts, sour)
        elif listb [0][0] != 1:
            listb [0][0] = 1
            print ("Seat is successfully booked.")
            ticket(id, "B11", dest, ts, "Business", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            business(d, s, feid, listb, id, dest, ts, sour)
    elif bsr == "1" and bsc == "2":
        if listb == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in business class are taken.
            Please choose different class or trip""")
            pselected()
        elif listb[0][1] == 1:
            print ("Unfortunately seat is taken.")
            business(d, s, feid, listb, id, dest, ts, sour)
        elif listb [0][1] != 1:
            listb [0][1] = 1
            print ("Seat is successfully booked.")
            ticket(id, "B12", dest, ts, "Business", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            business(d, s, feid, listb, id, dest, ts, sour)
    elif bsr == "1" and bsc == "3":
        if listb == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in business class are taken.
            Please choose different class or trip""")
            pselected()
        elif listb[0][2] == 1:
            print ("Unfortunately seat is taken.")
            business(d, s, feid, listb, id, dest, ts, sour)
        elif listb [0][2] != 1:
            listb [0][2] = 1
            print ("Seat is successfully booked.")
            ticket(id, "B13", dest, ts, "Business", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            business(d, s, feid, listb, id, dest, ts, sour)
    elif bsr == "1" and bsc == "4":
        if listb == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in business class are taken.
            Please choose different class or trip""")
            pselected()
        elif listb[0][3] == 1:
            print ("Unfortunately seat is taken.")
            business(d, s, feid, listb, id, dest, ts, sour)
        elif listb [0][3] != 1:
            listb [0][3] = 1
            print ("Seat is successfully booked.")
            ticket(id, "B14", dest, ts, "Business", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            business(d, s, feid, listb, id, dest, ts, sour)
    elif bsr == "1" and bsc == "5":
        if listb == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in business class are taken.
            Please choose different class or trip""")
            pselected()
        elif listb[0][4] == 1:
            print ("Unfortunately seat is taken.")
            business(d, s, feid, listb, id, dest, ts, sour)
        elif listb [0][4] != 1:
            listb [0][4] = 1
            print ("Seat is successfully booked.")
            ticket(id, "B15", dest, ts, "Business", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            business(d, s, feid, listb, id, dest, ts, sour)

    elif bsr == "2" and bsc == "1":
        if listb == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in business class are taken.
            Please choose different class or trip""")
            pselected()
        elif listb[1][0] == 1:
            print ("Unfortunately seat is taken.")
            business(d, s, feid, listb, id, dest, ts, sour)
        elif listb[1][0] != 1:
            listb[1][0] = 1
            print ("Seat is successfully booked.")
            ticket(id, "B21", dest, ts, "Business", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            business(d, s, feid, listb, id, dest, ts, sour)
    elif bsr == "2" and bsc == "2":
        if listb == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in business class are taken.
            Please choose different class or trip""")
            pselected()
        elif listb[1][1] == 1:
            print ("Unfortunately seat is taken.")
            business(d, s, feid, listb, id, dest, ts, sour)
        elif listb[1][1] != 1:
            listb[1][1] = 1
            print ("Seat is successfully booked.")
            ticket(id, "B22", dest, ts, "Business", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            business(d, s, feid, listb, id, dest, ts, sour)
    elif bsr == "2" and bsc == "3":
        if listb == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in business class are taken.
            Please choose different class or trip""")
            pselected()
        elif listb[1][2] == 1:
            print ("Unfortunately seat is taken.")
            business(d, s, feid, listb, id, dest, ts, sour)
        elif listb[1][2] != 1:
            listb[1][2] = 1
            print ("Seat is successfully booked.")
            ticket(id, "B23", dest, ts, "Business", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            business(d, s, feid, listb, id, dest, ts, sour)
    elif bsr == "2" and bsc == "4":
        if listb == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in business class are taken.
            Please choose different class or trip""")
            pselected()
        elif listb[1][3] == 1:
            print ("Unfortunately seat is taken.")
            business()
        elif listb[1][3] != 1:
            listb[1][3] = 1
            print ("Seat is successfully booked.")
            ticket(id, "B24", dest, ts, "Business", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            business(d, s, feid, listb, id, dest, ts, sour)
    elif bsr == "2" and bsc == "5":
        if listb == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in business class are taken.
            Please choose different class or trip""")
            pselected()
        elif listb[1][4] == 1:
            print ("Unfortunately seat is taken.")
            business(d, s, feid, listb, id, dest, ts, sour)
        elif listb[1][4] != 1:
            listb[1][4] = 1
            print ("Seat is successfully booked.")
            ticket(id, "B25", dest, ts, "Business", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            business(d, s, feid, listb, id, dest, ts, sour)
    else:
        print("Invalid Entry")
        business(d, s, feid, listb, id, dest, ts, sour)
    

def economy(d, s, feid, liste, id, dest, ts, sour):
    eclass(d, s, feid)
    esr = input ("Please select your row: ")
    esc = input ("Choose your prefered seat (e.g. Enter 1 for the first seat from the left): ")
    if esr == "1" and esc == "1":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[0][0] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [0][0] != 1:
            liste [0][0] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E11", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "1" and esc == "2":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[0][1] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [0][1] != 1:
            liste [0][1] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E12", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "1" and esc == "3":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[0][2] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [0][2] != 1:
            liste [0][2] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E13", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "1" and esc == "4":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[0][3] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [0][3] != 1:
            liste [0][3] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E14", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "1" and esc == "5":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[0][4] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [0][4] != 1:
            liste [0][4] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E15", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "2" and esc == "1":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[1][0] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [1][0] != 1:
            liste [1][0] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E21", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "2" and esc == "2":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[1][1] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [1][1] != 1:
            liste [1][1] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E22", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "2" and esc == "3":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[1][2] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [1][2] != 1:
            liste [1][2] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E23", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "2" and esc == "4":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[1][3] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [1][3] != 1:
            liste [1][3] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E24", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "2" and esc == "5":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[1][4] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [1][4] != 1:
            liste [1][4] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E25", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "3" and esc == "1":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[2][0] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [2][0] != 1:
            liste [2][0] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E31", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "3" and esc == "2":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[2][1] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [2][1] != 1:
            liste [2][1] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E32", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "3" and esc == "3":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[2][2] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [2][2] != 1:
            liste [2][2] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E33", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "3" and esc == "4":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[2][3] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [2][3] != 1:
            liste [2][3] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E34", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "3" and esc == "5":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[2][4] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [2][4] != 1:
            liste [2][4] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E35", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "4" and esc == "1":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[3][0] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [3][0] != 1:
            liste [3][0] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E41", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "4" and esc == "2":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[3][1] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [3][1] != 1:
            liste [3][1] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E42", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "4" and esc == "3":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[3][2] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [3][2] != 1:
            liste [3][2] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E43", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "4" and esc == "4":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[3][3] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [3][3] != 1:
            liste [3][3] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E44", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "4" and esc == "5":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[3][4] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [3][4] != 1:
            liste [3][4] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E45", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "5" and esc == "1":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[4][0] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [4][0] != 1:
            liste [4][0] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E51", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "5" and esc == "2":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[4][1] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [4][1] != 1:
            liste [4][1] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E52", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "5" and esc == "3":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[4][2] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [4][2] != 1:
            liste [4][2] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E53", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "5" and esc == "4":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[4][3] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [4][3] != 1:
            liste [4][3] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E54", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "5" and esc == "5":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[4][4] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [4][4] != 1:
            liste [4][4] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E55", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "6" and esc == "1":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[5][0] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [5][0] != 1:
            liste [5][0] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E61", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "6" and esc == "2":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[5][1] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [5][1] != 1:
            liste [5][1] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E62", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "6" and esc == "3":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[5][2] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [5][2] != 1:
            liste [5][2] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E63", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "6" and esc == "4":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[5][3] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [5][3] != 1:
            liste [5][3] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E64", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "6" and esc == "5":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[5][4] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [5][4] != 1:
            liste [5][4] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E65", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "7" and esc == "1":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[6][0] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [6][0] != 1:
            liste [6][0] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E71", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "7" and esc == "2":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[6][1] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [6][1] != 1:
            liste [6][1] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E72", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "7" and esc == "3":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[6][2] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [6][2] != 1:
            liste [6][2] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E73", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "7" and esc == "4":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[6][3] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [6][3] != 1:
            liste [6][3] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E74", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "7" and esc == "5":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[6][4] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [6][4] != 1:
            liste [6][4] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E75", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "8" and esc == "1":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[7][0] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [7][0] != 1:
            liste [7][0] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E81", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "8" and esc == "2":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[7][1] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [7][1] != 1:
            liste [7][1] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E82", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "8" and esc == "3":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[7][2] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [7][2] != 1:
            liste [7][2] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E83", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "8" and esc == "4":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[7][3] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [7][3] != 1:
            liste [7][3] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E84", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    elif esr == "8" and esc == "5":
        if liste == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]:
            print ("""Unfortunately all seats in economy class are taken.
            Please choose different class or trip""")
            pselected()
        elif liste[7][4] == 1:
            print ("Unfortunately seat is taken.")
            economy(d, s, feid, liste, id, dest, ts, sour)
        elif liste [7][4] != 1:
            liste [7][4] = 1
            print ("Seat is successfully booked.")
            ticket(id, "E85", dest, ts, "Economy", sour)
            mainmenu2()
        else:
            print("Invalid Entry")
            economy(d, s, feid, liste, id, dest, ts, sour)
    else:
        print("Invalid Entry")
        economy(d, s, feid, liste, id, dest, ts, sour)

mainmenu()
