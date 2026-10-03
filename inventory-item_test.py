def inventory(jail_card, poäng, mult, jackpot_mult):
    print()
    print("#" * 50)
    print()
    print("Du har:")
    print(f"{jail_card} Get out of jail free-kort.")
    print()
    print("Statestik:")
    print(f"Du har {poäng} poäng.")
    print(f"Du får {mult}x vid vinst och {jackpot_mult}x vid jackpot.")
    print()
    print("#" * 50)
    print()
    back = input("Vill du återvända [Y/n]: ")
    if back.lower() != "n":
        items = jail_card

        if items > 0:
            item()

def item(jail_card, jail_card_active):
    print()
    item = input("Vill du använda ett föremål [Y/n]: ")
    if item != "n":
        while True:
            print()
            print(f"(1) Du har {jail_card} kort tillgänglig.")
            print()
            
            item_use = input("Vad vill du använda [1-5], eller [n] för att avbryta: ")
            if item_use.lower() == "n":
                print()
                break
            else:
                try:
                    item_use = int(item_use)
                    break
                except ValueError:
                    print("Vänligen välj en av alternativen.")
                    print()

        if int(item_use) == 1:
            if jail_card_active != True:
                if jail_card > 0:
                    jail_card -= 1 
                    jail_card_active = True
                    print("Du har nu ett kort igång.")
                else:
                    print("Du har inga kort tillgänglig!")
            elif jail_card_active == True:
                print("Du har redan ett kort igång!")
        else:
            print()
    return jail_card, jail_card_active