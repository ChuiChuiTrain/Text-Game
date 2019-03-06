"""
-------------------------------------------------------------------------------
Name: Adventure_Game.py
Purpose: To create an entertaining textbased game

Author:		Chui.G

Created:   22/01/2016
------------------------------------------------------------------------------
"""


import random

#room values and variables
room_list = []
room_grid = [[11,12,13,14,15],[21,22,23,24,25],[31,32,33,34,35]]
can_do = True
can_go = True
done = False
north_southpos = 0
east_westpos = 0
game_finish = False
game_over = None
game = True

#prints out map in the beginning
print ("+-----------+-----------+-----------+----------+----------+")
print ("|You are    |           |           |          |          |")
print ("|here.      |           |           |          |          |")
print ("|           |           |           |          |          |")
print ("|           |           |           |          |          |")
print ("|           |           |           |          |          |")
print ("+-----------+-----------+-----------+----------+----------+")
print ("|           |           |           |          |          |")
print ("|           |           |           |          |          |")
print ("|           |           |           |          |          |")
print ("|           |           |           |          |          |")
print ("|           |           |           |          |          |")
print ("|           |           |           |          |          |")
print ("+-----------+-----------+-----------+----------+----------+")
print ("|           |           |           |          |  /    \  |")
print ("|           |           |           |          | | () ()| |")
print ("|           |           |           |          |  \  ^ /  |")
print ("|           |           |           |          |   HHHH   |")
print ("|           |           |           |          |   \__/   |")
print ("|           |           |           |          |          |")
print ("+-----------+-----------+-----------+----------+----------+")


