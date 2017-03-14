from train.driver import driverListener
from ev3dev.ev3 import Screen
import ev3dev.fonts as fonts

class display(object):
    def __init__(self):
        self.screen = Screen()
    def showstartpoint(self, startpoint: str, driverlistener: bool):
        if driverlistener.onStartStaion:
            self.screen.draw.text((10,10), startpoint, font=fonts.load("helvR24"))
            self.screen.update()

    def showendpoint(self, endpoint: str, driver_listener: bool):
        if driver_listener.onendstaion:
            self.screen.draw.text((10, 10), endpoint, font=fonts.load("helvR24"))
            self.screen.update()

    onEndStationReach

    onStartStationReach

    onChangeLine