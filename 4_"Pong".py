# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
LEFT = False
RIGHT = True

# add some global variables
ball_pos = [WIDTH / 2.0, HEIGHT / 2.0]
ball_vel = [0.0, 0.0]
score_left = 0
score_right = 0
paddle_left_pos = HEIGHT / 2 - PAD_HEIGHT / 2
paddle_right_pos = HEIGHT / 2 - PAD_HEIGHT / 2
paddle_left_vel = 0
paddle_right_vel = 0
PAD_VEL_CST = 3 # constant of velocity of paddles

# add some global temps
temp_ball_vel = 0
temp_PAD_VEL_CST = 0
is_pause = False





# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2.0, HEIGHT / 2.0]
    if direction == LEFT: # direction: upper left
        ball_vel = [-(random.randrange(2, 4) + random.randrange(0, 100) * 0.01), -(random.randrange(1, 3) + random.randrange(0, 100) * 0.01)]
    else: # direction: upper right
        ball_vel = [(random.randrange(2, 4) + random.randrange(0, 100) * 0.01), -(random.randrange(1, 3) + random.randrange(0, 100) * 0.01)]

        
        
        
        
# define event handlers
def new_game():
    global paddle_left_pos, paddle_right_pos, paddle_left_vel, paddle_right_vel  
    global score_left, score_right
    # choose the direction randomly by default
    if random.randrange(0,2) == 0: 
        spawn_ball(LEFT) 
    else:
        spawn_ball(RIGHT) 
    # reset the score
    score_left = 0
    score_right = 0
    
# draw handler
def draw(canvas):
    global score_left, score_right, paddle_left_pos, paddle_right_pos, paddle_left_vel, paddle_right_vel, ball_pos, ball_vel       
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw scores
    canvas.draw_text(str(score_left), [WIDTH / 4 - 25, (HEIGHT / 2) + 30], 100, 'Red')
    canvas.draw_text(str(score_right), [(WIDTH / 4) * 3 - 25, (HEIGHT / 2) + 30], 100, 'Green')
    
    # update ball
    # if the ball is going to pass through left gutter
    if ball_pos[0] - BALL_RADIUS + ball_vel[0] < PAD_WIDTH:
        # while the ball is touching left gutter without paddle left
        if ball_pos[1] < paddle_left_pos or ball_pos[1] > paddle_left_pos + PAD_HEIGHT:            
            # print some information for debug
            print 'The ball hit the left gutter, at the point: [' + str(ball_pos[0] - BALL_RADIUS) + ', ' + str(ball_pos[1]) + ']'
            print 'The upper right corner of left paddle is: [' + str(PAD_WIDTH) + ', ' + str(paddle_left_pos) + ']'
            print 'The bottom right corner of left paddle is: [' + str(PAD_WIDTH) + ', ' + str(paddle_left_pos + PAD_HEIGHT) + ']'
            print
            score_right += 1
            spawn_ball(RIGHT)
        else:
            # while the ball is touching left gutter with paddle left
            ball_vel[0] = -(ball_vel[0] * 1.1)
            ball_vel[1] = (ball_vel[1] * 1.1)      
    # if the ball is going to pass through right gutter
    if ball_pos[0] + BALL_RADIUS + ball_vel[0] > WIDTH - PAD_WIDTH:
        # while the ball is touching right gutter without paddle right
        if ball_pos[1] < paddle_right_pos or ball_pos[1] > paddle_right_pos + PAD_HEIGHT:            
            # print some information for debug
            print 'The ball hit the right gutter, at the point: [' + str(ball_pos[0] + BALL_RADIUS) + ', ' + str(ball_pos[1]) + ']'
            print 'The upper left corner of right paddle is: [' + str(WIDTH - PAD_WIDTH) + ', ' + str(paddle_right_pos) + ']'
            print 'The bottom left corner of right paddle is: [' + str(WIDTH - PAD_WIDTH) + ', ' + str(paddle_right_pos + PAD_HEIGHT) + ']'
            print
            score_left += 1
            spawn_ball(LEFT)
        else:
            # while the ball is touching right gutter with paddle right
            ball_vel[0] = -(ball_vel[0] * 1.1)
            ball_vel[1] = (ball_vel[1] * 1.1)         
    
    # if the ball is going to pass through upper of the canvas or bottom of the canvas    
    if ball_pos[1] - BALL_RADIUS + ball_vel[1] < 0 or ball_pos[1] + BALL_RADIUS + ball_vel[1] > HEIGHT:
        ball_vel[1] = -ball_vel[1]
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS-2, 2, 'Yellow', 'Orange')
    
    # update paddle's vertical position, keep paddle on the screen
    # make sure paddle left stay in the canvas
    if paddle_left_pos + paddle_left_vel >= 0 and paddle_left_pos + paddle_left_vel <= HEIGHT - PAD_HEIGHT:
        paddle_left_pos += paddle_left_vel
    # make sure paddle right stay in the canvas    
    if paddle_right_pos + paddle_right_vel >= 0 and paddle_right_pos + paddle_right_vel <= HEIGHT - PAD_HEIGHT:
        paddle_right_pos += paddle_right_vel
        
    # draw paddles
    # paddle left
    canvas.draw_polygon([[0, paddle_left_pos], [PAD_WIDTH, paddle_left_pos], [PAD_WIDTH, paddle_left_pos + PAD_HEIGHT], [0, paddle_left_pos + PAD_HEIGHT]], 1, 'Red', 'Red')
    # paddle right
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle_right_pos], [WIDTH, paddle_right_pos], [WIDTH, paddle_right_pos + PAD_HEIGHT], [WIDTH - PAD_WIDTH, paddle_right_pos + PAD_HEIGHT]], 1, 'Green', 'Green')
    #print ball_vel

