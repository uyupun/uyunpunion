import sys
import time
from enum import Enum

import pigpio

from drivers.driver import Driver


class PeltierMode(Enum):
    Cold: str = "cold"  # type: ignore
    Warm: str = "warm"  # type: ignore


class PeltierModeNotExistsError(Exception):
    pass


class PeltierDriver(Driver):
    def __init__(self) -> None:
        super().__init__()

        self.apwm = 19
        self.ain1 = 20
        self.ain2 = 21

        self.pi = pigpio.pi()

    def init_peltier(self) -> None:
        for pin in [self.apwm, self.ain1, self.ain2]:
            self.pi.set_mode(pin, pigpio.OUTPUT)
            self.pi.write(pin, 0)

    def start(self, mode: PeltierMode = PeltierMode.Cold) -> None:
        self.init_peltier()

        if mode == PeltierMode.Cold:
            return self._cold()
        if mode == PeltierMode.Warm:
            return self._warm()
        raise PeltierModeNotExistsError

    def stop(self) -> None:
        self.init_peltier()

        print("peltier stop")

    def _cold(self) -> None:
        self.pi.hardware_PWM(self.apwm, 1000, (100 * 10000))
        self.pi.write(self.ain1, 0)
        self.pi.write(self.ain2, 1)
        time.sleep(0.5)

        print("peltier cold")

    def _warm(self) -> None:
        self.pi.hardware_PWM(self.apwm, 1000, (100 * 10000))
        self.pi.write(self.ain1, 1)
        self.pi.write(self.ain2, 0)
        time.sleep(0.5)

        print("peltier warm")


if __name__ == "__main__":
    action = sys.argv[1]
    driver = PeltierDriver()

    if action == "cold":
        driver.start(mode=PeltierMode.Cold)
    if action == "warm":
        driver.start(mode=PeltierMode.Warm)
    elif action == "stop":
        driver.stop()
