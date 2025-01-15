'''
File to test edge dectection.
On each negative edge of the button, the LED will toggle on and off.
'''
import board
import digitalio
import countio

# configure the LED to GP14
led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT
# initialize the value of the LED to off
led.value = False

# configure the button to GP15
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
# set the pull up resistor
button.pull = digitalio.Pull.UP

# configure the edge counter
# following example from https://docs.circuitpython.org/en/latest/shared-bindings/countio/index.html#countio.Edge
edgeCounter = countio.Counter(board.GP15, edge=countio.Edge.FALL)
print("Edge Counter Set")

while True:
    # if a edge is detected, toggle the LED
    if edgeCounter.count > 0:
        print(edgeCounter.count)
        led.value = not led.value
        edgeCounter.reset()
