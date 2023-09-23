from typing import Literal


class BalloonDriver:
    def status(self):
        print("balloon status")

    def needle(self, balloon_id: Literal[1, 2]):
        print("balloon needle")
