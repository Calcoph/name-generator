from random import randint

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # letter list
vowel = ["a", "e", "i", "o", "u"] # vowel list
consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l",
"m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"] # consonant list

def multiple_names(x):
    if x.isdigit():
        for n in range(int(x)):
            print
            print str(n + 1) + ". " + name_gen() # generates x amount of names
    else:
        print "input is not valid"

def vowel_gen(): # generates a random vowel
    num = randint(0, 4)
    return vowel[num]
def letter_gen(): # generates a random letter
    num = randint(0, 25)
    return abc[num]

def name_gen(): #the name generator
    pene = randint(5, 9)
    name = ""
    lastl = "nada"
    for n in range(pene):
        letter = letter_gen()
        if lastl == "nada": # starts the word
            name = name + letter.upper()
        else: # check what was the last letter
            if lastl in vowel:
                name = name + letter
            elif lastl in consonant:
                letter = vowel_gen()
                name = name+letter
            else: # for bug detection
                print "error"

        lastl = letter
    return name

on = True
while on == True:
    input1 = raw_input("What would you like to do? ")
    if input1 == "generate":
        multiple_names(raw_input("How many names would you like to generate?" ))
    elif input1 == "help":
        print "all available commands are: help, generate, exit"
    elif input1 == "exit":
        on = False
    else:
        print "input is not valid"
