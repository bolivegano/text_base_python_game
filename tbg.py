import random
import time
import pdb
from termcolor import colored

class Player:
    def __init__(self):
        self.player_health = 100
        self.player_energy = 0
    
    def normal_atk(self):
        attack = random.randint(0, 15)
        self.player_energy += 10
        return attack

    def special_atk(self):
        special_attack = random.randint(20, 40)
        self.player_energy -= 20
        return special_attack

    def heal(self):
        healing = random.randint(5, 25)
        self.player_health += healing
        self.player_energy -= 15
        return healing

    def subtract_health(self, amount):
        self.player_health = self.player_health - amount
    
    def print_status(self, name="COMP", color="yellow"):
        print(colored(f"\n{name}\t\t{self.player_health} health,\t{self.player_energy} energy.", f"{color}"))
    
def turn_order():
   return random.choice([["name", "COMP", "COMP", "name"], ["COMP", "name", "name", "COMP"]])

def print_statuses(player_health, player_energy, computer_health, computer_energy):
    print(colored(f"\n{player_name_input}:\t\t{player_health} health,\t{player_energy} energy.", "red"))
    print(colored(f"COMP:\t\t{computer_health} health,\t{computer_energy} energy.", "yellow"))
    time.sleep(2)

def print_turn(turn):
    if turn == "COMP":
        print(colored(f"\n::::::: COMP'S TURN :::::::", "yellow"))
        time.sleep(2)
    else:
        print(colored(f"\n::::::: {player_name_input}'S TURN :::::::", "red"))
        time.sleep(2)

def game_start():
    ready = str(input("Are you ready to play? (y to play, other keys to exit): ")).lower()
    if ready != "y":
        exit()
    else:
        return ready
        
def get_action():
    selection = ""
    while selection == "" or selection not in (1,2,3,4):
        try:
            selection = int(input("\nPlease choose an action:\n\n1) Normal Attack\n2) Special Attack\n3) Heal\n4) exit program\n\n"))
            if selection > 4:
                print("You must choose a value: 1, 2, 3, or 4 to exit")
            else:
                return selection
        except ValueError as ve:
            print("You must choose a value: 1, 2, or 3. Type 4 to exit")
        

def game_mechanics(ready, player_name):
    turn_order_list = turn_order()
    upcoming_turns = turn_order_list.copy()
    current_turn = []
    human = Player()
    comp = Player()
    name = player_name

    while ready=="y" and human.player_health > 0 and comp.player_health > 0:
        if not upcoming_turns:
            upcoming_turns = turn_order.copy()
        else:
            current_turn.append(upcoming_turns.pop())
            print_turn(current_turn[-1])
            if current_turn[-1] != "COMP":
                #pdb.set_trace()
                action = get_action()
                if action == 1:
                    player_normal_attack = human.normal_atk()
                    comp.subtract_health(player_normal_attack)
                    print(f"\n{name} just did a normal attack causing {player_normal_attack} damage!")
                    human.print_status(name, "red")
                    comp.print_status()
                    time.sleep(2)
                elif action == 2 and human.player_energy >= 20:
                    player_special_attack = human.special_atk()
                    comp.subtract_health(player_special_attack)
                    print(f"\n{name} just did a special attack causing {player_special_attack} damage!")
                    human.print_status(name, "red")
                    comp.print_status()
                    time.sleep(2)
                elif action == 3 and human.player_energy >= 15:
                    human_heal = human.heal()
                    print(f"\n{name} just healed themselves for {human_heal}.")
                    human.print_status(name, "red")
                    comp.print_status()
                    time.sleep(2)

                elif action == 3 and human.player_energy < 15:
                    time.sleep(2)
                    print(f"\nYou have {human.player_health} health and {human.player_energy} energy.")
                    print(f"\nYou don't have enough energy to heal. Please choose regular attack")
                elif action == 4:
                    exit()
            else:
                if comp.player_health < 50 and comp.player_energy >= 15:
                    comp_healing = comp.heal()
                    print(f"The computer has healed themselves for {comp_healing}.")
                    human.print_status(name, "red")
                    comp.print_status()
                    time.sleep(2)
                elif comp.player_energy >= 20:
                    comp_special_attack = comp.special_atk()
                    human.subtract_health(comp_special_attack)
                    print(f"\nThe computer just did a special attack causing {comp_special_attack} damage.")
                    human.print_status(name, "red")
                    comp.print_status()
                    time.sleep(2)
                else:
                    comp_norm_attack = comp.normal_atk()
                    human.subtract_health(comp_norm_attack)
                    print(f"\nThe computer did a normal attack and inflicted {comp_norm_attack} damage.")
                    human.print_status(name, "red")
                    comp.print_status()
                    time.sleep(2)

    if comp.player_health <= 0:
        print(colored(f"\n***** {name} has won this round! *****\n\n", "green"))
    elif human.player_health <= 0:
        print(colored(f"\n***** The COMP has won this round! *****\n\n", "green"))

# *** MAIN PROGRAM ***
ready_input = game_start()
player_name_input = str(input("Please enter your name: ")).upper()
game_mechanics(ready_input, player_name_input)