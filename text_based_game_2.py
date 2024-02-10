hp = 100
attack = 10
lizard = 10
sword = 25
axe = 90
goblin = 100
monster_king = 250
armour = 50
pickaxe = False
key = False

print('Welcome to the dungeon, what is this challengers name?: ')
name = input('Enter your name: ')

def start_game():
    global name
    print(f'Welcome {name}, you have entered the dungeon.')
    action = input('You have come up to a big door, what do you do? ')
    if action == 'I walk up and open the door':
        print(f'Well done {name}. The door opens slowly, you notice how heavy it is...')
        print('You have entered the room first room.')
        print('You notice a small candle in the centre of the room, the walls and floor are cobblestone.')
        print('You have a door infront of you, some moss to the left and some cracks on the right wall.')
        first_room()
    else:
        action


def first_room():
    action = input('What do you do? ')
    if action == 'I open the door':
        print('You open the door to the next room')
        print('The door locks behind you')
        print('You encounter a goblin!')
        fight2()
    elif action == 'I check the moss on the walls':
        action2 = input('You have revelead a secret room, would you like to go in? Y / N  ')
        if action2 == 'Y':
            print('You have entered a hidden room')
            hidden1()
        elif action2 == 'N':
            print('You are back at the first room')
            print('You notice a chest at the end of the room')
            first_room()
    elif action == 'I check the cracks':
        global pickaxe
        if pickaxe == True:
            print('You have found another hidden room')
            hidden2()
        else:
            print('You cannot break this wall with your strength.')
            print('You are still in the first room.')
            first_room()

def hidden1():
     action = input('What do you do? ')
     if action == 'I go to open the chest':
         print('A lizard hops out')
         fight1()

def fight1():
    action = input('Attack the monster!')
    global lizard
    global pickaxe
    global attack
    if action == 'hit':
        print('You have hit the lizard.')
        lizard = lizard - attack
        if lizard <= 0:
            print('The monster has been slain!')
            print('You find a pickaxe in the corner of the room')
            pickaxe = True
            chest()

def chest():
    global armour
    global hp
    print('You have reached the chest.')
    action = input('What do you do?')
    if action == 'Open chest':
        print('The chest contained some armour!')
        print('You equip the new armour')
        hp = hp + armour
        first_room()

def hidden2():
    global sword
    global attack
    print('Stones fly off the walls!')
    print('A room is seen behind the cracks and a chest is revealed!')
    print('You open the chest and see it contains a sword!')
    print('You equip the sword and start to feel stronger already')
    attack = attack + sword
    print('You return to the first room')
    first_room()

def fight2():
    global hp
    global key
    global attack
    global goblin
    quest = input('Do you fight or run?')
    if quest == 'fight':
        action = input('Hit the goblin!')
        if action == 'hit':
            goblin - attack
            hp - 5
        elif goblin <= 0:
            print('You have defeated the monster!')
            hp = 150
            print('A key was dropped.')
            key = True
            print('On the room number 2...')
            second_room()
        elif hp <= 0:
            ask = input('You have died. Try again. Y / N  ')
            if ask == 'Y':
                start_game()
            elif ask == 'N':
                end_game_loss()
    elif quest == 'run':
        print('You safely escaped.')
        second_room()

def second_room():
    global attack
    global axe
    global sword
    print('You come to the end of the hallway and enter a second room')
    print('The door behind you locks again')
    print('You notice a chest with a lock on it to the left.')
    print('At the end of the room is a big door twice the size as the others.')
    quest = input('What do you do?')
    if quest == 'check chest':
        print('The lock looks similar to the key dropped!')
        action = input('Use key? Y / N  ')
        if action == 'Y':
            print('The lock opens!!!')
            print('You find an axe inside')
            print('You equip the axe!')
            attack = attack - sword + axe
            quest
        elif action == 'N':
            quest
    if quest == 'i open the door':
        print('You struggle to push open the door')
        print('Candles start to light up around the room in a purple hue')
        print('You have encountered the monster king.')
        fight3()

def fight3():
    global hp
    global monster_king
    global attack
    global name
    print('The monster is fast and gets the first attack')
    hp - 50
    action = input('Hit the monster!')
    if action == 'hit':
        monster_king - attack
        hp - 25
        if monster_king <= 0:
            print('The final boss has been defeated!')
            print('Congratulations!!!')
            print(f'{name} has finished the dungeon!!!')
            end_game_win()
        elif hp <= 0:
            print()

def end_game_win():
    global name
    print(f'Thank you for playing {name}.')

def end_game_loss():
    global name
    print(f'Unlucky {name}, thank you for playing.')


start_game()