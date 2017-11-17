

my_dict = {}
file = open('your-assigned-glyphs.dat')
my_glyphs = file.read()
file.close()

my_glyphs = my_glyphs.strip(":")
my_glyphs = my_glyphs.strip("%")
my_glyphs = my_glyphs.split("&")

for x in range(len(my_glyphs)-1):
    my_dict[my_glyphs[x][0]] = my_glyphs[x][2:]



print(my_dict)

# Defining functions:

def myInsert(my_dict, key, value):

    if my_dict[key]:    # If it exists
        return False
    else:
        my_dict[key] = value
        return True


def myReplace(my_dict, key, value): # For this function, I am assuming that I will be returning a boolean.

    if my_dict[key] == False:   # If it doesn't exist
        return False
    else:
        del my_dict[key]
        my_dict[key] = value
        return True


# Menu:

print("\n\nPlease select your option below:")
print("\n\n  a) quit \n  b) translate \n  c) insert \n  d) replace")

choice = input("\n\n        Enter your selection here: ")

no_crash = 1
while no_crash == 1:
    
    if choice.lower() == "a":
        print('\n\nYou chose "quit".')
        quit()

    elif choice.lower() == "b":
        print('\n\nYou chose "translate".')
        trnslt = input("\n\nPlease enter a string to be translated (with commas in between).\n\n--> ")
        trnslt = trnslt.upper()
        
        # Looping through each character in string:
        for i in range(len(trnslt)):
            if trnslt[i] in my_dict:
                trnslt = my_dict[trnslt[i]]
        print(trnslt)
    
        no_crash = 0
    
       

        

    elif choice.lower() == "c":
        print('\n\nYou chose "insert".')
        key = input("\n\nPlease enter a key to assign a value to: ")
        value = input("\nPlease enter a value for the key: ")
        myInsert(key, value)
        no_crash = 0
        

    elif choice.lower() == "d":
        print('\n\nYou chose "replace".')
        key = input("\n\nPlease enter a key to assign a value to: ")
        value = input("\nPlease enter a value for the key: ")
        myReplace(key, value)
        no_crash = 0
        

    else:
        print("\n\nThis is not a valid option. Try again.")
        no_crash = 1





