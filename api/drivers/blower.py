import sys
import time

import pigpio

from drivers.driver import Driver
from settings import get_settings

settings = get_settings()


class BlowerDriver(Driver):
    def __init__(self) -> None:
        super().__init__()
        self.pi = pigpio.pi()
        self.pin = 25

    def start(self) -> None:
        if settings.ENV == "dev":
            print("blower started")
            return

        self.pi.set_mode(self.pin, pigpio.OUTPUT)
        self.pi.write(self.pin, 1)
        time.sleep(0.5)
        print("blower started")

    def stop(self) -> None:
        if settings.ENV == "dev":
            print("blower stopped")
            return

        self.pi.set_mode(self.pin, pigpio.OUTPUT)
        self.pi.write(self.pin, 0)
        time.sleep(0.5)
        print("blower stopped")


if __name__ == "__main__":
    action = sys.argv[1]
    driver = BlowerDriver()

    if action == "start":
        driver.start()
    elif action == "stop":
        driver.stop()
