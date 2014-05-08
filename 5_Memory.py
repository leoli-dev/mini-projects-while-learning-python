# implementation of card game - Memory

import simplegui
import random

# globals variables
WIDTH = 800 # width of canvas
HEIGHT = 100 # height of canvas
deck = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
WIDTH_CARD = WIDTH / len(deck) # width of each card
MARGIN = 2 # margin between the edge of card and the blue line
turns = 0
state_list = []
previous_exposed_num = -1 # -1 means null
previous_exposed_index = -1 # -1 means null

# helper function to initialize globals
def new_game():
    global deck, turns, state_list, previous_exposed_num, previous_exposed_index
    random.shuffle(deck) 
    turns = 0
    label.set_text("Turns = " + str(turns))
    # states of each number of deck: hidden, exposed, paired
    state_list = ["hidden", "hidden", "hidden", "hidden", 
              "hidden", "hidden", "hidden", "hidden", 
              "hidden", "hidden", "hidden", "hidden", 
              "hidden", "hidden", "hidden", "hidden"]
    previous_exposed_num = -1
    previous_exposed_index = -1
         
# define event handlers
def mouseclick(pos):
    global previous_exposed_num, previous_exposed_index, exposed_cards, turns
    on_click_card_index = pos[0] / WIDTH_CARD
#    if pos[0] % WIDTH_CARD == 0:
#        on_click_card_index = pos[0] / WIDTH_CARD
#    else:
#        on_click_card_index = pos[0] / WIDTH_CARD + 1

    # only respond when the card is hidden
    if state_list[on_click_card_index] == "hidden":        
        # case: no previous exposed card
        if previous_exposed_num == -1 and state_list.count("exposed") == 0:            
            previous_exposed_num = deck[on_click_card_index]
            previous_exposed_index = on_click_card_index
            state_list[on_click_card_index] = "exposed"
        # case: two previous exposed cards are not matched
        elif previous_exposed_num == -1 and state_list.count("exposed") == 2:
            # hide the two previous exposed cards
            for n in range(len(state_list)):
                if state_list[n] == "exposed":
                    state_list[n] = "hidden"
            previous_exposed_num = deck[on_click_card_index]
            previous_exposed_index = on_click_card_index
            state_list[on_click_card_index] = "exposed"   
        # case: there is a previous exposed card     
        else:
            # increase counter firstly
            turns += 1
            label.set_text("Turns = " + str(turns))
            # if this card is matched with the previous exposed card
            if previous_exposed_num == deck[on_click_card_index]:
                state_list[previous_exposed_index] = "paired"
                state_list[on_click_card_index] = "paired"
                previous_exposed_num = -1
                previous_exposed_index = -1                
            # otherwise    
            else:
                previous_exposed_num = -1
                previous_exposed_index = -1
                state_list[on_click_card_index] = "exposed"
                                   
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for n in range(len(deck)):
        if state_list[n] == "hidden":
            # four point for drawing the square of blue lines, and also two yellow diagonals
            point_upper_left = (MARGIN + n * WIDTH_CARD, MARGIN)
            point_upper_right = (WIDTH_CARD - MARGIN + n * WIDTH_CARD, MARGIN)
            point_bottom_right = (WIDTH_CARD - MARGIN + n * WIDTH_CARD, HEIGHT - MARGIN)
            point_bottom_left = (MARGIN + n * WIDTH_CARD, HEIGHT - MARGIN)
            canvas.draw_polygon([point_upper_left, point_upper_right, point_bottom_right, point_bottom_left], 2, 'Blue')
            canvas.draw_line(point_upper_left, point_bottom_right, 2, 'Yellow')
            canvas.draw_line(point_upper_right, point_bottom_left, 2, 'Yellow')            
        elif state_list[n] == "paired":
            canvas.draw_text(str(deck[n]), (5 + n * WIDTH_CARD, 80), 80, 'Green')
        else:
            canvas.draw_text(str(deck[n]), (5 + n * WIDTH_CARD, 80), 80, 'White')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