# key down handler
def keydown(key):
    global paddle_left_vel, paddle_right_vel
    if key == simplegui.KEY_MAP['w']:
        paddle_left_vel = -PAD_VEL_CST
    elif key == simplegui.KEY_MAP['s']:
        paddle_left_vel = PAD_VEL_CST    
    elif key == simplegui.KEY_MAP['up']:
        paddle_right_vel = -PAD_VEL_CST
    elif key == simplegui.KEY_MAP['down']:
        paddle_right_vel = PAD_VEL_CST
          
# key up handler   
def keyup(key):
    global paddle_left_vel, paddle_right_vel
    if key == simplegui.KEY_MAP['w']:
        paddle_left_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle_left_vel = 0    
    elif key == simplegui.KEY_MAP['up']:
        paddle_right_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle_right_vel = 0

# 'Restart' button handler
def btn_restart():
    global is_pause, PAD_VEL_CST, paddle_left_pos, paddle_right_pos
    # Resume the game
    if is_pause == True:
        is_pause = False
        PAD_VEL_CST = temp_PAD_VEL_CST           
    # reset the position of paddles
    paddle_left_pos = HEIGHT / 2 - PAD_HEIGHT / 2
    paddle_right_pos = HEIGHT / 2 - PAD_HEIGHT / 2
    # make a new game
    new_game()

# 'Pause / Resume' button handler
def btn_pause_resume():
    global temp_ball_vel, temp_PAD_VEL_CST, is_pause, ball_vel, PAD_VEL_CST
    if is_pause == False:
        is_pause = True
        temp_ball_vel = ball_vel
        ball_vel = [0, 0]
        temp_PAD_VEL_CST = PAD_VEL_CST
        PAD_VEL_CST = 0
    else:
        is_pause = False
        ball_vel = temp_ball_vel
        PAD_VEL_CST = temp_PAD_VEL_CST
      
        
        
        
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', btn_restart, 100)
frame.add_button('Pause / Resume', btn_pause_resume, 150) # add one more button for debug

# start frame
new_game()
frame.start()
