from train.driver import DriverListener
from ev3dev.ev3 import Screen
import time
import ev3dev.fonts as fonts

class display(DriverListener):
    def __init__(self):
        self.screen = Screen()

    def on_station_reached(self, station: 'Station', line: 'Line'):
        self.screen.draw.text((10,10), 'Current Station: ' + station, font=fonts.load("helvR24"))
        self.screen.update()

    def on_line_change(self, station: 'Station', curr_line: 'Line', target_line: 'Line'):
        pass

    def on_end_station_reached(self, station: 'Station', line: 'Line'):
        self.screen.draw.text((10, 10), 'Current Station: ' + station, font=fonts.load("helvR24"))
        self.screen.update()