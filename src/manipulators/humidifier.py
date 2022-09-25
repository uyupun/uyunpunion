import sys
from time import time

import pigpio

try:
    from manipulators.manipulator import Manipulator
except ImportError:
    from manipulator import Manipulator


class HumidifierManipulator(Manipulator):
    def __init__(self) -> None:
        super().__init__()
        self.pi = pigpio.pi()
        self.pin = 23

    def start(self):
        self.pi.set_mode(self.pin, pigpio.OUTPUT)

        self.pi.write(self.pin, 1)
        time.sleep(0.5)
        self.pi.write(self.pin, 0)

        print("humidifier start")

    def stop(self):
        self.pi.set_mode(self.pin, pigpio.OUTPUT)

        self.pi.write(self.pin, 0)
        time.sleep(0.5)
        self.pi.write(self.pin, 1)
        time.sleep(0.5)
        self.pi.write(self.pin, 0)
        time.sleep(0.5)
        self.pi.write(self.pin, 1)
        time.sleep(0.5)
        self.pi.write(self.pin, 0)

        print("humidifier stop")


if __name__ == "__main__":
    action = sys.argv[1]
    manipulator = HumidifierManipulator()

    if action == "start":
        manipulator.start()
    elif action == "stop":
        manipulator.stop()
