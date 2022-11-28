# Match funktion ist leider erst ab Version 3.10 verfügbar
# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case _:
#             return "Something's wrong with the internet"



import random

dic = {"stein" : 0, "papier" : 1, "schere" : 2, "echse" : 3, "spock" : 4}

while True:

    while True:
        choice = input("Wähle (stein,papier,schere,echse,spock): ")
        choice = choice.lower()

        if choice not in dic.keys():
            print("Falsche Eingabe!\n")

        else:
            pc = random.choice(list(dic.keys()))
            pc = pc.lower()
            break

    if choice == pc:
        print("{0:10}{1:10}".format("Spieler: ", choice[0].upper()+choice[1:]))
        print("{0:10}{1:10}".format("Computer: ", pc[0].upper()+pc[1:]))
        print("Unentschieden!")

    elif (
        (choice == "stein" and (pc == "schere" or pc == "echse")) or
        (choice == "papier" and (pc == "stein" or pc == "spock")) or
        (choice == "schere" and (pc == "papier" or pc == "echse")) or
        (choice == "echse" and (pc == "papier" or pc == "spock")) or
        (choice == "spock" and (pc == "stein" or pc == "schere"))
        ):
        print("{0:10}{1:10}".format("Spieler: ", choice[0].upper()+choice[1:]))
        print("{0:10}{1:10}".format("Computer: ", pc[0].upper()+pc[1:]))
        print("Du gewinnst!")

    else:
        print("{0:10}{1:10}".format("Spieler: ", choice[0].upper()+choice[1:]))
        print("{0:10}{1:10}".format("Computer: ", pc[0].upper()+pc[1:]))
        print("Der Computer gewinnt!")

    again = input("\nNochmal (j/n): ")
    if again == "J" or again == "j":
        continue
    else:
        break
