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
        self.i2c = SMBus(
            SMBus(1) if self.playerSide.value === PlayerSide.A.value else SMBus(4)
        )

    def measure(self):
        data = i2c.read_i2c_block_data(SENSOR_ADDR, SENSOR_MEASURE_ADDR, 2)
        print(data[0] * 1000 + data[1])
        return data[0] * 1000 + data[1]

    def write(self, distance):
        sideAFile = open(f'distance_{self.playerSide}.txt', 'w+')
        sideAFile.write(str(distance))
        sideAFile.close()
