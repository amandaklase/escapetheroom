import random
import time
import sys
import textwrap
import story_text
import first_choice_text
import search_room_text
import search_door_text
import search_bed_text
import search_end_table_text
import search_art_text
import search_tablet_text
from check_exit import check_exit

############# BIG HOUSE BREAKOUT ###############
#This is a text-based escape the room game.#


# (this is for my reference, so I remember all the items I want to hide around the room and is not used in code) game_inventory = ["key", "eye", "box", "screwdriver", "glass shard", "note", "blanket", "artist's name", "code"]

#global list useful in many functions
user_inventory = []

def format_text(text_variable):

    ### This format makes the large chunks of text more readable###

    print ("\n")
    dedented_text = textwrap.dedent(text_variable).strip()
    print(textwrap.fill(dedented_text, width=50))
    print ("\n")

def inventory_search(list_of_items_usable_on_object, user_name):

    ### This function allows the user to use her inventory###
    print ("You take a look at what you've collected:\n")

    if len(user_inventory) == 0:
        print ("You don't have anything yet.")

    else:
        for item in user_inventory:
            print (item)

        while True: 

            use_item = input("\nWould you like to try an item here? Type exit or the item name: ")

            if use_item == "exit":
                search_room(user_name)
            
            use_item = use_item.lower()

            if use_item in list_of_items_usable_on_object:
                print ("\nSuccess!")
                break

            elif use_item not in list_of_items_usable_on_object:
                print ("\nThis doesn't work here.")

            else:
                print ("\nYou don't have one of those! Maybe check your spelling?")

def play_game():

    ### This is the master function to play the game. It contains a welcome message that directs initial play and keeps things neater.###

    print ("********BIG HOUSE BREAKOUT********")
    
    user_name = input("\nWhat's your name? ")
    user_name = user_name.title()

    user_home = input("What city did you grow up in? ")
    user_home = user_home.title()
    
    print ('\n{}. . .{}. . .yo, {}, get up!'.format(user_name, user_name, user_name)) 
    story(user_name, user_home)
       
def story(user_name, user_home): 

    ### This function contains the story text for the game. It has user input return breaks to let the user read at her own pace.###

    #I haven't moved this section of text to the file because of problems with the .format method
    start_message_2 = 'It takes a moment to remember but when you do, your heart drops. You can still see Dallas-Bailey Blake’s sorrowful expression as you accepted the dreaded bouquet of black roses. The look of delight in the other contestant’s eyes as you walked the red carpet of elimination. You blew it, {}. You missed your chance to marry the dreamboat who was dating you concurrently with ten other people. Eleven if you count that hot mess Madison. (You don’t.)'.format(user_name) 
    
    format_text(story_text.start_message_1)
    keep_going = input("\nPress RETURN to continue")
    format_text(start_message_2)
    keep_going = input("\nPress RETURN to continue")
    format_text(story_text.start_message_3)
    keep_going = input("\nPress RETURN to continue")
    print ("\nWhat the hell’s going on here?")
    format_text(story_text.start_message_4)
    first_choice(user_home, user_name)
    
def first_choice(user_home, user_name):

    ### This contains the first choice the user makes and either gives more story or has a game over condition, depending on what she chooses. It also allows the user to choose to start searching the room.###

    while True:

        print ("\nPress the button?")  
        
        tablet = input("\na) Do it \nb) You're not my mom, tablet. You can't tell me what to do!\n >: ")
        tablet = tablet.lower()

        if tablet == "a":
            #didn't move this to file because of a problem with .format method
            tablet_message_5 = "Oh hell no. You did not come here all the way from {} to put up with this nonsense. You don't know if you can trust the PA, but you sure as hell know you want a way out.".format(user_home)

            format_text(first_choice_text.tablet_message_1)
            print ("\nThe screen goes dark.")  
            format_text(first_choice_text.tablet_message_2)

            video_2 = input("\nPress RETURN to play the video.")

            format_text(first_choice_text.tablet_message_3)
            format_text(first_choice_text.tablet_message_4)

            print ("\nThe video abruptly cuts off.")
            format_text(tablet_message_5)

            start_search = input("\nPress RETURN to search the room.")

            search_room(user_name)


        elif tablet == "b":

            format_text(first_choice_text.tablet_no_1)
            ignore_tablet = input("\nPress RETURN to continue.")
            format_text(first_choice_text.tablet_no_2)
            format_text(first_choice_text.tablet_no_3)
           
            print ("\nGAME OVER")

            try_again = input("\nWould you like to play again? Type 'quit' to end game. ")

            if try_again == "quit":
                check_exit(try_again)  
            
            else:
                play_game()

        elif tablet == "quit":
            check_exit(tablet)

        else:
            print ("The only options are a or b, friend. Unless you'd like to quit? Type 'quit' to end game. ")   

