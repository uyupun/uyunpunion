import sys
import time
from enum import Enum

import pigpio

try:
    from manipulators.manipulator import Manipulator
except ImportError:
    from manipulator import Manipulator


class PeltierMode(Enum):
    Cold: str = "cold"
    Warm: str = "warm"


class PeltierModeNotExistsError(Exception):
    pass


class PeltierManipulator(Manipulator):
    def __init__(self) -> None:
        super().__init__()

        self.apwm = 19
        self.ain1 = 20
        self.ain2 = 21

        self.pi = pigpio.pi()

    def init_peltier(self):
        for pin in [self.apwm, self.ain1, self.ain2]:
            self.pi.set_mode(pin, pigpio.OUTPUT)
            self.pi.write(pin, 0)

    def start(self, mode=PeltierMode.Cold):
        self.init_peltier()

        if mode == PeltierMode.Cold:
            return self._cold()
        if mode == PeltierMode.Warm:
            return self._warm()
        raise PeltierModeNotExistsError

    def stop(self):
        self.init_peltier()

        print("peltier stop")

    def _cold(self):
        self.pi.hardware_PWM(self.apwm, 1000, (100 * 10000))
        self.pi.write(self.ain1, 1)
        self.pi.write(self.ain2, 0)
        time.sleep(0.5)

        print("peltier cold")

    def _warm(self):
        self.pi.hardware_PWM(self.apwm, 1000, (100 * 10000))
        self.pi.write(self.ain1, 0)
        self.pi.write(self.ain2, 1)
        time.sleep(0.5)

        print("peltier warm")


if __name__ == "__main__":
    action = sys.argv[1]
    manipulator = PeltierManipulator()

    if action == "cold":
        manipulator.start(mode=PeltierMode.Cold)
    if action == "warm":
        manipulator.start(mode=PeltierMode.Warm)
    elif action == "stop":
        manipulator.stop()
