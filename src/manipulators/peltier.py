from enum import Enum

from manipulators.manipulator import Manipulator


class PeltierMode(Enum):
    Cold: str = "cold"
    Warm: str = "warm"


class PeltierModeNotExistsError(Exception):
    pass


class PeltierManipulator(Manipulator):
    def start(self, mode=PeltierMode.Cold):
        if mode is PeltierMode.Cold:
            return self._cold()
        if mode is PeltierMode.Warm:
            return self._warm()
        raise PeltierModeNotExistsError

    def stop(self):
        pass

    def _cold(self):
        pass

    def _warm(self):
        pass