def search_room(user_name):

    ### This function allows the user to pick different general areas of the room to search ###
    
    contents_of_room = {"a.":"door", "b.":"bed", "c.":"end table", "d.":"painting", "e.":"tablet", "quit.":"quit"}
    
    format_text(search_room_text.room_description)
    print ("\n")

    if "box" in user_inventory:
        contents_of_room["f."] = "try to open box"
    
    for content in contents_of_room:
        print (content, contents_of_room[content])
          
    while True:

        direction_to_search = input("> ")
        direction_to_search = direction_to_search.lower()

        if direction_to_search == "a":
            search_door(user_name)

        if direction_to_search == "b":
            search_bed(user_name)

        if direction_to_search == "c":
            search_end_table(user_name)

        if direction_to_search == "d":
            search_art(user_name)

        if direction_to_search == "e":
            search_tablet(user_name)

        if direction_to_search == "quit":
            check_exit(direction_to_search)
                
        if direction_to_search == "f":
            open_box(user_name)

        else:
            print ("invalid entry. Try again.")

def search_door(user_name):
    
    ###This function take a closer look at the door and checks if the user is able to unlock it###
    
    list_of_items_usable_on_object_1_1 = ["eye", "keycard"]

    format_text(search_door_text.door_message_1) 

    if len(user_inventory) == 0:
        format_text(search_door_text.door_message_2)
        format_text(search_door_text.door_message_3)
        
        while True:

            another_search = input("You'll try the door again when you have a plan. Press RETURN to search somewhere else. ")
            search_room(user_name)
        
    elif len(user_inventory) > 0:
        lock_search = input("Try the lock with some of the items you've found, y/n?: ")
        lock_search = lock_search.lower()

        if lock_search == "y" and "keycard" in user_inventory:
            format_text(search_door_text.first_lock)
            
            if "eye" in user_inventory and "blanket" in user_inventory:
                format_text(search_door_text.second_lock)
                time.sleep (2)

                print ('"Identity confirmed, Mike Shapiro. All hail Shaavoth."\n\nYou hold your breath as you try the handle...')
                
                format_text(search_door_text.no_blanket_1)
                keep_going = input("\nPress RETURN to continue ")
                format_text(search_door_text.no_blanket_2)
                keep_going = input("\nPress RETURN to continue ")
                format_text(search_door_text.no_blanket_3)
                keep_going = input("\nPress RETURN to continue ")
                

                if "note" not in user_inventory:
                    format_text(search_door_text.no_blanket_5)
                    format_text(search_door_text.no_blanket_6)
                
                format_text(search_door_text.no_blanket_4)

                again = input("Would you like to play again? Type 'quit' to exit: ")
                again = again.lower()

                check_exit(again)

            elif "eye" in user_inventory and "blanket" not in user_inventory:
                format_text(search_door_text.second_lock)
                time.sleep (2)

                print ('"Identity confirmed, Mike Shapiro. All hail Shaavoth."\n\nYou hold your breath as you try the handle... \nThe door swings open and you stumble into freedom. \nCongratulations, {} you win!\n'.format(user_name))

                again = input("Would you like to play again? Type 'quit' to exit: ")
                again = again.lower()

                check_exit(again)

            else:
                format_text(search_door_text.no_eye)
            
        elif lock_search == "y" and "eye" in user_inventory and "keycard" not in user_inventory:
            format_text(search_door_text.no_key)
            search_room(user_name)

        if lock_search == "y" and "keycard" not in user_inventory and "eye" not in user_inventory:
            inventory_search(list_of_items_usable_on_object_1_1, user_name)

        elif lock_search == "n":
            search_room(user_name)

        else:
            print ("invalid choice.")
            search_door(user_name)

