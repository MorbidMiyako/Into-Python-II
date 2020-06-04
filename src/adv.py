from room import RoomClass
from player import PlayerClass
from item import ItemClass


# Declare all the rooms

item = {
    'key': ItemClass("key", "unlocks the treasure"),
    'sword': ItemClass("sword", "protects you if needed"),
    'treasure': ItemClass("treasure", "who knows what it hides, maybe you if you find and use the key")
}

room = {
    'outside':  RoomClass("Outside Cave Entrance",
                          "North of you, the cave mount beckons", item['sword']),

    'foyer':    RoomClass("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': RoomClass("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item['key']),

    'narrow':   RoomClass("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': RoomClass("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", item['treasure']),
}


# Link rooms together

room['outside'].connections["north"] = room['foyer']
room['foyer'].connections["south"] = room['outside']
room['foyer'].connections["north"] = room['overlook']
room['foyer'].connections["east"] = room['narrow']
room['overlook'].connections["south"] = room['foyer']
room['narrow'].connections["west"] = room['foyer']
room['narrow'].connections["north"] = room['treasure']
room['treasure'].connections["ssouth"] = room['narrow']


def printRoomMessage():
    print(f"{player_variable.player_name} enters {player_variable.current_room.room_name}")
    print("")
    print(player_variable.current_room.room_description)
    print("")
    #


def printNextPlayerMove():
    global player_move
    print(f"What is {player_variable.player_name}'s next move?")
    print("")
    player_move = input().split(" ")
    print("")
    if len(player_move) == 2:
        try:
            player_move[1] = item[player_move[1]]
        except:
            print(player_move[1])


def printControls():
    print(f"{player_variable.player_name} has the following moves at his disposal:")
    print("'c' or 'controls' to list the controls")
    print("'q' or 'quit' to quit the game")
    print("'s' or 'search' to search the current room")
    print("'i' or 'inventory' to search his inventory")
    print("'north', 'east', 'south' and 'west' to move in their respective directions")
    print("'take (item)' to take an item from a room")
    print(
        f"'drop (item)' to drop an item from {player_variable.player_name}'s inventory")
    print(
        f"'use (item)' to use an item from {player_variable.player_name}'s inventory")


room_variable = room["outside"]
print("The adventure game has started")
print("")
print("What will be your name?")
print("")
player_name = input()
player_variable = PlayerClass(room_variable, player_name)
print("")
printControls()
print("")
printRoomMessage()

while player_variable.is_playing:
    printNextPlayerMove()
    if len(player_move) == 1:
        if player_move[0] in ["north", "east", "south", "west"]:
            if player_variable.current_room.connections[player_move[0]] is not None:
                player_variable.move(player_move[0])
                printRoomMessage()
        elif player_move[0] in ["q", "quit"]:
            print("Thanks for playing!")
            player_variable.is_playing = False
        elif player_move[0] in ["i", "inventory"]:
            player_variable.searchInventory()
        elif player_move[0] in ["s", "search"]:
            player_variable.current_room.searchRoom(
                player_variable.player_name)
        elif player_move[0] in ["c", "controls"]:
            printControls()
        else:
            print(
                f"{player_variable.player_name} is confused, he doesnt understand what to do")
            print("For a list of controls, use 'c' or 'controls'")
    elif len(player_move) == 2:
        if player_move[0] in ["drop", "take"]:
            player_variable.changeInventory(player_move)
        elif player_move[0] in ["use"]:
            player_variable.useItem(player_move, item['treasure'])
    player_variable.amount_of_moves += 1


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


"""
def printRoomMessage():
    global player_move
    print(f"{player_variable.player_name} enters {player_variable.current_room}")
    print("")
    print(room_variable.room_description)
    print("")
    print("Would you like to move north, east, south or west?")
    print("")
    player_move = input().split(" ")
    print("")


room_variable = room["outside"]
print("The adventure game has started, enter q when you want to quit")
print("")
print("What will be your name?")
print("")
player_name = input()
player_variable = PlayerClass(room_variable.room_name, player_name)
print("")
printRoomMessage()

x = 1

while x > 0:

    if len(player_move) == 1:
        if "q" == player_move[0]:
            x = 0
        elif "i" == player_move[0]:
            print(
                f"{player_variable.player_name} looks trough his inventory. He finds {player_variable.player_inventory}")
            print("")
            printRoomMessage()
        else:
            try:
                if "north" == player_move[0]:
                    print(f"You go {player_move[0]}")
                    print("")
                    room_variable = room_variable.n_to
                    player_variable.current_room = room_variable.room_description
                    printRoomMessage()
                elif "south" == player_move[0]:
                    print(f"You go {player_move[0]}")
                    print("")
                    room_variable = room_variable.s_to
                    player_variable.current_room = room_variable.room_description
                    printRoomMessage()
                elif "east" == player_move[0]:
                    print(f"You go {player_move[0]}")
                    print("")
                    room_variable = room_variable.e_to
                    player_variable.current_room = room_variable.room_description
                    printRoomMessage()
                elif "west" == player_move[0]:
                    print(f"You go {player_move[0]}")
                    print("")
                    room_variable = room_variable.w_to
                    player_variable.current_room = room_variable.room_description
                    printRoomMessage()
                else:
                    print(
                        "Directions can only be indicated as 'north', 'east', 'south' and 'west'")
                    print("")
            except:
                print("You can't go that way")
                print("")
    elif len(player_move) == 2:
        if player_move[0] == "take":
            if player_move[1] == "key"


"""
"""
second day ideas:


"""

"""
player_variable = PlayerClass("outside")
room_variable = RoomClass(room["outside"])
print("game is starting, enter q when you want to quit")

x = 1

loop:
while x > 0:

    print(player_variable.room)
    print(room_variable.room_description)
    player_move = input("would you like to move north, east, south or west?)

    if "q" is entered
        x = 0
    else:
        try:
            if "north" is entered:
                player_variable = PlayerClass(room[player_variable.room].n_to)
                room_variable = RoomClass(room[player_variable.room])
            elif "south" is entered:
                player_variable = PlayerClass(room[player_variable.room].s_to)
                room_variable = RoomClass(room[player_variable.room])
            elif "east" is entered:
                player_variable = PlayerClass(room[player_variable.room].e_to)
                room_variable = RoomClass(room[player_variable.room])
            elif "west" is entered:
                player_variable = PlayerClass(room[player_variable.room].w_to)
                room_variable = RoomClass(room[player_variable.room])
            else:
                print(warning that only following directions are possible)
        except:
            print(warning that direction is not possible)

player:

class PlayerClass():
    def __init__(self, room):
        self.room = room

room:

class RoomClass():
    def __init__(self, room_description) #this could be a super of player?
        self.room_description = room_description

second iteration:

            if "north" is entered:
                room_variable = room[room_variable.room_name].n_to
                player_variable = PlayerClass(room_variable.room_name)
            elif "south" is entered:
                room_variable = room[room_variable.room_name].s_to
                player_variable = PlayerClass(room_variable.room_name)
            elif "east" is entered:
                room_variable = room[room_variable.room_name].e_to
                player_variable = PlayerClass(room_variable.room_name)
            elif "west" is entered:
                room_variable = room[room_variable.room_name].w_to
                player_variable = PlayerClass(room_variable.room_name)
            else:
                print(warning that only following directions are possible)
        except:
            print(warning that direction is not possible)

player:

class PlayerClass():    #this could be a super of player?
    def __init__(self, room_name):
        self.room = room_name

room:

class RoomClass():
    def __init__(self,room_name, room_description)
        self.room_name = room_name
        self.room_description = room_description

first working iteration:

room_variable = room["outside"]
player_variable = PlayerClass(room_variable.room_name)
print("game is starting, enter q when you want to quit")
print("")
print(player_variable.room_name)
print("")
print(room_variable.room_description)
print("")
print("would you like to move north, east, south or west?")
print("")
player_move = input()
print("")

x = 1

while x > 0:

    if "q" == player_move:
        x = 0
    else:
        try:
            if "north" == player_move:
                print(f"you go {player_move}")
                print("")
                room_variable = room_variable.n_to
                player_variable = PlayerClass(room_variable.room_name)
                print(player_variable.room_name)
                print("")
                print(room_variable.room_description)
                print("")
                print("would you like to move north, east, south or west?")
                print("")
                player_move = input()
                print("")
            elif "south" == player_move:
                print(f"you go {player_move}")
                print("")
                room_variable = room_variable.s_to
                player_variable = PlayerClass(room_variable.room_name)
                print(player_variable.room_name)
                print("")
                print(room_variable.room_description)
                print("")
                print("would you like to move north, east, south or west?")
                print("")
                player_move = input()
                print("")
            elif "east" == player_move:
                print(f"you go {player_move}")
                print("")
                room_variable = room_variable.e_to
                player_variable = PlayerClass(room_variable.room_name)
                print(player_variable.room_name)
                print("")
                print(room_variable.room_description)
                print("")
                print("would you like to move north, east, south or west?")
                print("")
                player_move = input()
                print("")
            elif "west" == player_move:
                print(f"you go {player_move}")
                print("")
                room_variable = room_variable.w_to
                player_variable = PlayerClass(room_variable.room_name)
                print(player_variable.room_name)
                print("")
                print(room_variable.room_description)
                print("")
                print("would you like to move north, east, south or west?")
                print("")
                player_move = input()
                print("")
            else:
                print("you can't go that way")
                print("")
                print("would you like to move north, east, south or west?")
                print("")
                player_move = input()
                print("")
        except:
            print(
                "directions can only be indicated as 'north', 'east', 'south' and 'west'")
            print("")
            print("would you like to move north, east, south or west?")
            print("")
            player_move = input()
            print("")



"""
