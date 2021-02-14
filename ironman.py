import gpiozero
from time import sleep
import asyncio
import websockets

class IronGPIO:
    def __init__(self, arm, hand, head):
        self.arm = arm
        self.hand = hand
        self.head = head
    """
        Args:
            pinNumber (int) [0 - 40] - pin number in BoardMode
    """
    def ClickPin(self, pinNumber):
        pin = pinNumber

        
        return 1

    """
        Args:
            degree (int) [ 1 < x < 360 ] - how much you want to move the arm
            way    (int) [ 0 or 1] - way you want to move the arm
    """
    def MoveArm(self, motor, time, way = 0 ):
        if (way == 0):
            motor.forward()
            time.sleep(time)
            motor.stop()
        else:
            motor.backward()
            time.sleep(time)
            motor.stop()

        
            


def test():
    #! Instances
    arm = gpiozero.Motor(35, 37)
    hand = gpiozero.Motor(33, 35)
    head = gpiozero.Motor(3, 37)

    iron = IronGPIO(arm, hand, head)

    while True:
        iron.MoveArm(hand, 2, way=0)
        iron.MoveArm(hand, 2, way=1)

    
test()