def main():
    """Start the game through a function"""
    global done
    global game
    global north_southpos
    global east_westpos
    global room_list
    global room_grid
    global can_do
    global can_go
    global inventory
    global room_lay1
    global room_lay2
    global room_lay3
    global room_list
    global equipped
    global base_attack
    global inventory
    global can_do
    global health
    global game_finish
    global game
    global game_over

    #item values
    weapons = [["Spear",4,"Nothing"],["Rapier",3,"Nothing"],["Knife",1,"Nothing"],["Broad Sword",2,"Nothing"],["Old Musket",17,"Nothing"],["Torch",1,"Flame"],["Burning  Sword",3,"Flame"]]
    armour = []
    potions = ["Mysterious potion","Health potion","Rage potion"]

    #character values
    health = 15
    base_attack = 1
    inventory = [["Mysterious potion",1],["Health potion",0],["Rage potion",0]]
    equipped = ["Nothing",0,"Nothing"]

    #monster values (name,health,damage,armour,special effects)
    monsters = [["Slime",3,1,None],["Lowly Goblin",2,1,None],["Skeleton",3,2,None],["Novice Necromancer",3,2,None],
    ["Animated armour",5,3,None],["Necromancer",4,4,None],["Armed Skeleton",7,3,None],["Mud Golem",5,3,"Resist"],["Pyromancer",5,2,"Flame"],
    ["Deathcharger",6,4,"Charge"],["Goblin Gloryseeker",10,3,"Resist"],["Dancing Swords",5,4,None],["Fire Elemental",10,3,"Flame"],
    ["The Soul Collector",25,4,"Nevermore"]]


    def mystery():
        """set mysterious potion chances and what they do"""
        pot_chance = random.randint(1,100)
        global health
        global base_attack
        if pot_chance <= 25:
            health += 3
        if pot_chance >= 26 and pot_chance <= 35:
            health += -2
        if pot_chance >= 36 and pot_chance <= 45:
            base_attack += 1
        if pot_chance >= 46 and pot_chance <= 70:
            health += 1
        if pot_chance >= 71 and pot_chance <= 75:
            base_attack += -1
        if pot_chance >= 76 and pot_chance <= 90:
            health += -1
        if pot_chance >= 91 and pot_chance <= 95:
            base_attack += 2
        if pot_chance >= 96:
            health = 15


    def potion():
        """Enables potion use"""
        global inventory
        global can_do
        global health
        global base_attack
        if user_in.lower() == "mysterious potion":
            can_do = True
            if inventory[0][1] >= 1:
                mystery()
                inventory[0][1] = inventory[0][1] - 1
            else:
                print ("You do not have a Mysterious potion.")

        elif user_in.lower() == "health potion":
            if inventory[1][1] >= 1:
                health += 4
                inventory [1][1] = inventory[1][1] - 1
            else:
                print ("You do not have a Health potion.")

        elif user_in.lower() == "rage potion":
            if inventory[2][1] >= 1:
                base_attack += 1
                health += -2
                inventory[2][1] = inventory[2][1] - 1
            else:
                print ("You do not have a Rage potion.")
        else:
            can_do = False


    def monster_chance():
        """Monster fighting"""
        global room_lay1
        global room_lay2
        global room_lay3
        global room_list
        global north_southpos
        global east_westpos
        global equipped
        global base_attack
        global inventory
        global can_do
        global health
        global game_finish
        global game
        global game_over

        correct_input = True
        fight = False
        flame_charge = 0
        player_flame = 0

        #check which level user is on and give program data as to which monsters should user be fighting on that level and also spawn monsters at a 25% chance
        if room_list[north_southpos][east_westpos] == room_list[2][4]:
            print ("You have a very bad feeling about this.")
            selected_monster = monsters[13]
            monster_health = selected_monster[1]
            fight = True
        if can_do == True and can_go == True:
            spawn = random.randint(1,100)
            if spawn >= 75 and room_list[north_southpos][east_westpos] != room_list[0][0] and room_list[north_southpos][east_westpos] != room_list[2][4]:
                for i in room_lay1:
                    if i == room_list[north_southpos][east_westpos]:
                        selected_monster = monsters[random.randint(0,3)]
                        monster_health = selected_monster[1]
                        fight = True
                for i in room_lay2:
                    if i == room_list[north_southpos][east_westpos]:
                        selected_monster = monsters[random.randint(4,8)]
                        monster_health = selected_monster[1]
                        fight = True
                for i in room_lay3:
                    if i == room_list[north_southpos][east_westpos]:
                        selected_monster = monsters[random.randint(9,12)]
                        monster_health = selected_monster[1]
                        fight = True

            while fight == True:

                #check for special effects on monsters and give data as to what they do
                if selected_monster[3] == "Charge":
                    print ("Before you can react a deathcharger attacks you.")
                    health += -1*(selected_monster[2])
                if selected_monster[3] == "Flame" and flame_charge > 0 or selected_monster[3] == "Nevermore" and flame_charge > 0:
                    print ("You take an additional",flame_charge,"burn damage.")
                    health += -1*(flame_charge)

                #print out UI
                print ("Inventory:","   Mysterious Potion(s):",inventory[0][1],"  Health Potion(s):",inventory[1][1],"   Rage Potion(s):",inventory[2][1])
                print ("Your health:",health,"    Your attack:",base_attack+equipped[1])
                print (selected_monster[0],"    Health:",monster_health,"    Attack:",selected_monster[2],"    Special:",selected_monster[3])


                #If you die prompt user with game over and bring user to main menu
                if health <= 0:
                    game_over = input("Game over you have died.Type anything to go to main menu. ")
                    if game_over != None:
                        main()
                if game_over != None:
                        break

                #get user to tell whether to attack defend or drink a potion and check if it is a valid input
                user_in = input("What do you do? (Attack,Defend,Drink potions) ")

                if user_in.lower() == "attack":
                    if selected_monster[3] == "Resist" or selected_monster[3] == "Nevermore":
                        resist_chance = random.randint(1,100)
                    if selected_monster[3] == "Resist" and resist_chance >= 50 or selected_monster[3] == "Nevermore" and resist_chance >= 50:
                        print ("The monster resisted your attack and only took half damage.")
                        monster_health += -1*(equipped[1]+base_attack)/2
                    else:
                        monster_health += -1*(equipped[1]+base_attack)
                    if equipped[2] == "Flame" and player_flame > 0:
                            print ("The monster took an additional",player_flame,"burn damage.")
                            monster_health += -1*player_flame
                    if equipped[2] == "Flame":
                        player_flame += 1
                    correct_input = True

                elif user_in.lower() == "defend":
                    if selected_monster[3] == "Resist":
                        resist_chance = random.randint(1,100)
                    if selected_monster[3] == "Resist" and resist_chance >= 50:
                        print ("The monster resisted your attack and only took half damage.")
                        monster_health += -1*(equipped[1]+base_attack)/4
                    else:
                        monster_health += (-1*(equipped[1]+base_attack))/2
                    if equipped[2] == "Flame" and player_flame > 0:
                            print ("The monster took an additional",player_flame,"burn damage.")
                            monster_health += -1*player_flame
                    if equipped[2] == "Flame":
                        player_flame += 1
                    correct_input = True

                elif user_in.lower() != "defend" and user_in.lower() != "attack":
                    if user_in.lower() == "mysterious potion":
                        can_do = True
                        if inventory[0][1] >= 1:
                            mystery()
                            inventory[0][1] = inventory[0][1] - 1
                            correct_input = True
                        else:
                            print ("You do not have a Mysterious potion.")
                            correct_input = False

                    elif user_in.lower() == "health potion":
                        if inventory[1][1] >= 1:
                            health += 4
                            inventory [1][1] = inventory[1][1] - 1
                            correct_input = True
                        else:
                            print ("You do not have a Health potion.")
                            correct_input = False

                    elif user_in.lower() == "rage potion":
                        if inventory[2][1] >= 1:
                            base_attack += 1
                            health += -2
                            inventory[2][1] = inventory[2][1] - 1
                            correct_input = True
                        else:
                            print ("You do not have a Rage potion.")
                            correct_input = False
                    else:
                        correct_input = False
                        print ("Can't do that.")
                else:
                    correct_input = False


                # lower monster health values when attacked and also increase flame charges per turn and make it so that you are only hit on a valid input
                if monster_health >= 0 and correct_input == True:
                    if user_in == "defend":
                        health += (-1*(selected_monster[2]))/2
                    else:
                        health += -1*(selected_monster[2])
                    if selected_monster[3] == "Flame" or selected_monster[3] == "Nevermore":
                        flame_charge += 1
                if monster_health <= 0 and room_list[north_southpos][east_westpos] == room_list[2][4]:
                    game_over = input("Congratulations, you have beaten the game! Type anything to go to main menu. ")
                    if game_over != None:
                        main()
                    game_finish = True
                    fight = False

                elif monster_health <= 0:
                    print ("You have slain the",selected_monster[0]+".")
                    flame_charge = 0
                    drop_chance = random.randint(1,100)
                    if drop_chance <= 35:
                        inventory[random.randint(0,2)][1] += 1
                        print ("You have found some potions after defeating the",selected_monster[0]+".")
                    can_do = True
                    fight = False





    while done == True:
        if game_over != None:
            game = True
            done = False
            break
        chest = False

        #tells user which areas are blocked off.
        if north_southpos == 0:
            print ("There is a mysterious force preventing you from going north.")
        if east_westpos == 0:
            print ("There is a mysterious force preventing you from going west.")
        if north_southpos == 2:
            print ("There is a mysterious force preventing you from going south.")
        if east_westpos == 4:
            print ("There is a mysterious force preventing you from going east.")

        #print UI and also room data
        print (room_list[north_southpos][east_westpos])
        print ("Inventory:","   Mysterious Potion(s):",inventory[0][1],"  Health Potion(s):",inventory[1][1],"   Rage Potion(s):",inventory[2][1])
        print ("Your current health is:",health)
        print ("Your current base attack is:",base_attack)
        print ("You are equipped with a",equipped[0],"which adds an additional",equipped[1],"attack and has the special effect:",equipped[2])
        monster_chance()

        #tell user if there is a chest in the room
        for i in range(2):
            if room_grid[north_southpos][east_westpos] == chest_room[0][i]:
                print ("There is a chest open it?(yes or just ignore this) ")
            if room_grid[north_southpos][east_westpos] == chest_room[1][i]:
                print ("There is a chest open it?(yes or just ignore this) ")
            if room_grid[north_southpos][east_westpos] == chest_room[2][i]:
                print ("There is a chest open it?(yes or just ignore this) ")

        #tells user whether programs understands him/her and also if an area is impossible to access
        if can_do == False:
            print ("Can't do that.")
            can_do = True
        if can_go == False:
            print ("Can't go that way.")
            can_go = True

        if game_over != None:
            done = False
            break

        user_in = input("What would you like to do: ")

    #Check if there is a chest in the room and if there is prompt user with message
        for i in range(3):
            if room_grid[north_southpos][east_westpos] == chest_room[i][0]:
                if user_in.lower() == "yes":
                    chest = True
                    chest_room[i][0] = None
                    inventory[random.randint(0,2)][1] += 1
                    inventory[random.randint(0,2)][1] += 1
                    chance = random.sample([0,0,1,1,2,2,3,3,4,4,5,6,6],1)
                    random_drop = weapons[chance[0]]
                    text = "From the chest you found a: "+random_drop[0]+" and a couple of potions. Would you like to equip the "+random_drop[0]+"? (yes/else type in anything)(WARNING: equipping a new item will remove the currently equipped item.)"
                    user_ask_equip = input(text)
                    if user_ask_equip == "yes":
                        equipped = weapons[chance[0]]
                        chest = True


            if room_grid[north_southpos][east_westpos] == chest_room[i][1]:
                if user_in.lower() == "yes":
                    chest = True
                    chest_room[i][1] = None
                    inventory[random.randint(0,2)][1] += 1
                    inventory[random.randint(0,2)][1] += 1
                    chance = random.sample([0,0,1,1,2,2,3,3,4,4,5,6,6],1)
                    random_drop = weapons[chance[0]]
                    text = "From the chest you found a: "+random_drop[0]+" and a couple of potions. Would you like to equip the "+random_drop[0]+"? (yes/else type in anything)(WARNING: equipping a new item will remove the currently equipped item.)"
                    user_ask_equip = input(text)
                    if user_ask_equip == "yes":
                        equipped = weapons[chance[0]]
                        chest = True

        #make it possible for user to input north or n and make it not case sensistive
        if user_in.lower() == "n" or user_in.lower() == "north":
            if north_southpos == 0:
                can_do = True
                can_go = False
            else:
                north_southpos += -1
                can_do = True
        elif user_in.lower() == "e" or user_in.lower() == "east":
            if east_westpos == 4:
                can_go = False
                can_do = True
            else:
                east_westpos += 1
                can_do = True
        elif user_in.lower() == "s" or user_in.lower() == "south":
            if north_southpos == 2:
                can_go = False
                can_do = True
            else:
                north_southpos += 1
                can_do = True
        elif user_in.lower() == "w" or user_in.lower() == "west":
            if east_westpos == 0:
                can_go = False
                can_do = True
            else:
                east_westpos += -1
                can_do = True
        elif user_in.lower() != "n" and user_in.lower() != "e" and user_in.lower() != "s" and user_in.lower() != "w" and chest == False:
            potion()

        if game_finish == True:
            break


