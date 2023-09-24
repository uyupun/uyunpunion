from smbus2 import SMBus
import time

class PlayerSide(Enum):
    A: str = "A"
    B: str = "B"

class BalloonSensor:
    #デバイスのアドレス 0x52
    SENSOR_ADDR = 0x52
    SENSOR_MEASURE_ADDR = 0xd3

    def __init__(self, playerSide):
        self.playerSide = playerSide
        if self.playerSide == PlayerSide.A:
            self.i2c = SMBus(1)
        else:
            self.i2c = SMBus(4)

    def measure(self):
        data = self.i2c.read_i2c_block_data(SENSOR_ADDR, SENSOR_MEASURE_ADDR, 2)
        print(data[0] * 1000 + data[1])
        return data[0] * 1000 + data[1]

    def write(self, distance):
        sideAFile = open(f'distance_{self.playerSide}.txt', 'w+')
        sideAFile.write(str(distance))
        sideAFile.close()
