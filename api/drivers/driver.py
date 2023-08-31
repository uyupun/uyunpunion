from abc import ABC, abstractmethod


class Driver(ABC):
    @abstractmethod
    def start():
        pass

    @abstractmethod
    def stop():
        pass
