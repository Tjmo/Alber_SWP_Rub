# Match funktion ist leider erst ab Version 3.10 verfügbar
# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case _:
#             return "Something's wrong with the internet"

    



import random
from enum import IntEnum

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


def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str} (0-4)): "))
    action = Action(selection)
    return action

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

def determine_winner(user_action, computer_action):
    defeats = victories[user_action]
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif computer_action in defeats:
        print(f"{user_action.name} beats {computer_action.name}! You win!")
    else:
        print(f"{computer_action.name} beats {user_action.name}! You lose.")

while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

