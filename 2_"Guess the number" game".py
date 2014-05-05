# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

"""import some modules"""
import random, simplegui

# initialize global variables used in your code
secret_number = random.randrange(0, 100)
secret_number_range = 100
number_allowed_guess = 0

# helper function to start and restart the game
def new_game():
    """ This fonction is to start new game, and print out some introductions. """
    global secret_number, number_allowed_guess
    print
    print "=== A new game start ==="    
    if secret_number_range == 100:      
        number_allowed_guess = 7
        secret_number = random.randrange(0, 100)
    else:
        number_allowed_guess = 10
        secret_number = random.randrange(0, 1000)
    print "Range: [0, " + str(secret_number_range) + ")"
    print
    
# define event handlers for control panel
def range100():
    """ This function is to get a secret number in the range of [0, 100) """
    global secret_number, secret_number_range
    secret_number = random.randrange(0, 100)
    secret_number_range = 100
    new_game()
    

def range1000():
    """ This function is to get a secret number in the range of [0, 1000) """
    global secret_number, secret_number_range
    secret_number = random.randrange(0, 1000)
    secret_number_range = 1000
    new_game()
    
    
def input_guess(guess):
    """ This function is to deal with the number that player entered. """
    global number_allowed_guess
    # Using a try-except to catch wrong input
    try:
        guess = int(guess)       
        end = False
        print "Your guess number is: " + str(guess)
        if guess > secret_number:
            print "Lower"
        elif guess < secret_number:
            print "Higher"
        else:
            print "Correct!"
            end = True
        number_allowed_guess -= 1         
        if end == True:
            print "You win!"
            print
            new_game()
        elif end == False and number_allowed_guess == 0:
            print "You lose!"
            print
            new_game()
        else:            
            print "You remain " + str(number_allowed_guess) + " times to guess."
            print
    except Exception as e:
        print "Error:"
        print "Something wrong with the number you've entered,"
        print "please to enter an integer."
        print
         
    
# create frame
frame = simplegui.create_frame('Guess the number', 200, 400)

# register event handlers for control elements
frame.add_button('Range: [0, 100)', range100, 150)
frame.add_button('Range: [0, 1000)', range1000, 150)
frame.add_input('Enter a number to guess:', input_guess, 50)


# call new_game and start frame
new_game()
frame.start()


# always remember to check your completed program against the grading rubric
