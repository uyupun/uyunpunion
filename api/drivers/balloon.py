from typing import Literal

from drivers.driver import Driver


class BalloonDriver(Driver):
    def status(self):
        print("balloon status")

    def needle(self, balloon_id: Literal[1, 2]):
        print("balloon needle")