def search_bed(user_name):

    ###This function lets the user take a closer look at the bed and find the hidden objects necessary for escape###

    bed_areas = {"a.":"search pillow", "b.":"search blanket", "c.": "search underneath bed", "d.":"search underneath mattress", "e.":"return to main search", "quit.":"quit game"}


    format_text(search_bed_text.bed_1)

    while True:

        print ("Which part of the bed would you like to search?")
        for item in bed_areas:
            print (item, bed_areas[item]) 
        
        user_action = input("> ")
        user_action = user_action.lower()

        if user_action == "a":
            format_text(search_bed_text.pillow_message_1)
            eat_mint = input("> ")
            eat_mint = eat_mint.lower()

            if eat_mint == "y":
                if "note" in user_inventory:
                    format_text(search_bed_text.pillow_message_2)
                    format_text(search_bed_text.pillow_message_3)
                    format_text(search_bed_text.pillow_message_4)
                if "note" not in user_inventory:
                    format_text(search_bed_text.pillow_message_2)
                    format_text(search_bed_text.pillow_message_3)
                    format_text(search_door_text.no_blanket_5)
                    format_text(search_bed_text.pillow_message_4)

                print ("GAME OVER")

                try_again = input("\nWould you like to play again, y/n? ")
                try_again = try_again.lower()
                
                if try_again == "y":
                    play_game()
                    return
                elif try_again == "n":
                    sys.exit("GAME OVER")

            if eat_mint == "n":
                format_text(search_bed_text.pillow_message_5)
            else:
                print ("invalid choice")
        
        elif user_action == "b":
            if "blanket" in user_inventory:
                format_text(search_bed_text.blanket_message_2)

            if "blanket" not in user_inventory:
                format_text(search_bed_text.blanket_message)
                user_inventory.append("blanket")           
        elif user_action == "c":
            if "screwdriver" not in user_inventory: 
                format_text(search_bed_text.under_bed_message_1)

            elif "screwdriver" in user_inventory:
                format_text(search_bed_text.under_bed_message_2)
        
        elif user_action == "d":
            if "screwdriver" in user_inventory:
                print ("You already picked up the screwdriver. There's nothing else here.")

            if "screwdriver" not in user_inventory:
                format_text(search_bed_text.under_mattress_message)
                user_inventory.append("screwdriver")
               
        elif user_action == "e":
            search_room(user_name)

        elif user_action == "quit":
            check_exit(user_action)

        else: 
            print ("This does nothing.")
   
def search_end_table(user_name):

    ### This function allows the user to take a closer look at the table, and perform actions and find and use inventory items.###

    end_table_areas = {"a.":"search vase", "b.":"search underneath table", "c.":"return to main search", "quit.":"quit game"}
   
    list_of_items_usable_on_object_1_3 = ["screwdriver"]
    format_text(search_end_table_text.end_table_1)

    while True:

        print ("Which area of the end table would you like to search?")

        for item in end_table_areas:
            print (item, end_table_areas[item]) 
        
        user_action = input("> ")
        user_action = user_action.lower()

        if user_action == "a" and "glass shard" in user_inventory:
            print ("\nNothing left to smash here.")

        elif user_action == "a" and "note" not in user_inventory:
            format_text(search_end_table_text.vase_message_1)
            format_text(search_end_table_text.vase_message_2)

            red_paper = input("Retrieve the paper, y/n? ")
            red_paper = red_paper.lower()

            if red_paper == "y":
                format_text(search_end_table_text.paper_message_1)
                eat_it = input("Eat the paper, y/n? ")
                eat_it = eat_it.lower()
                if eat_it == "y":
                    format_text(search_end_table_text.paper_message_4)
                    user_inventory.append("note")
                if eat_it == "n":
                    format_text(search_end_table_text.paper_message_2) 

            elif red_paper == "n":
                format_text(search_end_table_text.paper_message_3)

            format_text(search_end_table_text.vase_message_3)
            
            break_vase = input("Smash the vase, y/n? ")
            break_vase = break_vase.lower()

            if break_vase == "y":
                format_text(search_end_table_text.vase_message_4)
                user_inventory.append("glass shard")

            elif break_vase == "n":
                format_text(search_end_table_text.vase_message_5)
        
        elif user_action == "a" and "note" in user_inventory:
            format_text(search_end_table_text.vase_message_3)
            
            break_vase = input("Smash the vase, y/n? ")
            break_vase = break_vase.lower()

            if break_vase == "y":
                format_text(search_end_table_text.vase_message_4)
                user_inventory.append("glass shard")

            elif break_vase == "n":
                format_text(search_end_table_text.vase_message_5)
        
        elif user_action == "b":
            format_text(search_end_table_text.underneath_table_message)
            if "box" in user_inventory:
                print ("There's nothing else to see here.\n")
            elif "box" not in user_inventory: 
                move_table = input("Move the table and uncover the vent, y/n? ")
                move_table = move_table.lower()

                if move_table == "y":
                        format_text(search_end_table_text.search_vent_message)
                        format_text(search_end_table_text.vent_message_2)

                        if "screwdriver" not in user_inventory:
                            search_end_table(user_name)

                        if "screwdriver" in user_inventory:
                            format_text(search_end_table_text.vent_message_3)
                            search_vent = input("Look at inventory, y/n? ")
                            search_vent = search_vent.lower()

                            if search_vent == "y":
                                inventory_search(list_of_items_usable_on_object_1_3, user_name) 
                                format_text(search_end_table_text.vent_message_4)
                                user_inventory.append("box")
                                format_text(search_end_table_text.vent_message_5)
                                try_box_code = input("Would you like to input a code to open the box, y/n? ")
                                try_box_code = try_box_code.lower() 

                                if try_box_code == "y":
                                    open_box(user_name)  
                                    user_inventory.append("box")

                                elif try_box_code == "n":
                                    format_text(search_end_table_text.box_message)
                                else:
                                    print ('invalid choice')

                elif move_table == "n":
                    print ("Okay.")
                    search_end_table(user_name)

                else:
                    print ("invalid")    
                        
        elif user_action == "c":
            search_room(user_name)
        
        elif user_action == "quit":
            check_exit(user_action)
        
        else: 
            print ("\ninvalid choice.")

