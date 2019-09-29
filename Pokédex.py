# ----------------------------------------------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 3: Pokedex
# Jacob Weikert
# Last Modified: October 11, 2017
# ----------------------------------------------------------------------------
# This program displays a menu for the user. Based on user input,specific
# pokemon details are obtained.
# ----------------------------------------------------------------------------
# HONORS LAB ENHANCEMENT: POKEMON SELFIES
#
#   If option "2" from the menu display is chosen. Then an .jpg file of that
#   pokemon will appear in your python directory, where it can be accessed.
#   Once you open this file, you will see a selfie of a friendly pokemon.
#
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

import string
import urllib.request

# Reads the file "poke_selfie.txt" written, and sends it into a "pic_list".
# def rpokemon_pics():
#     pic_list = []
#     file = open('poke_selfie.txt', 'r')
#     for line in file:
#         value = line.split('\n')
#         pic_list.append(value)
#     file.close()
#     return pic_list

# Saves a specific "name".jpg file into your python directory.    
# def download_web_image(url, name):
#     full_name = str(name) + '.jpg'
#     urllib.request.urlretrieve(url, full_name)

# Prints the menu options available to user.
def printMenu():
    print('1. Print Pokedex')
    print('2. Lookup Pokemon by Name')
    print('3. Lookup Pokemon by Number')
    print('4. Print Number of Pokemon')
    print('5. Print Total Hit Points of All Pokemon')
    print('6. Quit')
    print()

# If option 1 is chosen, the description of the pokemon (including name) is printed.
def printPokedex(pokedex):
    print()
    print('The Pokedex')
    print('-----------')
    for idx in pokedex:
        pokemon = pokedex[idx][0]
        hp = pokedex[idx][1]
        if len(pokedex[idx]) > 3:
            types = pokedex[idx][2] + ' and ' + pokedex[idx][3]
        else:
            types = pokedex[idx][2]
        print('Number: ' + str(idx) + ', Name: ' + str(pokemon) + ', HP: ' + str(hp) + ', Type: ' + str(types))
        print('-----------')
    print('End Pokedex\n\n')
#-----------------------------------------------------------------------------------------------------------------------
# HONORS LAB ENHANCEMENT TO THIS OPTION
# Can look up pokemon by name, retrieve the details of pokemon

def lookupByName(pokedex, name):
    new_dic = {}
#     pic_list = rpokemon_pics() # Return the "pic_list" made in the read file to the value of "pic_list"
    pokes = list(pokedex.values()) 
    list_of_poke = []
    pokeFlag = False
    
    for ele in pokes: # Throws pokedex values into a list
        list_of_poke.append(ele[0])
    for i in range(0, 29): # Can create pictures of the 30 pokemon listed in Paxtons "in" file.
        new_dic[list_of_poke[i]] = str(pic_list[i][0]) #Throws key-value pairs of pokemon-URL's into "new_dic".
    for idx in pokedex: # Finds pokemon the user desires, and returns statistics and a selfie of pokemon
        pokemon = pokedex[idx][0]
        if pokemon == name:
#             for akey in new_dic.keys(): # Makes a picture (.jpg file) for the pokemon chosen.
#                 if akey == pokemon:
#                     download_web_image(new_dic[akey], name)
            pokemon = pokedex[idx][0]
            hp = pokedex[idx][1]
            if len(pokedex[idx]) > 3:
                types = pokedex[idx][2] + ' and ' + pokedex[idx][3]
            else:
                types = pokedex[idx][2]
            print('Number: ' + str(idx) + ', Name: ' + str(pokemon) + ', HP: ' + str(hp) + ', Type: ' + str(types))
            pokeFlag = True
            
    if pokeFlag == False:
        print("The pokemon named " + name + ' does not exist')
    print()
#-----------------------------------------------------------------------------------------------------------------------   
# Look up description of pokemon based on the inputed number.
def lookupByNumber(pokedex, number):
    pokeFlag = False
    for idx in range(1, len(pokedex) + 1):
        if idx == number:
            pokemon = pokedex[idx][0]
            hp = pokedex[idx][1]
            if len(pokedex[idx]) > 3:
                types = pokedex[idx][2] + ' and ' + pokedex[idx][3]
                pokeFlag = True
            else:
                types = pokedex[idx][2]
                pokeFlag = True
            print('Number: ' + str(idx) + ', Name: ' + str(pokemon) + ', HP: ' + str(hp) + ', Type: ' + str(types))
    if pokeFlag == False:
        print('Error: Pokemon number ' + str(number) + ' does not exist')
    print()

# Find out how many pokemon are in the pokedex dictionary provided.
def howManyPokemon(pokedex):
    print('There are ' + str(len(pokedex)) + ' different Pokemon')
    print()

# Find out total hitpoints of ALL pokemon listed in the pokedex dictionary. 
def howManyHitPoints(pokedex):
    total_hp = 0
    for idx in pokedex:
        total_hp += pokedex[idx][1]
    print('The total number of hit points for all pokemon is ' + str(total_hp))
    print()
                    
    
# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def createPokedex(filename):
    pokedex = {}
    file = open(filename, "r")
    
    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        index = int(pokelist.pop(0))
        pokedex[index] = [pokelist.pop(0)]          # name
        pokedex[index] += [int(pokelist.pop(0))]    # hit points
        pokedex[index] += [pokelist.pop(0)]         # type
        if len(pokelist) == 1:
            pokedex[index] += [pokelist.pop(0)]     # optional second type

    file.close()
    return pokedex

# ---------------------------------------

def getChoice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    pokedex = createPokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        printMenu()
        choice = getChoice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            printPokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ")
            name = name.capitalize()
            lookupByName(pokedex, name)
        elif choice == 3:
            number = getChoice(1, 1000, "Enter a Pokemon number: ")
            lookupByNumber(pokedex, number)
        elif choice == 4:
            howManyPokemon(pokedex)
        elif choice == 5:
            howManyHitPoints(pokedex)
    print("Thank you.  Goodbye!")

# ---------------------------------------

main()
