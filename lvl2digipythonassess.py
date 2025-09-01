#NOTE on first run ENSURE that NO file called "db.txt" exists in the same directory!!!
#TODO
# add modification of existing cards
# add deletion of cards
# consolodate repeated strings to top of file
# redo all inputs to be easier to repeated
# import os to clear console
# make input a function


try:
    # attempts to create the default db.txt, if a file with the name db.txt exists this will skip (allowing for modified versions to exist)
    print("creating db...")
    with open('db.txt', 'x') as db:
        print("populating...")
        db.write('Stoneling\n7\n1\n25\n15\nVexscream\n1\n6\n21\n19\nDawnmirage\n5\n15\n18\n22\nBlazegolem\n15\n20\n23\n6\nWebsnake\n7\n15\n10\n5\nMoldvine\n21\n18\n14\n5\nVortexwing\n19\n13\n19\n2\nRotthing\n16\n7\n4\n12\nFroststep\n14\n14\n17\n4\nWispghoul\n17\n19\n3\n2\n')
        print("done!")
except:
    print('db already exists!')
running = True
editing = False
selected_card = ''
selected_cards = []
searching = False
stats = ["Name", "Strength", "Speed", "Stealth", "Cunning"] #for later use
name_index=[]

def card_read(card_name_index):#put anything other than the starting index in here and you shall find a quick death
    card_details_list = []
    with open('db.txt') as db:
        cards_details_list = list(db)
    for i in range(5):
        card_details_list.append(cards_details_list[card_name_index + i]) #create a list with all of the data for the specified card (each card has 5 lines of data)
    card_details_list = ' '.join(card_details_list).replace("\n", "").split() #turn into a string to remove the \n at the end then back into a list
    return("{:<13} {:>3} {:>7} {:>9} {:>8}".format(*card_details_list)) #13 char limit for names, format into nice rows

def card_add():
    adding_card = True
    print("Please input the details of your new card as follows:\nName Strength Speed Stealth Cunning | seperated by spaces\nEg: Newcard 12 8 7 3")
    while adding_card:
        try:
            new_card_list = []
            new_card_list = (input(": ")).split()
            if len(new_card_list) > 5 or len(new_card_list) < 5:
                print("Invalid card input, please try again")
            else:

                try:
                    #will result in error if non numbre inputed
                    for i in range(1, 5):
                        int(new_card_list[i])
                except:
                    print("Invalid card input, please try again")
                is_pass = True
                for i in range(1, 5):
                    if int(new_card_list[i]) < 1 or int(new_card_list[i]) > 25:
                        is_pass = False
                if is_pass == True:
                    print("do you wish to add this card: ")
                    print("Name:    Strength   Speed   Stealth  Cunning")
                    print("{:<13} {:>3} {:>7} {:>9} {:>8}".format(*new_card_list))
                    write_conf = input("y/N: ")
                    if write_conf.lower() == 'y':
                        with open('db.txt', 'a') as db:
                            for i in range(5):
                                db.write((new_card_list[i]) + '\n')
                        adding_card = False
                        return("Changes written")
                    else:
                        adding_card = False
                        return("no writes made")

                else:
                    print("Invalid card input (max value 25, min 1), please try again")
        except:
            return("error, please try again\nExiting card adder, please run again!")



def card_edit(selected_card):
    print("Modify card:")
    print("Name:    Strength   Speed   Stealth  Cunning")
    print(card_read(selected_card))
    edit_loop = True
    while edit_loop:
        try:
            modify_selection = input("Which attrabute do you wish to modify (number)\n1 2 3 4 or 5\n# ")
        except:
            print("Woah there pal!")
        try:
            if int(modify_selection) in range(1, 6):
                print("you have selected to modify ", stats[int(modify_selection)-1])
                try:
                        modify_value = input("What do you want to change this value to?\n# ")
                except:
                    ("Woah there pal!")
            else:
                print("Invalid number!")
        except:
            if modify_selection.lower() == 'q':
                edit_loop = False
                return("Exiting!")
            elif len(modify_selection) == 0:
                print('')

            print("Please input a number!")
def card_remove(selected_card):
    return

def card_search(count):
    global selected_cards
    try:
        search_term = int(input("Please input what you'd like to search for cards by:\nName [returns exact matches] 0) Strength 1) Speed 2) Stealth 3) Cunning 4)\n? "))
    except:
        print("Error")
        return("Error thrown, exiting the Wizard")
    valid_cards_index = []
    valid_cards = []
    if search_term == 0:
        card_names = []
        card_name = ""
        searched_name = input("Please provide the whole name of the card you wish to find\n: ")
        with open('db.txt') as db:
            card_names = list(db)
        for i in range(count):

            if (card_names[i]).lower() == ((searched_name).lower() + "\n"): # ignore case just like ntfs
                card_name = card_names[i] #if the card is an exact match then return it's name (might add partial matches later)
                print("Name:    Strength   Speed   Stealth  Cunning")
                selected_cards = [i]
                return(card_read(i))
        else:
            return("No card With the specified name was found (did you forget a capital or add a space?)")
    if search_term in range(1,5):
        stat_out = []
        print("Value of ", stats[search_term], " ")
        stat = input("[ ")+"\n"#the way I call on the db adds \n so I add it here to be matched later

        with open('db.txt') as db:#use with so that it closes the txt
            stat_out = list(db)
        for i in range(int(count/5)): #making this an int then /5 isn't all that bad since the txt SHOULD always be divisable by 5
            if stat_out[(search_term)+(i*5)] == stat:#every search_term (attrabutes 1 - 4) +5 so that it only searches for the desired attrabute
                valid_cards_index.append(((search_term)+(i*5))-search_term)#create an array with the index of where the name is in the full db array,
        for i in range(len(valid_cards_index)):
            valid_cards.append(card_read(valid_cards_index[i]))

        if len(valid_cards_index) == 0:
            return("sorry, no cards match your search")

        else:
            selected_cards = valid_cards_index
            print("Name:    Strength   Speed   Stealth  Cunning")
            return('\n'.join(valid_cards))
    else:
        return("Unexpected error, outside of given range!")#if this error is ever thrown something has gone VERY wrong

