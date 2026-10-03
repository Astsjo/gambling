import random
import time
import sys

restart = True
password = "Test"
dev = False
menu_choice = " "
has_item = False

print()
dev_choice = input("Öppna utvecklarinställningar [Y/n]: ")
if dev_choice.lower() != "n":
    pass_input = input("Lösenord: ") 
    if pass_input == password:
        dev = True
    else:
        print("Fel lösenord.")
        dev = False
else:
    print()


def shop(point, mult, jackpot_mult, mult_price, jail_card, has_item):
    while True:
        print("#" * 50)
        print()
        print("Tillgängliga uppgraderingar/varor:")
        print()
        print(f"(1) {mult_price}p: Vinst multiplikation")
        print("(2) 10p: Get out of jail free card (inga förlorade poäng när igång och vid förlust)")
        print()
        print("#" * 50)
        print()
        shop_choice = input(f"Du har {point} poäng, välj alternativ [1-5] eller [n] för att avbryta: ")
        print()

        if shop_choice.lower() == "n":
            break
        elif int(shop_choice) == 1:
            if point >= mult_price:
                mult += (mult/2)
                jackpot_mult += (jackpot_mult/2)

                point -= mult_price
                mult_price += (mult_price/1.5)

                jackpot_mult = int(jackpot_mult)
                mult = int(mult)
                mult_price = int(mult_price)

                print(f"Du får nu {mult}x om du gissar rätt och {jackpot_mult}x om du gissar rätt på exact!")
            else:
                print()
                print("Du har inte råd!")
        elif int(shop_choice) == 2:
            if point >= 10:
                jail_card += 1
                point -= 10
                has_item = True
                print()
                print("Du har nu ett till kort!")
            else:
                print("Du har inte råd!")
        else:
            print("Vänligen välj ett alternativ.")

        print()
        print("#" * 50)
        print()
        shop_cont = input("Vill du fortsätta handla [Y/n]: ")
        print()
        if shop_cont.lower() != "n":
            print()
        else:
            break
    return point, mult, jackpot_mult, mult_price, jail_card, has_item


def item(jail_card, jail_card_active):
    print()
    while True:
        print("#" * 50)
        print()
        print(f"(1) Du har {jail_card} kort tillgänglig.")
        print()
        print("#" * 50)
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
                print()
                print()
                print("Du har nu ett kort igång.")
            else:
                print("Du har inga kort tillgänglig!")
        elif jail_card_active == True:
            print("Du har redan ett kort igång!")
    else:
        print()
    return jail_card, jail_card_active


def inventory(jail_card, jail_card_active, point, mult, jackpot_mult):
    print()
    print("#" * 50)
    print()
    print("Du har:")
    print(f"{jail_card} Get out of jail free-kort.")
    print()
    print("Statestik:")
    print(f"Du har {point} poäng.")
    print(f"Du får {mult}x vid vinst och {jackpot_mult}x vid jackpot.")
    print()
    print("#" * 50)
    print()
    while True:
        while True:
            print("Vill du:")
            print("(1) Återvända")
            print("(2) Använda föremål")
            print()
            print("#" * 50)
            print()
            back = input("Välj alternativ [1-2]: ")
            try:
                back = int(back)
                break
            except ValueError:
                print("Vänligen välj ett alternativ.")

        if back == 2:
            items = jail_card

            if items > 0:
                jail_card, jail_card_active = item(jail_card, jail_card_active)
                break
            elif items <= 0:
                print()
                print("Du har inga föremål!")
                print()
                print("#" * 50)
                print()
        elif back == 1:
            break
    return jail_card, jail_card_active