#welcome user to game and give instructions
while game == True:
    if done == False:
        print ("Welcome to Dungeon Souls! To move type in n/e/s/w or north/east/south/west. To drink potions you must type in the potion name. Your goal is to escape by reaching the final room and defeating the boss.")
        game_start = input ("Would you like to start the game (yes/quit)")
        if game_start.lower() == "yes":
            room_list = []
            game_start = None

            #randomize rooms every run except for room 1 and room 15 and also randomize where the chest rooms are.
            room_lay1 = ["You are in a forest. You find a cellar and you enter it. Behind you the entrance closes in on you, you must find another way out."]
            ran_roomlay1 = random.sample(["The walls are damp. you hear echoes in the distance.","The air begins to thin as you enter the room. Almost magically the room seems to appear before you.","The walls of this room seem to be ridden with war from another time.","Nothing interesting in this room."],4)
            for i in ran_roomlay1:
                room_lay1.append(i)
            room_lay2 = random.sample(["Suits of armours line the walls of the room. Best be weary in case it is not just decoration.","This is a library full of ancient books, but you have no time to read.","You enter a room which seems to be an armory, although there is nothing too useful here.","Nothing interesting in this room.","There is a note in this room. Its hard to make out what is written on it. It does not seem to be written in any language known by you."],5)
            room_lay3 = random.sample(["You hear a cry: Nevermore! NEVERMORE!!!","You are very close to the exit, but you feel as though there is something blocking your escape.","On the floor seems to be the remains of what seems to be a ritual of some sort.","You can feel an evil prescence consuming your soul."],4)
            room_lay3.append("There is only one final obstacle to your escape...")
            room_list.append(room_lay1)
            room_list.append(room_lay2)
            room_list.append(room_lay3)
            chest_room = []
            chest_room.append(random.sample([12,13,14,15],2))
            chest_room.append(random.sample([21,22,23,24,25],2))
            chest_room.append(random.sample([31,32,33,34],2))

            # start the game function.
            done = True
            game_over = None
            game = False
            main()

        elif game_start.lower() == "quit":
            break

