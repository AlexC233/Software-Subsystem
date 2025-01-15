'''
Testing the FSM for the Electrical Subsystem
Three states: Off, People, Plants
Off: No LEDs on
People: All LEDs on
Plants: Red and Blue LEDs on
Each button press changes the state
Off -> People -> Plants -> Off
'''
import board
import digitalio
import countio

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

# configure the edge counter
edgeCounter = countio.Counter(board.GP15, edge=countio.Edge.RISE)

'''
Edge Counter Function
returns 1 if positive edge detected
returns 0 if no positive edge detected
'''
def edge():
    if edgeCounter.count >= 1:
        edgeCounter.reset()
        return 1
    return 0

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
        print("State: ", state)
