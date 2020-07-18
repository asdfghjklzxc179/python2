from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
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
player = Player(input(" Enter your name "), room['outside'])
print(f'Hello, {player.name}')

# Make a new player object that is currently in the 'outside' room.
# Write a loop that:

while(player.name):
    # * Prints the current room name
    print(f'{player.name} you are in {player.in_room.name}')
# * Prints the current description (the textwrap module might be useful here).
    print(player.in_room.description)
# * Waits for user input and decides what to do.
    gowhere = input(
        "Where do you want to go? (enter N, W, S, E or Q to quit)")

# If the user enters a cardinal direction, attempt to move to the room there.
    if gowhere == 'N' or 'n':
        player.in_room.name = player.in_room.name.n_to
    elif gowhere == 'W' or 'w':
        player.in_room.name = player.in_room.name.room.w_to
    elif gowhere == 'S' or 's':
        player.in_room.name = player.in_room.name.room.s_to
    elif gowhere == 'E' or 'e':
        player.in_room.name = player.in_room.name.room.e_to
        # If the user enters "q", quit the game.
    elif gowhere == 'Q' or 'q':
        print("See ya")
        break
        # Print an error message if the movement isn't allowed.
    else:
        print("The direction you chose does not exist")
