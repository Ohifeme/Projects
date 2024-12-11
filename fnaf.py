import time
import random
import threading
import pygame,sys


# Game variablesyes
power = 100
time_remaining = 360  # 6 minutes (game time)
cameras = ['East Hall', 'West Hall', 'Kitchen', 'Pirate Cove']
animatronics = ['Freddy', 'Bonnie', 'Chica', 'Foxy', 'Golden Fred']
camera_status = {camera: False for camera in cameras}  # All cameras start off
door_closed = False

# Custom functions
def text_animation_intro(msg):
    for i in msg:
        print(i,end="",flush=True)
        time.sleep(0.03)

def text_animation_game(msg):
    for i in msg:
        print(i,end="",flush=True)
        time.sleep(0.02)

def play_audio(filepth):
    pygame.mixer.init()
    pygame.mixer.music.load(filepth)
    pygame.mixer.music.play()



    




# Game introduction

text_animation_intro("\nWelcome to Five Nights at Freddy's!\n")
time.sleep(1)
text_animation_intro("There are consequences for not listening to me...\n")
time.sleep(1)
action1=input(text_animation_intro("Type the 'yes' to start")) #prints out a none
if action1=="yes":
    time.sleep(2)
    text_animation_intro("Don't listen the noises!\n")
else:
    play_audio("/Users/ohifemeunuigboje/Documents/feddy fazebear/foxy yap.mp3")
    time.sleep(2)
    text_animation_game("Consequences...\n")
    text_animation_game("Foxy is now aware of your presence\n")
    time.sleep(10)


input(text_animation_game("Press Enter to listen to Phone guy's message")) #fix this

play_audio('/Users/ohifemeunuigboje/Documents/feddy fazebear/phoneguy.mp3')

time.sleep(7)

action2=input(text_animation_intro("To stop Phone Guy's memo, type 'stop'. To play with Phone guy's memo in the background, enter 'play'\n\n"))
if action2=='stop':
    pygame.mixer.music.stop()
elif action2=='play':
    text_animation_intro("Good job listening to Phone Guy!\n")
    time.sleep(3)
else:
    pygame.mixer.music.stop()
    play_audio("/Users/ohifemeunuigboje/Documents/feddy fazebear/Nightmare Foxy .mp3")
    time.sleep(1)
    text_animation_game("Uh Oh! You didn't listen and have awoken Nightmare Foxy!\n")
    time.sleep(5)



text_animation_intro("Survive the night by monitoring cameras and managing power.\n")
time.sleep(1)
text_animation_intro("Power drains when cameras are active or the door is closed.\n")
time.sleep(1)
text_animation_intro("Type 'check cameras', 'close door', or 'open door' to play.\n")
time.sleep(1)

def check_cameras():
    global power
    active_camera = random.choice(cameras)
    text_animation_game(f"Checking cameras... Animatronics spotted in {active_camera}!")
    camera_status[active_camera] = True
    power -= 5

def close_door():
    global power, door_closed
    if door_closed:
        text_animation_game("The door is already closed!")
    else:
        text_animation_game("You close the door.")
        door_closed = True
        power -= 10

def open_door():
    global door_closed
    if door_closed:
        text_animation_game("You open the door.")
        door_closed = False
    else:
        text_animation_game("The door is already open!")

def random_events():
    # Simulates animatronics moving or approaching
    animatronic = random.choice(animatronics)
    event = random.choice(["approaching the office", "moving in the halls"])
    print(f"Warning: {animatronic} is {event}!")

# Game loop
while time_remaining > 0 and power > 0:
    print(f"\nTime Remaining: {time_remaining // 60}:{time_remaining % 60:02}")
    print(f"Power: {power}%")
    action = input("Your action (check cameras / close door / open door): ").strip().lower()

    if action == 'check cameras':
        check_cameras()
    elif action == 'close door':
        close_door()
    elif action == 'open door':
        open_door()
    else:
        print("Invalid action! Please choose a valid command.")

    # Power drains passively
    power -= 1 if not door_closed else 2

    # Random animatronic events
    if random.random() < 0.3:  # 30% chance of an event
        random_events()

    # Time decreases
    time_remaining -= 5
    time.sleep(1)

# Game end
if power <= 0:
    print("\nYou've run out of power. The animatronics got you!")
elif time_remaining <= 0:
    print("\n6:00 AM! You survived the night!")
