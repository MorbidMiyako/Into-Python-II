from room import RoomClass
from player import PlayerClass


# Declare all the rooms


room = {
    'outside':  RoomClass("Outside Cave Entrance",
                          "North of you, the cave mount beckons"),

    'foyer':    RoomClass("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': RoomClass("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   RoomClass("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': RoomClass("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

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


def printMessage():
    global player_move
    print(f"You are in {player_variable.room_name}")
    print("")
    print(room_variable.room_description)
    print("")
    print("Would you like to move north, east, south or west?")
    print("")
    player_move = input()
    print("")


room_variable = room["outside"]
player_variable = PlayerClass(room_variable.room_name)
print("The adventure game has started, enter q when you want to quit")
print("")
printMessage()

x = 1

while x > 0:

    if "q" == player_move:
        x = 0
    else:
        try:
            if "north" == player_move:
                print(f"You go {player_move}")
                print("")
                room_variable = room_variable.n_to
                player_variable = PlayerClass(room_variable.room_name)
                printMessage()
            elif "south" == player_move:
                print(f"You go {player_move}")
                print("")
                room_variable = room_variable.s_to
                player_variable = PlayerClass(room_variable.room_name)
                printMessage()
            elif "east" == player_move:
                print(f"You go {player_move}")
                print("")
                room_variable = room_variable.e_to
                player_variable = PlayerClass(room_variable.room_name)
                printMessage()
            elif "west" == player_move:
                print(f"You go {player_move}")
                print("")
                room_variable = room_variable.w_to
                player_variable = PlayerClass(room_variable.room_name)
                printMessage()
            else:
                print(
                    "Directions can only be indicated as 'north', 'east', 'south' and 'west'")
                print("")
                printMessage()
        except:
            print("You can't go that way")
            print("")
            printMessage()

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
