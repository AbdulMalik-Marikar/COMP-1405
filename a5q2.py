
# Dictionary

my_dict = {}
file = open('your-assigned-glyphs.dat')
my_glyphs = file.read()
file.close()

my_glyphs = my_glyphs.strip(":")
my_glyphs = my_glyphs.strip("%")
my_glyphs = my_glyphs.split("&")

for x in range(len(my_glyphs)-1):
    my_dict[my_glyphs[x][0]] = my_glyphs[x][2:]


# Defining functions:

def myInsert(my_dict, key, value):

    if key.upper() in my_dict:    # If it exists
        return False
    else:
        my_dict[key.upper()] = value
        return True


def myReplace(my_dict, key, value): # For this function, I am assuming that I will be returning a boolean.

    if key.upper() in my_dict:        # If it exists
        del my_dict[key.upper()]
        my_dict[key.upper()] = value
        return True
        
    else:
        return False


def myTranslate(my_dict, trnslt):  
        trnslt = trnslt.upper()
        trnslt = trnslt.split(",")
        
        new_list = []
        # Looping through each character in list:
        for i in range(len(trnslt)):
            if trnslt[i] in my_dict:
                new_list += [my_dict[trnslt[i]]]
        
        return new_list


# Menu:

print("\n\nPlease select your option below:")
print("\n\n  a) quit \n  b) translate \n  c) insert \n  d) replace")

choice = input("\n\n        Enter your selection here: ")

no_crash = 0
while no_crash == 0:
    
    if choice.lower() == "a":
        print('\n\nYou chose "quit".')
        quit()

    elif choice.lower() == "b":
        print('\n\nYou chose "translate".')
        trnslt = input("\n\nPlease enter a string to be translated (with commas in between).\n\n--> ")
        print(myTranslate(my_dict, trnslt))
        no_crash = 1
        
       
    elif choice.lower() == "c":
        print('\n\nYou chose "insert".')
        key = input("\n\nPlease enter a key to assign a value to: ")
        value = input("\nPlease enter a value for the key: ")
        print(myInsert(my_dict, key, value))
        no_crash = 1
        
        

    elif choice.lower() == "d":
        print('\n\nYou chose "replace".')
        key = input("\n\nPlease enter a key to assign a value to: ")
        value = input("\nPlease enter a value for the key: ")
        print(myReplace(my_dict, key, value))
        no_crash = 1
        
        
    else:
        print("\n\nThis is not a valid option. Try again.")
        no_crash = 0

    
        
    







