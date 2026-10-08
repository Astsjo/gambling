import random
import time
import sys
from input_validator import valid_int_input, valid_int_string_input
from any_key_continue import press_any_key

restart = True
password = "Test"
dev = False
menu_choice = " "
has_item = False
first_time = True

print()
dev_choice = input("Öppna utvecklarinställningar [Y/n]: ").strip().lower()
if dev_choice != "n":
    pass_input = input("Lösenord: ") 
    if pass_input == password:
        dev = True
    else:
        print("Fel lösenord.")
        dev = False
else:
    print()

def grammar_tutorial():
    print()
    print("#" * 50, "\n")

    print("Det är ganska enkelt.\n")

    print("I ja/nej alternativ (ser ut [y/n]) räker det med ett")
    print("av alternativen. Oftast kommer en bokstav vara en versal,")
    print("den är förvalda alternativet om du inte väljer en av")
    print("alternativen.\n")

    print("Så ett alterativ som ser ut [Y/n] kommer ett enkel enter")
    print("eller annan karaktär bli ett ja, och ett N kommer bli nej.")
    print("Det går att svara i både gemener och versaler alltid.\n")

    print("När det finns alternativ i en mening (som [e]xact)")
    print("så räker det med att skriva enbart E, eller hela ordet.\n")

    print("Alternativ mellan någonting förvalt, som en lista,")
    print("behöver du bara skriva siffran som hör ihop med det alternativet.\n")

    print("Om du givit ett svar som inte fungerar kommer du bes")
    print("välja ett av alternativen. Om du inte väljer någonting")
    print("i en ja/nej fråga kommer det bli versalen automatiskt.\n")

    print("#" * 50)
    press_any_key()
    print()

def game_tutorial():
    print("#" * 50, "\n")

    print("Välkommen!")
    print()
    print("Reglerna är enkel: \n")

    print("Du börjar med ett antal poäng.")
    print("Du kommer möta en dator med två tärningar.\n")

    print("Du ska gissa om summan av tärningarna kommer att vara")
    print("mindre än 6, större än 6, eller exact 6.\n")

    print("Gissar du rätt tjänar du poäng. Gissar du fel så")
    print("förlorar du poängen du lade.")
    print("Du tjänar extra om du gissar rätt på exact 6.\n")

    print("Mellan rundor kan du kolla ditt föråd, statestik,")
    print("föremål, affären, och använda föremål du har.\n")

    print("#" * 50)
    press_any_key()
    print()


def shop(point, mult, jackpot_mult, mult_price, jail_card, has_item):
    while True:
        print("#" * 50)
        print()
        print("Tillgängliga uppgraderingar/varor:\n")

        print(f"(1) {mult_price}p: Vinst multiplikation")
        print("(2) 10p: Get out of jail free card (inga förlorade poäng när igång och vid förlust)\n")

        print("#" * 50, "\n")

        shop_choice = valid_int_string_input(f"Du har {point} poäng, välj alternativ [1-5] eller [n] för att avbryta: ", allowed_strings=["n"])
        print()

        if shop_choice == "n":
            break
        elif shop_choice == 1:
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
        elif shop_choice == 2:
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
        print("#" * 50, "\n")
        
        shop_cont = input("Vill du fortsätta handla [Y/n]: ").strip().lower()
        print()
        if shop_cont != "n":
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
        
        item_use = valid_int_string_input("Vad vill du använda [1-5], eller [n] för att avbryta: ", allowed_strings=["n"])
        if item_use == "n":
            print()
            break
        elif item_use == 1:
            if jail_card_active != True:
                if jail_card > 0:
                    jail_card -= 1 
                    jail_card_active = True
                    print()
                    print("Du har nu ett kort igång.\n")
                else:
                    print("Du har inga kort tillgänglig!")
            elif jail_card_active == True:
                print("Du har redan ett kort igång!")
        else:
            print()
    return jail_card, jail_card_active


def inventory(jail_card, jail_card_active, point, mult, jackpot_mult):
    print()
    print("#" * 50, "\n")

    print("Du har:")
    print(f"{jail_card} Get out of jail free-kort.")
    print(f"Kort aktiverad: {jail_card_active}\n")

    print("Statestik:")
    print(f"Du har {point} poäng.")
    print(f"Du får {mult}x vid vinst och {jackpot_mult}x vid jackpot.\n")

    print("#" * 50, "\n")

    while True:
        while True:
            print("Vill du:")
            print("(1) Återvända")
            print("(2) Använda föremål\n")

            print("#" * 50, "\n")

            back = valid_int_input("Välj alternativ [1-2]: ")
            break
        if back == 2:
            items = jail_card

            if items > 0:
                jail_card, jail_card_active = item(jail_card, jail_card_active)
                break
            elif items <= 0:
                print()
                print("Du har inga föremål!\n")

                print("#" * 50, "\n")

        elif back == 1:
            break
    return jail_card, jail_card_active


