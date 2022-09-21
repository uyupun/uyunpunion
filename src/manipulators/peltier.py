import sys
from enum import Enum

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
    def start(self, mode=PeltierMode.Cold):
        if mode == PeltierMode.Cold:
            return self._cold()
        if mode == PeltierMode.Warm:
            return self._warm()
        raise PeltierModeNotExistsError

    def stop(self):
        print("peltier stop")

    def _cold(self):
        print("peltier cold")

    def _warm(self):
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
