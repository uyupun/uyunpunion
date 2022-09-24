import sys

try:
    from manipulators.manipulator import Manipulator
except ImportError:
    from manipulator import Manipulator


class HumidifierManipulator(Manipulator):
    def start(self):
        print("humidifier start")

    def stop(self):
        print("humidifier stop")


if __name__ == "__main__":
    action = sys.argv[1]
    manipulator = HumidifierManipulator()

    if action == "start":
        manipulator.start()
    elif action == "stop":
        manipulator.stop()
