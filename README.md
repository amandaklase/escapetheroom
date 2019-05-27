# Escape the Room

text based escape the room game

## Hackbright Prep Project

### This program will allow a user to play a text-based adventure game where the object is to search rooms for resources and to make a series of decisions on how to use those resources to escape those rooms

### winning condition will be if the player makes the correct decisions that will lead to the exit of the room

### losing condition will be making an incorrect decision which leads to death

* print the game title
* create a list of player inventory
* ask user for their player name
* print an opening paragraph using the player's name to explain the situation they find themselves in and what they must do to move on.
* print a description of what the character sees
  * Ask if the character would like to examine something closer.
    * if they want to search closer, ask which object they want to look closer at
    * depending on the item, describe it and give a hint as to whether it can be lifted, or moved, etc. and then ask the user what they would like to do, including use inventory item
      * if they choose further search
        * if the further search reveals a usuable object, automatically add it to player inventory
        * if it reveals mini game, play mini game
        * if nothing of interest is revealed, say so
        * in all cases, remember that they've done this
        * print message about the inventory
        * ask if they want to take a closer look at something else:
          * if yes, repeat, if no, quit loop
      * if access inventory, allow user input of which inventory item they would like to access
        * if item is capable of working on object, say so and add new combined inventory item or reveal mini game
        * if it isn't, say so and exit back to allow them to try another inventory item or exit.
      * if they choose exit, break looping, pulling them back out one level to the direction and list objects again.

#### Extras if I have time

* Move to next room, which is a hallway. Describe the hallway and start searches again
* another change is that an option will be to talk to people, and we want a way for those people to ask the character to find something for them or to solve a mini game and if they do to reward them with soemthign. we will have to have the program remember if they have already talked to them and change their script accordingly.