def computer(point, cheat_choice, mult, jackpot_mult, jail_card_active):
    print()
    while True:
        choice = input("Datorn står och skakar två tärningar i handen. Tror du den kommer att slå [m]indre, [s]törre, eller [e]xact 6, eller [n] för att avbryta: ").strip().lower()
        print()
        if choice in ["mindre", "m", "större", "s", "exact", "6", "exact6", "e"]:
            break
        elif choice == "n":
            return point, cheat_choice, mult, jackpot_mult, jail_card_active
        else:
            print("Vänligen välj en av alternativen.\n")

    # Användaren väljer hur mycket de lägger på sin gissning
    while True:
        amount = valid_int_string_input(f"Hur mycket vill du lägga (du har {point} just nu) eller [n] för att avbryta: ", allowed_strings=["n"])
        print()
        if amount == "n":
            return point, cheat_choice, mult, jackpot_mult, jail_card_active
        elif (point - amount) < 0:
            print("Du kan inte välja mer än poängen du har!\n")
        elif (amount <= 0):
            print("Du måste lägga någonting!")
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

    print("Datorn kastar tärningarna, de studsar omkring...\n")
    time.sleep(1.2)

    print("En av tärningarna snurrar...\n")
    time.sleep(2.4)

    print(f"Datorn slog {rnd_num}\n")

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
            time.sleep(3)
        else:
            print("Du gissade fel, du förlorade.")
            amount = 0
            time.sleep(3)
    return point, cheat_choice, mult, jackpot_mult, jail_card_active


def menu(first_round):
    if first_round != True:
        print()
        print("#" * 20, "\n")

        print("(1) Gå till datorn.")
        print("(2) Gå till affären.")
        print("(3) Förråd.")
        print("(4) Avsluta.")
        print("(5) Tutorials.\n")

        print("#" * 20, "\n")

        menu_choice = valid_int_input("Välj alternativ [1-5]: ")
        print()

        print("#" * 20)
    elif first_round == True:
        print()
        print("#" * 20, "\n")

        print("(1) Gå till datorn.")
        print("(2) Avsluta.")
        print("(3) Tutorials.\n")

        print("#" * 20, "\n")

        menu_choice = valid_int_input("Välj alternativ [1-3]: ")

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
                if (cheat_choice.lower() in ["m", "mindre"]):
                    rnd_num = 1
                elif (cheat_choice.lower() in ["s", "större"]):
                    rnd_num = 12
                elif (cheat_choice.lower() in ["e", "exact"]):
                    rnd_num = 6
                else:
                    cheat_choice = " "

            while (point > 0):
                if first_time == True:
                    print()
                    tutorial_grammar = input("Vet du hur alternativen i spelet fungerar [y/N]: ").strip().lower()
                    if tutorial_grammar != "y":
                        grammar_tutorial()
                    tutorial_game = input("Vill du ha en tutorial [Y/n]: ").strip().lower()
                    print()
                    if tutorial_game != "n":
                        game_tutorial()
                        
                menu_choice = menu(first_round)
                if first_round == True:
                    if menu_choice == 1:
                        point, cheat_choice, mult, jackpot_mult, jail_card_active = computer(
                            point, cheat_choice, mult, jackpot_mult, jail_card_active
                        )
                        first_round = False
                    elif menu_choice == 2:
                        cont = False
                        print()
                        print(f"Tack för att du spelade, du slutade med {point} poäng!\n")
                      
                        sys.exit(0)
                    elif menu_choice == 3:
                        print("#" * 20, "\n")
                        
                        print("(1) Alternativ.")
                        print("(2) Spelet.\n")
                        
                        print("#" * 20, "\n")
                        
                        tutorial_choice = valid_int_string_input("Välj tutorial [1-2] eller [n] för att avbryta: ", allowed_strings=["n"])
                        if tutorial_choice == "n":
                            print()
                        elif tutorial_choice == 1:
                            grammar_tutorial()
                        elif tutorial_choice == 2:
                            game_tutorial()
                    first_time = False
                    
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
                        print(f"Tack för att du spelade, du slutade med {point} poäng!\n")
                        
                        sys.exit(0)
                    elif menu_choice == 5:
                        print("#" * 20, "\n")
                        
                        print("(1) Alternativ.")
                        print("(2) Spelet.\n")
                        
                        print("#" * 20, "\n")
                        
                        tutorial_choice = valid_int_string_input("Välj tutorial [1-2] eller [n] för att avbryta: ", allowed_strings=["n"])
                        if tutorial_choice == "n":
                            print()
                        elif tutorial_choice == 1:
                            grammar_tutorial()
                        elif tutorial_choice == 2:
                            game_tutorial()
        else: 
            print()
            game_over = input("Du har inga poäng kvar! Vill du starta om [Y/n]: ").strip().lower()
            print()
            if game_over == "n":
                sys.exit(0)
            else:
                restart = True
                cont = False