from abc import ABC, abstractmethod


class Manipulator(ABC):
    @abstractmethod
    def start():
        pass

    @abstractmethod
    def stop():
        pass
