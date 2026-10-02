first_round = False
menu_choice = " "
import sys
def menu():
    if first_round != True:
        print()
        print("#" * 20)
        print()
        print("(1) Gå till datorn.")
        print("(2) Gå till affären.")
        print("(3) Förråd.")
        print("(4) Avsluta.")
        print()
        while True:
            menu_choice = input("Välj alternativ [1-4]: ")
            try:
                menu_choice = int(menu_choice)
                break
            except ValueError:
               print("Vänligen välj en av alternativen.") 
        print("#" * 20)
    elif first_round == True:
        print()
        print("#" * 20)
        print()
        print("(1) Gå till datorn.")
        print("(2) Avsluta.")
        print()
        print("#" * 20)
        while True:
            menu_choice = input("Välj alternativ [1-2]: ")
            try:
                menu_choice = int(menu_choice)
                break
            except ValueError:
                print("Vänligen välj en av alternativen.") 

if first_round == True:
    if menu_choice == 1:
        computer()
    elif menu_choice == 2:
        sys.exit(0)
elif first_round != True:
    if menu_choice == 1:
        computer()
    elif menu_choice == 2:
        shop()
    elif menu_choice == 3:
        inventory()
    elif menu_choice == 4:
        sys.exit(0)