def open_box(user_name):

    #This function allows the user to play a mini game of sorts, entering a code (that is hidden elsewhere in the room) to unlock a box to retrieve one of the door keys

    code = "96431"
    open_box_message = "Your fingers hover over the brass slides, ready to try a 5 digit code."
    format_text(open_box_message)
    code_guess = input("Enter Code: ")

    while code_guess != code: 

        if code_guess.isdigit() and len(code_guess) == 5:
            print("Wrong code. The box stays firmly locked.")
            another_try = input("Try again, y/n? ")
            if another_try == "y":
                print ("Okay!")
            elif another_try == "n":
                break
            else:
                print ('invalid choice')
        else:
            print("Invalid code. Code requires 5 digits")

        code_guess = input("Enter Code: ")

    if code_guess == code:
        box_message_1 = "The code works! You pop the lid of the box and almost drop it when you see what's inside. There, nestled in red velvet, is an eyeball. A blue-eyed eyeball. A blue-eyed eyeball in Mike Shapiro's signature hue. Did the PA pry it out of him to help you? What happened to the rest of him? It's horrifying, it's disgusting, it's...potentially useful? You shudder, closing the box up and putting it in your pocket."
        format_text(box_message_1)
        user_inventory.append("eye")
        search_room(user_name)

def search_art(user_name):
    
    ### This function allows the user to take a closer look at the painting, and perform actions and find and use inventory items.###
    
    art_areas = {"a.":"painting", "b.":"frame", "c.":"return to main search", "quit.":"quit game"}
   
    list_of_items_usable_on_object_1_4 = ["glass shard"]

    list_of_items_usable_on_object_1_5 = ["blanket"]

    format_text(search_art_text.art_1)

    while True:

        print ("What part of the painting would you to like to see?")

        for item in art_areas:
            print (item, art_areas[item]) 
        
        user_action = input("> ")
        user_action = user_action.lower()

        if user_action == "a" and "artist's name: Henry Armitage" in user_inventory:
            format_text(search_art_text.painting_7)
            search_room(user_name)
    
        elif user_action == "a" and "keycard" not in user_inventory:
            format_text(search_art_text.painting_1)
            format_text(search_art_text.painting_2)
            format_text(search_art_text.painting_3)

        elif user_action == "a" and "keycard" in user_inventory and "blanket" not in user_inventory:
            format_text(search_art_text.painting_1)
            format_text(search_art_text.painting_2)
            format_text(search_art_text.painting_4)

        elif user_action == "a" and "blanket" in user_inventory and "keycard" in user_inventory:
            format_text(search_art_text.painting_4)
            format_text(search_art_text.painting_8)
            cover_painting = input("Look at inventory, y/n? ")
            cover_painting = cover_painting.lower()

            if cover_painting == "y":
                inventory_search(list_of_items_usable_on_object_1_5, user_name)
                format_text(search_art_text.painting_5)
                format_text(search_art_text.painting_6)
                user_inventory.remove("blanket")
                user_inventory.append("artist's name: Henry Armitage")

            elif cover_painting == "n":
                print ("Okay.")
            
            else:
                print ("Invalid response. Try again.")
                

        elif user_action == "b" and "keycard" not in user_inventory and "glass shard" not in user_inventory:           
            format_text(search_art_text.frame_1)
            format_text(search_art_text.frame_2)
            format_text(search_art_text.frame_3)

        elif user_action == "b" and "keycard" not in user_inventory and "glass shard" in user_inventory:
            
            format_text(search_art_text.frame_1)
            format_text(search_art_text.frame_2)
            format_text(search_art_text.frame_4)
            
            search_wallpaper = input("Look at inventory, y/n? ")
            search_wallpaper = search_wallpaper.lower()

            if search_wallpaper == "y":
                inventory_search(list_of_items_usable_on_object_1_4, user_name)
                user_inventory.append("keycard")

                format_text(search_art_text.frame_5)
                format_text(search_art_text.frame_6)

            elif search_wallpaper == "n":
                print ("Okay.")
                search_room(user_name)

            else:
                print ("invalid choice")

                
        elif user_action == "b" and "keycard" in user_inventory and "artist's name: Henry Armitage" not in user_inventory:
            format_text(search_art_text.frame_7)
            
            
        elif user_action == "c":
            search_room(user_name)
        
        elif user_action == "quit":
            check_exit(user_action)
        
        else: 
            print ("invalid choice")

