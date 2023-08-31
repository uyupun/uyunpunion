import sys
import time

import pigpio

try:
    from drivers.driver import Driver
except ImportError:
    from drivers import Driver


class BlowerDriver(Driver):
    def __init__(self) -> None:
        super().__init__()
        self.pi = pigpio.pi()
        self.pin = 25

    def start(self):
        self.pi.set_mode(self.pin, pigpio.OUTPUT)

        self.pi.write(self.pin, 1)
        time.sleep(0.5)

        print("blower start")

    def stop(self):
        self.pi.set_mode(self.pin, pigpio.OUTPUT)

        self.pi.write(self.pin, 0)
        time.sleep(0.5)

        print("blower stop")


if __name__ == "__main__":
    action = sys.argv[1]
    driver = BlowerDriver()

    if action == "start":
        driver.start()
    elif action == "stop":
        driver.stop()
