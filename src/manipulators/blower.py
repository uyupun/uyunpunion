import sys

from manipulator import Manipulator


class BlowerManipulator(Manipulator):
    def start(self):
        print("blower start")

    def stop(self):
        print("blower stop")


if __name__ == "__main__":
    action = sys.argv[1]
    manipulator = BlowerManipulator()

    if action == "start":
        manipulator.start()
    elif action == "stop":
        manipulator.stop()
