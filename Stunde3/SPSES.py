# Match funktion ist leider erst ab Version 3.10 verfügbar
# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case _:
#             return "Something's wrong with the internet"

import random
from enum import IntEnum


spieler_siege = 0
ai_siege = 0
spiel_wahl = {"Stein": 0, "Papier": 0, "Schere": 0, "Spock": 0, "Echse": 0}

class Action(IntEnum):
    Stein = 0
    Papier = 1
    Schere = 2
    Echse = 3
    Spock = 4

victories = {
    Action.Schere: [Action.Echse, Action.Papier],
    Action.Papier: [Action.Spock, Action.Stein],
    Action.Stein: [Action.Echse, Action.Schere],
    Action.Echse: [Action.Spock, Action.Papier],
    Action.Spock: [Action.Schere, Action.Stein]
}


def get_user_auswahl():
    wahlmöglichkeiten = [f"{action.name}[{action.value}]" for action in Action]
    wahlmöglichkeiten_str = ", ".join(wahlmöglichkeiten)
    auswahl = int(input(f"Wähle zwischen 0 und 4 ({wahlmöglichkeiten_str}): "))
    action = Action(auswahl)
    return action

def get_computer_auswahl():
    auswahl = random.randint(0, len(Action) - 1)
    action = Action(auswahl)
    print(f"Computer Wahl: ",action)
    return action

def determine_winner(spieler_zug, computer_action):
    global ai_siege, spieler_siege
    verlier = victories[spieler_zug]
    if spieler_zug == computer_action:
        print(f"Beide Spieler haben {spieler_zug.name} gewählt. Unentschieden!")
    elif computer_action in verlier:
        print(f"{spieler_zug.name} schlägt {computer_action.name}! Du Gewinnst!")
        spieler_siege = spieler_siege + 1
    else:
        print(f"{computer_action.name} schlägt {spieler_zug.name}! Du verlierst.")
        ai_siege = ai_siege + 1

def save_data_to_file():
    data = "Spieler gewinnt: " + str(spieler_siege) + "\nComputer gewinnt: " + str(ai_siege) + "\n" + str(spiel_wahl)
    with open("D:/Dokumente/Schule/2022_23/SWP_Rub/Stunde3/stat.txt", 'w') as stat:
        stat.write(data)
        stat.close()

if __name__ == "__main__":
    while True:
        try:
            spieler_zug = get_user_auswahl()
            print("Spieler Wahl:", spieler_zug)
            
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
            print(f"Falsche Eingabe, bitte etwas von {range_str} eingeben!")
            continue
        computer_action = get_computer_auswahl()
        determine_winner(spieler_zug, computer_action)

        play_again = input("Nochmal? (j/n): ")
        if play_again.lower() != "j":
            break

        save_data_to_file()
