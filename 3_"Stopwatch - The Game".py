""" Mini-project # 3 - "Stopwatch: The Game" """

""" 1. import module """
import simplegui

""" 2. define global variables """
counter = 0 # This variable counts each tenths of second when the timer starts
number_of_successful_stops = 0 # This variable counts the number of successful stops, like "0:10.0"
number_of_total_stops = 0 # This variable counts the number of total stops


""" 3. define helper function format that converts time
       in tenths of seconds into formatted string A:BC.D """
def format(t):
    tenths_of_seconds = t % 10
    seconds = (t - tenths_of_seconds) / 10 % 10
    ten_seconds = (t - seconds * 10 - tenths_of_seconds) / 100 % 6
    minutes = (t - ten_seconds * 100 - seconds * 10 - tenths_of_seconds) / 600
    return str(minutes) + ":" + str(ten_seconds) + str(seconds) + "." + str(tenths_of_seconds)
    
""" 4. define event handlers for buttons; "Start", "Stop", "Reset" """
# handler for button "Start"
def btnStart():
    if not timer.is_running():
        timer.start()
        
# handler for button "Stop"
def btnStop():
    global number_of_successful_stops, number_of_total_stops
    if timer.is_running():
        timer.stop()
        number_of_total_stops += 1
        if counter % 10 == 0:
            number_of_successful_stops += 1    

# handler for button "Reset"
def btnReset():
    global counter, number_of_successful_stops, number_of_total_stops
    if timer.is_running():
        timer.stop()
    # reset all the global variables   
    counter = 0
    number_of_successful_stops = 0
    number_of_total_stops = 0

""" handler for button "Start & Stop" (PS: it's useful but not necessary) """
def btnStartAndStop():
    global counter, number_of_successful_stops, number_of_total_stops 
    if timer.is_running():
        timer.stop()
        number_of_total_stops += 1
        if counter % 10 == 0:
            number_of_successful_stops += 1 
    else:
        timer.start()

""" 5. define event handler for timer with 0.1 sec interval """
def timer_handler():
    global counter
    counter += 1

""" 6. define draw handler """
def draw_handler(canvas):
    # draw "0:00.0"
    canvas.draw_text(format(counter), (100, 150), 80, 'Blue')
    # draw "0/0"
    canvas.draw_text(str(number_of_successful_stops), (250, 50), 50, 'Red') # display corretly range: 0-99
    canvas.draw_text("/"+str(number_of_total_stops), (300, 50), 50, 'Gray') # display corretly range: 0-999
    
""" 7. create frame """
frame = simplegui.create_frame('Stopwatch', 400, 200, 150)
frame.set_canvas_background('White')

""" 8. register event handlers """
frame.set_draw_handler(draw_handler)
frame.add_button('Start', btnStart, 100)
frame.add_button('Stop', btnStop, 100)
frame.add_button('Reset', btnReset, 100)
timer = simplegui.create_timer(100, timer_handler)
""" Attention:
    I add this button to make the Stopwatch easier for control,
    and it's also easier for test. """
frame.add_button('Start & Stop', btnStartAndStop, 100)


""" 9. start frame """
frame.start()