#Main body of the program the "void_loop()" for all you arduino fans------------------------------------------------------------------
print("Welcome User to the \nMonster Card Catalogue!!!!!!!!!!!\n")
print("What would you like to do?\nView Database 1) Add a card 2) Modify Databse 3) Help [this prompt] h) Quit q)\n")
while running == True:

    while editing:
        try:
            eselection = input("$ ").lower()
        except:
            print("Woah there pal!\n")
            eselection = ''
        if eselection == '1':
            print(card_edit(selected_card))
        elif eselection == '2':
            break
        elif eselection == '3':
            break
        elif eselection == 'q':
            print("Back to main menu, your changes have been saved!")
            editing = False
        elif eselection == 'h':
            print('\nModify Card 1) Remove Card 2) Help [this prompt] h) Quit q)\n')
        elif len(eselection) == 0:
            print('')
        else:
            print("That is not a valid selection!\n")


    with open('db.txt') as db:
        count = sum(1 for _ in db)#amount of lines
    name_index = []
    for i in range(int((count/5))):
        name_index.append(i*5)

    try:
        selection = input('~ ').lower()
    except:
        print("Woah there pal!\n")
        selection = ''

    if selection == '1':
        print(count)
        print("Name:    Strength   Speed   Stealth  Cunning")
        for i in range(int(count/5)):
            print(card_read(name_index[i]))
    elif selection == '2':
        print(card_add())
    elif selection == '3':
        print("\nModifying Menu\n--------------------------\nPlease input what you'd like to do:\nStart the Search Wizard 1) Help [this prompt] h) Back q)\n")
        searching = True
        while searching:
            try:
                sselection = input("? ").lower()
            except:
                print("Woah there pal!")
                sselection = ''
            if sselection == '1':
                print(card_search(count))
                print("--Exiting the Wizard \"May you have a Splended day!\"--")
                if len(selected_cards) == 0:
                    print("No cards selected")
                elif len(selected_cards) == 1:
                    print("Do you wish to edit this card?")
                    try:
                        go_to_edit = input("y/N: ")
                    except:
                        print("Woah there pal!")
                    if go_to_edit.lower() == 'y':
                        editing = True
                        selected_card = selected_cards[0]
                        selected_cards = []
                        print("\nEditing Menu\n--------------------------\nMake your choice:\nModify Card 1) Remove Card 2) Help [this prompt] h) Quit q)\n")
                        searching = False
                else:
                    print("You have ", len(selected_cards), " cards selected\nwhich do you wish to modify? Type card number (eg \'1\' for the first card) or to edit none (enter any key)")
                    try:

                        go_to_edit = input('$? ')

                    except:
                        print("Woah there pal!")
                    for i in range((int(len(selected_cards)))):
                        try:
                            if (int(go_to_edit)-1) > len(selected_cards) or (int(go_to_edit)) < 1: #catch out of bounds numbers (minimum number is 1)
                                print("invalid card selected (number too high or low)\n")
                            elif selected_cards[int(go_to_edit)-1] == selected_cards[i]: #if the index of our input matches the index of the the avalible cards
                                selected_card = selected_cards[i]
                                selected_cards = []
                                print("you have selected: ")
                                print(card_read(int(selected_card)))
                                editing = True
                                print("\nEditing Menu\n--------------------------\nMake your choice:\nModify Card 1) Remove Card 2) Help [this prompt] h) Quit q)\n")
                                searching = False #kicks user into edit menu

                        except:
                            print("No card selected for editing!\n")
            elif sselection == 'q':
                print("Back to main menu!")
                searching = False
            elif sselection == 'h':
                print("\nStart the Search Wizard 1) Help [this prompt] h) Back q)\n")
            elif len(sselection) == 0:
                print('')
    elif selection == 'q':
        print("Good day.")
        break
    elif selection == 'h':
        print('\nView Database 1) Add a card 2) Modify Database 3) Help (this prompt) h) Back q)')
    elif len(selection) == 0:
        print('')
    else:
        print("That is not a valid selection!\n")

# By Logan T Wood
# NSN 143831077
# No clanker told me how to write this, I am the one who makes the computers think
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⠿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿
# ⣿⣿⡏⠁⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣦⣤⡄⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿
# ⣿⣿⣷⣄⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡧⠇⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣾⣮⣭⣿⡻⣽⣒⠀⣤⣜⣭⠐⢐⣒⠢⢰⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣏⣿⣿⣿⣿⣿⣿⡟⣾⣿⠂⢈⢿⣷⣞⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣷⣶⣾⡿⠿⣿⠗⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⠋⠉⠑⠀⠀⢘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⡿⠟⢹⣿⣿⡇⢀⣶⣶⠴⠶⠀⠀⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⡿⠀⠀⢸⣿⣿⠀⠀⠣⠀⠀⠀⠀⠀⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠹⣿⣧⣀⠀⠀⠀⠀⡀⣴⠁⢘⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿
# ⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⠗⠂⠄⠀⣴⡟⠀⠀⡃⠀⠉⠉⠟⡿⣿⣿⣿⣿
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠾⠛⠂⢹⠀⠀⠀⢡⠀⠀⠀⠀⠀⠙⠛⠿⢿
