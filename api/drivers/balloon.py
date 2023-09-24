import time
from typing import Literal

import pigpio


class BalloonDriver:
    def __init__(self) -> None:
        # super().__init__()
        self.pi = pigpio.pi()
        self.pin = 18
        self.pi.set_mode(self.pin, pigpio.OUTPUT)

    def status(self):
        print("balloon status")

    def needle(self, balloon_id: Literal[1, 2]) -> None:
        self.pi.set_servo_pulsewidth(self.pin, 1500)
        time.sleep(1)

        self.pi.set_servo_pulsewidth(self.pin, 2000)
        time.sleep(1)

        self.pi.set_servo_pulsewidth(self.pin, 1500)
        time.sleep(1)

        self.pi.set_servo_pulsewidth(self.pin, 0)
        self.pi.stop()
        print("balloon needle")
