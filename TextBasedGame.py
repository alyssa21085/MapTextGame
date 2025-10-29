#Project 1 Text based Game
#Alyssa Boyce

def display_game():
    game_intro = r"""
 __        ___ _       _       _   _             _  
 \ \      / (_) |_ ___| |__   | | | |_   _ _ __ | |_
  \ \ /\ / /| | __/ __| '_ \  | |_| | | | | '_ \| __|
   \ V  V / | | || (__| | | | |  _  | |_| | | | | |_
    \_/\_/  |_|\__\___|_| |_| |_| |_|\__,_|_| |_|\__|

        """

    print(game_intro)

def instructions():
    #Printing main menu and commands
    print("""******************************************************************************************
You have been dropped in the castle and must collect the items needed to defeat the Witch!
Collect 10 items total then find the witch to fight her!
But be careful! If you run into the witch before collecting all items it wont end well!
Move commands: go North, go South, go East, go West
Add to inventory: get \'item name\'
******************************************************************************************""")
    return

#FUNCTION to get status of each room, item in room and where able to move
def status(currentRoom, inventory):
    print('***********************************************')
    print('You are in the', currentRoom)
    print('Inventory: [', ', '.join(inventory), ']')
    return

#FUNCTION for Player movement
def player_move(currentRoom, direction):
    print('Which way would you like to go?')
    direction = input()
    print('***********************************************')


    #NORTH MOVEMENT
    if direction == 'go North':
        direction = direction[3:]
        if direction in rooms[currentRoom]:
            print('You go through the northern door.')
            currentRoom = rooms[currentRoom][direction]
            print('You entered the', currentRoom)
            print('***************************************************')
        else:
            print('You ran into a wall, try another direction.')
            print('***************************************************')

    #EAST MOVEMENT
    elif direction == 'go East':
        direction = direction[3:]
        if direction in rooms[currentRoom]:
            print('You go through the eastern door.')
            currentRoom = rooms[currentRoom][direction]
            print('You entered the', currentRoom)
            print('***************************************************')
        else:
            print('You ran into a wall, try another direction.')
            print('***************************************************')

    #SOUTH MOVEMENT
    elif direction == 'go South':
        direction = direction[3:]
        if direction in rooms[currentRoom]:
            print('You go through the southern door.')
            currentRoom = rooms[currentRoom][direction]
            print('You entered the', currentRoom)
            print('***************************************************')
        else:
            print('You ran into a wall, try another direction.')
            print('***************************************************')

    #WEST Movement
    elif direction == 'go West':
        direction = direction[3:]
        if direction in rooms[currentRoom]:
            print('You go through the western door.')
            currentRoom = rooms[currentRoom][direction]
            print('You entered the', currentRoom)
            print('***************************************************')
        else:
            print('You ran into a wall, try another direction.')
            print('***************************************************')

    #IF Data is not entered CORRECTLY
    else:
        print('You tripped and fell, try again.')
        print('You recall a distant past memory.')
        print('Move commands: go North, go South, go East, go West')
        print('***************************************************')

    return currentRoom

#FUNCTION to find item in current room
def find_item(currentRoom):
    print('**************************************************')
    print('You look around the', currentRoom,'.')
    if currentRoom == 'Great Hall':
        print('You search around the room and find nothing.')
        print('**************************************************')

    elif rooms[currentRoom]['item'] != ' ':
        #Check to see if Item is picked up
        if rooms[currentRoom]['item'] in inventory:
            print('It seems like you have already searched this room.')
            print('**************************************************')
        else:
            #Search room for item
            item = rooms[currentRoom]['item']
            print('You search around the room and find a', rooms[currentRoom]['item'])
            item = rooms[currentRoom]['item']

            print('Would you like to pick up the item?')
            getItem = input()
            item = 'get ' + item

            if getItem == item:
                #Check to see if item in inventory previously
                if rooms[currentRoom]['item'] in inventory:
                    print('It seems like you have already searched this room')

                else:
                    #PICK UP ITEM
                    print('The item is added to your inventory.')
                    inventory.append(item[4:])

                    #Plural VS Singular item list
                    if len(inventory) == 1:
                        print('You now have', (len(inventory)), 'item.' )
                        print('**************************************************')

                    elif len(inventory) > 1:
                        print('You now have', (len(inventory)), 'items.')
                        print('**************************************************')

            else:
                print('You did not pick up', item)

    return







#Room set up
rooms = {'Great Hall': {'North': 'Den',
                         'item': ' '},
                'Den': {'North': 'Basement',
                        'South': 'Great Hall',
                         'West': 'Throne Room',
                         'item': 'Parcel from the King'},
           'Basement': {'North': 'Gardens',
                        'South': 'Den',
                         'East': 'Library',
                         'item': 'Portal'},
            'Library': {'North': 'Clock Tower',
                         'West': 'Basement',
                         'item': 'Spell Book'},
        'Clock Tower': {'South': 'Library',
                         'West': 'Gardens',
                         'item': 'Siphon'},
            'Gardens': {'South': 'Basement',
                         'East': 'Clock Tower',
                         'West': 'Bathing Chambers',
                         'item': 'Amulet'},
        'Throne Room': {'North': 'Kings Quarters',
                         'East': 'Den',
                         'West': 'Dining Hall',
                         'item': 'Prince'},
     'Kings Quarters': {'South': 'Thone Room',
                         'item': 'Witch'},
              'Patio': {'North': 'Dining Hall',
                         'item': 'Sword'},
        'Dining Hall': {'North': 'Butlers Quarters',
                         'East': 'Throne Room',
                        'South': 'Patio',
                         'item': 'Daggers'},
   'Butlers Quarters': {'North': 'Bathing Chambers',
                        'South': 'Dining Hall',
                         'item': 'Shield'},
   'Bathing Chambers': {'South': 'Butlers Quarters',
                         'East': 'Gardens',
                         'item': 'Obsidian Mirror'}

}

#Dictionary for aquired inventory
inventory = []

#Players starting position and directions function
currentRoom = 'Great Hall'
direction = ' '
display_game()
instructions()

while True:
    status(currentRoom,inventory)


    #Exit loop if throne room is entered before all items collected
    #GAME OVER
    if currentRoom == 'Kings Quarters' and len(inventory) != 10:
        print('***************************************************')
        print('You ran into the Witch before collecting all items!')
        print('GAME OVER!')
        print('***************************************************')
        quit()


    find_item(currentRoom)

    # Exit loop if all items are found
    # WINNER
    if len(inventory) == 10:
        print('*****************************************************')
        print('You have collected all the items!')
        print('You wander around the castle once more in search for')
        print('the Witch, you find her in the King\'s Quarters and')
        print('use your items to defeat her. The kingdom is SAFE!')
        print('Congrats! You WON!')
        print('*****************************************************')
        quit()

    currentRoom = player_move(currentRoom, direction)