def search_tablet(user_name):

     ### This function allows the user to take a closer look at the tablet, and to play the mini game perform actions and find and use inventory items.###

    tablet_areas = {"a.":"app", "b.":"return to main search", "quit.":"quit game"}
    
    format_text(search_tablet_text.tablet_description_1)
    format_text(search_tablet_text.tablet_description_2)

    while True:
        print ("Take a closer look?")
        for item in tablet_areas:
            print (item, tablet_areas[item]) 
        
        user_action = input("> ")
        user_action = user_action.lower()

        if user_action == "a" and "box" in user_inventory:

            format_text(search_tablet_text.app_1) 
                
            print ("That's the same design on the lockbox. Think they're connected?\n")

            click_app = input("Click on it, y/n? ")
            click_app = click_app.lower()
                
            if click_app == "y":
                format_text(search_tablet_text.app_2)
                play_app_game = input("Want to play it, y/n? ")
                
                if play_app_game == "y":
                    format_text(search_tablet_text.app_3)
                    time.sleep(2)
                    play_mini_game()
                    search_room(user_name)

                elif play_app_game == "n":
                    print ("This is no time for games.")
                    search_room(user_name)

                else:
                    print ("invalid choice")
            
            elif click_app == "n":
                print ("Maybe later.")
                search_room(user_name)
            else:
                print ("invalid choice")
        

        if user_action == "a" and "box" not in user_inventory:

            format_text(search_tablet_text.app_1)

            click_app = input("Click on it, y/n? ")
            click_app = click_app.lower()
                
            if click_app == "y":
                format_text(search_tablet_text.app_2) 
                play_app_game = input("Want to play it, y/n? ")
                
                if play_app_game == "y":
                    format_text(search_tablet_text.app_3)
                    time.sleep(2)
                    play_mini_game()
                    search_room(user_name)

                elif play_app_game == "n":
                    print ("This is no time for games.")
                    search_room(user_name)

                else:
                    print ("invalid choice")
            
            elif click_app == "n":
                print ("Maybe later.")
                search_room(user_name)
            else:
                print ("invalid choice")

        elif user_action == "b":
            search_room(user_name)
        
        elif user_action == "quit":
            sys.exit("GAME OVER")
        
        else:
            print ("invalid entry")

def play_mini_game():
    ### This function is its own mini-game, a puzzle that needs to be solved in order to escape the room ###
    print ("*****ESCAPE SHAAVOTH'S LAIR****\n")

    format_text(search_tablet_text.mini_game_message)
    
    health = 3
    
    while health >= 1:
        shoot = input("\nPress RETURN to fire. ")
        
        if random.randint(1, 2) ==1:
            health = health - 1
            print ("Before you can shoot, Shaavoth lashes out, \nstriking you with a tentacle.")
            print ("Your health:", health) 
        
        else:
            print ("You took a shot and missed, blasphemer. \nShaavoth, blinks his thousand eyes, amused.")
            print ("Your health:", health)
    
    print ("\nGame Over \nYou have been defeated. \nThere is no escaping Shaavoth's lair....")  
    
    print ("\nHigh Scores\n")
    
    high_scores = ["FIND   90000", "BOX    06000", "GET    00400", "OUT    00030", "NOW    00001"]
    
    for high_score in high_scores:
        print (high_score)
        time.sleep (1)
    

    print ("9-6-4-3-1. Hmmm. Seems important. You make a mental note to remember that.")
    user_inventory.append("code is 96431")

play_game()




    







