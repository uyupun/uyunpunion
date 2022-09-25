import sys

import pigpio

try:
    from manipulators.manipulator import Manipulator
except ImportError:
    from manipulator import Manipulator


class BlowerManipulator(Manipulator):
    def __init__(self) -> None:
        super().__init__()
        self.pi = pigpio.pi()
        self.pin = 25

    def start(self):
        self.pi.set_mode(self.pin, pigpio.OUTPUT)

        self.pi.write(self.pin, 1)

        print("blower start")

    def stop(self):
        self.pi.set_mode(self.pin, pigpio.OUTPUT)

        self.pi.write(self.pin, 0)

        print("blower stop")


if __name__ == "__main__":
    action = sys.argv[1]
    manipulator = BlowerManipulator()

    if action == "start":
        manipulator.start()
    elif action == "stop":
        manipulator.stop()