def computer(point, cheat_choice, mult, jackpot_mult, jail_card_active):
    print()
    while True:
        choice = input("Datorn står och skakar två tärningar i handen. Tror du den kommer att slå [m]indre, [s]törre, eller [e]xact 6: ")
        print()
        if choice.lower() in ["mindre", "m", "större", "s", "exact", "6", "exact 6", "e"]:
            break
        else:
            print("Vänligen välj en av alternativen.")

    # Användaren väljer hur mycket de lägger på sin gissning
    while True:
        while True:
            amount = input(f"Hur mycket vill du lägga (du har {point} just nu): ")
            print()
            try:
                amount = int(amount)
                break
            except ValueError:
                print("Vänligen använd ett tal.")
                print()
            
        if (point - amount) < 0:
            print("Du kan inte välja mer än poängen du har!")
        else:
            point -= amount
            break

    # Datorns slag slumpas eller sätts om man valt vad det ska bli.
    if cheat_choice.lower() in ["m", "mindre"]:
        rnd_num = 1
    elif cheat_choice.lower() in ["s", "större"]:
        rnd_num = 12
    elif cheat_choice.lower() in ["e", "exact"]:
        rnd_num = 6
    else:
        rnd_num = random.randint(1, 12)

    print("Datorn kastar tärningarna, de studsar omkring")
    time.sleep(1.2)
    print()
    print("En av tärningarna snurrar...")
    time.sleep(2.4)
    print()
    print(f"Datorn slog {rnd_num}")

    # Kollar om gissningen är korrekt och updaterar vinsten/förlusten
    if choice.lower() in ["m", "mindre"] and (rnd_num < 6):
        print("Du gissade rätt, du vann!")
        amount *= mult
        point += amount
        jail_card_active = False
        time.sleep(3)
    elif (choice.lower() in ["s", "större"]) and (rnd_num > 6):
        print("Datorn fick större än 6, du vann!")
        amount *= mult
        point += amount
        jail_card_active = False
        time.sleep(3)
    elif (choice.lower() in ["e", "exact", "6", "exact 6"]) and (rnd_num == 6):
        print("Den fick exact 6, du vann stort!")
        amount *= jackpot_mult
        point += amount
        jail_card_active = False
        time.sleep(3)
    else:
        if jail_card_active == True:
            print("Du gissade fel och förlorade, men kortet förhindrade någon förlust av poäng!")
            point += amount
            jail_card_active = False
        else:
            print("Du gissade fel, du förlorade.")
            amount = 0
            time.sleep(3)
    return point, cheat_choice, mult, jackpot_mult, jail_card_active


def menu(first_round):
    if first_round != True:
        print()
        print("#" * 20)
        print()
        print("(1) Gå till datorn.")
        print("(2) Gå till affären.")
        print("(3) Förråd.")
        print("(4) Avsluta.")
        print()
        print("#" * 20)
        print()
        while True:
            menu_choice = input("Välj alternativ [1-4]: ")
            print()
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
        print()
        while True:
            menu_choice = input("Välj alternativ [1-2]: ")
            try:
                menu_choice = int(menu_choice)
                break
            except ValueError:
                print()
                print("Vänligen välj en av alternativen.") 
                print()
        menu_choice = int(menu_choice)
    return menu_choice


while restart:
    point = 20
    cont = True
    mult_price = 30
    jail_card = 0
    mult = 2
    jackpot_mult = 4
    jail_card_active = False
    first_round = True
    has_item = False
    cheat_choice = " "
    print()

    while cont:
        # Användaren förlorar om de har inga poäng kvar
        InvalidNumber = True
        if point > 0:
            if dev == True:
                cheat_choice = input("[M]indre, [S]törre, [E]xact: ")
                if ((cheat_choice.lower() == "m") or (cheat_choice.lower() == "mindre")):
                    rnd_num = 1
                elif ((cheat_choice.lower() == "s") or (cheat_choice.lower() == "större")):
                    rnd_num = 12
                elif ((cheat_choice.lower() == "e") or (cheat_choice.lower() == "exact")):
                    rnd_num = 6
                else:
                    cheat_choice = " "

            while (point > 0):
                menu_choice = menu(first_round)
                if first_round == True:
                    if menu_choice == 1:
                        point, cheat_choice, mult, jackpot_mult, jail_card_active = computer(
                            point, cheat_choice, mult, jackpot_mult, jail_card_active
                        )
                    elif menu_choice == 2:
                        cont = False
                        print()
                        print(f"Tack för att du spelade, du slutade med {point} poäng!")
                        print()
                        sys.exit(0)
                    first_round = False
                elif first_round != True:
                    if menu_choice == 1:
                        point, cheat_choice, mult, jackpot_mult, jail_card_active = computer(
                            point, cheat_choice, mult, jackpot_mult, jail_card_active
                        )
                    elif menu_choice == 2:
                        point, mult, jackpot_mult, mult_price, jail_card, has_item = shop(
                            point, mult, jackpot_mult, mult_price, jail_card, has_item
                        )
                    elif menu_choice == 3:
                        jail_card, jail_card_active = inventory(jail_card, jail_card_active, point, mult, jackpot_mult)
                    elif menu_choice == 4:
                        cont = False
                        print()
                        print(f"Tack för att du spelade, du slutade med {point} poäng!")
                        print()
                        sys.exit(0)
        else: 
            print()
            game_over = input("Du har inga poäng kvar! Vill du starta om [Y/n]: ")
            print()
            if game_over.lower() == "n":
                sys.exit(0)
            else:
                restart = True
                cont = False