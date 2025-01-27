'''
Final code for the Raspberry Pi Pico
'''
import board
import digitalio
import time
# configure the RED LED to GP0
red = digitalio.DigitalInOut(board.GP0)
red.direction = digitalio.Direction.OUTPUT
red.value = False
# configure the GREEN LED to GP1
green = digitalio.DigitalInOut(board.GP1)
green.direction = digitalio.Direction.OUTPUT
green.value = False
# configure the BLUE LED to GP2
blue = digitalio.DigitalInOut(board.GP2)
blue.direction = digitalio.Direction.OUTPUT
blue.value = False
# configure the button to GP15 with a pull-up resistor
# thus, the button will read True when not pressed
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

'''
Negative Edge Function
returns 1 if negative edge detected
returns 0 if no negative edge detected
'''
def edge():
    current_state = button.value # read the current state of the button
    if current_state == False: # check if the button is not pressed
        time.sleep(0.1) # wait for a short time
        if button.value == True: # check if the button is pressed, causing a negative edge
            return 1
    return 0 # otherwise, no negative edge would have occurred
'''
State Encoding:
0: Off
1: People
2: Plants
'''
state = 0 # initial state is Off
while True:
    if edge():
        state = (state + 1) % 3 # increment state. If state is 2, go back to 0
        if state == 0: # Off
            red.value = False
            green.value = False
            blue.value = False
        elif state == 1: # People
            red.value = True
            green.value = True
            blue.value = True
        elif state == 2: # Plants
            red.value = True
            green.value = False
            blue.value = True