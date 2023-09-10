import sys
import time

import pigpio

from drivers.driver import Driver


class HumidifierDriver(Driver):
    def __init__(self) -> None:
        super().__init__()
        self.pi = pigpio.pi()
        self.pin = 23

    def start(self) -> None:
        self.pi.set_mode(self.pin, pigpio.OUTPUT)

        self.pi.write(self.pin, 1)
        time.sleep(0.5)
        self.pi.write(self.pin, 0)

        print("humidifier start")

    def stop(self) -> None:
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
    driver = HumidifierDriver()

    if action == "start":
        driver.start()
    elif action == "stop":
        driver.stop()
