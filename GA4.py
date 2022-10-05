#Group Actvity 4

import turtle
import time

gm = turtle.Screen()      #Create the game enviroment
gm.title("Python Game")
gm.bgcolor("grey")

ch = turtle.Turtle()   #Initialize the character
ch.color("purple")
ch.speed(1)
ch.shape("arrow")
ch.penup()

is_paused = False

def toggle_pause():  #Pause Feature 
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True

gm.listen()             #tell python to listen to keypresses
gm.onkeypress(toggle_pause, "p")


time_limit = 10             #start of the time limit
start_time = time.time()

while True:
    if not is_paused:                 #Time limit 
        ch.forward(1)
        ch.left(1)

        elapsed_time = time.time() - start_time
        print(time_limit - int(elapsed_time))

        if elapsed_time > time_limit:
            print("GAME OVER")
            exit()
    else:
        start_time = time.time() - elapsed_time
        gm.update()
