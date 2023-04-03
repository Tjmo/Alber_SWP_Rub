import random
import ast
from enum import IntEnum
import requests

spieler_siege = 0
ai_siege = 0
name = (input(f"Enter your name: "))
names = []
multiple = names.append(name)

host = 'http://localhost:5000/score'

spiel_wahl = {"Stein": 0, "Papier": 0, "Schere": 0, "Spock": 0, "Echse": 0}


class Action(IntEnum):
    Stein = 0
    Papier = 1
    Schere = 2
    Spock = 3
    Echse = 4


siege = {
    Action.Schere: [Action.Echse, Action.Papier],
    Action.Papier: [Action.Spock, Action.Stein],
    Action.Stein: [Action.Echse, Action.Schere],
    Action.Echse: [Action.Spock, Action.Papier],
    Action.Spock: [Action.Schere, Action.Stein]
}

verloren = {
    Action.Schere: [Action.Stein, Action.Spock],
    Action.Papier: [Action.Schere, Action.Echse],
    Action.Stein: [Action.Papier, Action.Echse],
    Action.Echse: [Action.Stein, Action.Schere],
    Action.Spock: [Action.Papier, Action.Echse]
}


def get_computer_auswahl():
    auswahl = random.randint(0, len(Action) - 1)
    action = Action(auswahl)
    print(f"Computer wählte: ", action)
    return action


def get_user_auswahl():
    walhmöglichkeiten = [f"{action.name}[{action.value}]" for action in Action]
    walhmöglichkeiten_str = ", ".join(walhmöglichkeiten)
    auswahl = int(input(f"Enter a choice ({walhmöglichkeiten_str}): "))
    print("auswahl", auswahl)
    action = Action(auswahl)
    return action


def determine_winner(spieler_zug, computer_action):
    global ai_siege, spieler_siege
    defeats = siege[spieler_zug]
    if spieler_zug == computer_action:
        print(f"Beide Spieler haben {spieler_zug.name} gewählt. Unentschieden!")
    elif computer_action in defeats:
        print(f"{spieler_zug.name} schlägt {computer_action.name}! Du gewinnst!")
        spieler_siege = spieler_siege + 1
    else:
        print(f"{computer_action.name} schlägt {spieler_zug.name}! Du verlierst.")
        ai_siege = ai_siege + 1


def save_data_to_file():
    data = "Spieler " + str(name) + " gewinnt: " + str(spieler_siege) + "\nComputer gewinnt: " + str(
        ai_siege) + "\n" + str(spiel_wahl)
    with open("D:/Dokumente/Schule/2022_23/SWP_Rub/Stunde3/stat.txt", 'w') as stat:
        stat.write(data)
        stat.close()


def save_to_server():
    print('Speichere einen Eintrag am Server:')
    response = requests.put('%s/%s' % (host, name), data={'score': stat})
    print(response)
    print(response.json())


def get_from_server():
    print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
    print('Eintrag holen:')
    response = requests.get('%s/%s' % (host, name)).json()
    print(response)


if __name__ == "__main__":
    modus = input("Statistik ansehen[1], Spielen [2]: ")
    if modus.lower() == "1":
        get_from_server()
    else:
        while True:
            try:
                spieler_zug = get_user_auswahl()
                print("Spieler wählt:", spieler_zug)
                if spieler_zug == Action.Stein:
                    spiel_wahl["Stein"] = spiel_wahl["Stein"] + 1
                elif spieler_zug == Action.Papier:
                    spiel_wahl["Papier"] = spiel_wahl["Papier"] + 1
                elif spieler_zug == Action.Schere:
                    spiel_wahl["Schere"] = spiel_wahl["Schere"] + 1
                elif spieler_zug == Action.Spock:
                    spiel_wahl["Spock"] = spiel_wahl["Spock"] + 1
                elif spieler_zug == Action.Echse:
                    spiel_wahl["Echse"] = spiel_wahl["Echse"] + 1


            except ValueError as e:
                range_str = f"[0, {len(Action) - 1}]"
                print(f"Invalid auswahl. Enter a value in range {range_str}")
                continue
                continue
            
            computer_action = get_computer_auswahl()
            determine_winner(spieler_zug, computer_action)
            
            play_again = input("Nochmal? (j/n): ")
            if play_again.lower() != "j":
                break

            save_data_to_file()

        stat = str(spiel_wahl)

        save_to_server()
        get_from_server()
