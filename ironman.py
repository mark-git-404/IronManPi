from gpiozero import Motor
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
    def Click(self, pinNumber):
        
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
    arm = Motor(35, 37)
    hand = Motor(10,11)
    head = Motor(35, 37)

    iron = IronGPIO(arm, hand, head)

    while True:
        iron.MoveArm(hand, 2, way=0)
        iron.MoveArm(hand, 2, way=1)


    iron.Move()
    



if __name__ == __main__:
