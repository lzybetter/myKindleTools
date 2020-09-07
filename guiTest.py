import tkinter
import pygeoip

class FindLoaction(object):
    def __init__(self):
        self.gi = pygeoip.GeoIP('./GeoLiteCity.dat')