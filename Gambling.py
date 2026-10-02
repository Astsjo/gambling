import random
import time
restart = True
password = "Test"
dev = False

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

while restart:
    point = 20
    cont = True
    mult_price = 30
    jail_card = 0
    mult = 2
    jackpot_mult = 4
    shop = False
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

            # Användaren väljer om de vill gå in i affären eller inte
            if first_round == False:
                print()
                shop_enter = input("Vill du gå till affären [Y/n]: ")
                if shop_enter.lower() == "n":
                    shop = False
                else:
                    shop = True

            # Om de går in i affären:
            while shop:
                print()
                print("Tillgängliga uppgraderingar/varor:")
                print()
                print(f"(1) {mult_price}p: Vinst multiplikation")
                print("(2) 10p: Get out of jail free card (inga förlorade poäng när igång och vid förlust)")
                print()
                shop_choice = input(f"Du har {point} poäng, välj alternativ [1-5] eller [n] för att avbryta: ")

                if shop_choice.lower() == "n":
                    shop = False
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
                        shop = False

                # Användaren väljer om de vill fortsätta handla eller sluta
                print()
                if shop != False:
                    shop_cont = input("Vill du forstätta handla [Y/n]: ")
                    if shop_cont.lower() != "n":
                        shop = True
                    else:
                        shop = False

            # Användaren väljer sin gissning
            print()
            while True:
                choice = input("Datorn står och skakar två tärningar i handen. Tror du den kommer att slå [m]indre, [s]törre, eller [e]xact 6: ")
                print()
                if ((choice.lower() == "mindre") or (choice.lower() == "m") or (choice.lower() == "större") or (choice.lower() == "s") or (choice.lower() == "exact") or (choice.lower() == "6") or (choice.lower() == "exact 6") or (choice.lower() == "e")):
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

            # Användaren väljer om de vill använda något om de hareller inte
            if has_item:
                item = input("Vill du använda ett föremål [Y/n]: ")
                print()
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

                if jail_card <= 0:
                    has_item = False
                elif jail_card >= 1:
                    has_item = True

            # Datorns slag, sätts slumpat
            if cheat_choice == " ":
                rnd_num = random.randint(1, 12)
            print("Datorn kastar tärningarna, de studsar omkring")
            time.sleep(1.2)
            print()
            print("En av tärningarna snurrar...")
            time.sleep(2.4)
            print()
            print(f"Datorn slog {rnd_num}")

            # Kollar om gissningen är korrekt och updaterar vinsten/förlusten
            if ((choice.lower() == "mindre") or (choice.lower() == "m")) and (rnd_num < 6):
                print("Du gissade rätt, du vann!")
                amount *= mult
                point += amount
                jail_card_active = False
            elif ((choice.lower() == "större") or (choice.lower() == "s")) and (rnd_num > 6):
                print("Datorn fick större än 6, du vann!")
                amount *= mult
                point += amount
                jail_card_active = False
            elif ((choice.lower() == "exact") or (choice.lower() == "6") or (choice.lower() == "exact 6") or (choice.lower() == "e")) and (rnd_num == 6):
                print("Den fick exact 6, du vann stort!")
                amount *= jackpot_mult
                point += amount
                jail_card_active = False
            else:
                if jail_card_active == True:
                    print("Du gissade fel och förlorade, men kortet förhindrade någon förlust av poäng!")
                    point += amount
                    jail_card_active = False
                else:
                    print("Du gissade fel, du förlorade.")
                    amount = 0


            # Användaren väljer om de vill fortsätta
            cont_choice = input("Vill du fortsätta [Y/n]: ")
            if cont_choice.lower() != "n":
                cont = True
                first_round = False
            else:
                cont = False
                print()
                print(f"Tack för att du spelade, du slutade med {point} poäng!")
                print()
                exit()
        else: 
            print()
            game_over = input("Du har inga poäng kvar! Vill du starta om [Y/n]: ")
            print()
            if game_over.lower() == "n":
                restart = False
                exit()
            else:
                restart = True
                cont = False