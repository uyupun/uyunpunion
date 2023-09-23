from balloon import BalloonSensor
import time

while True:
    balloonSensorA = BalloonSensor(PlayerSide.A)
    balloonSensorB = BalloonSensor(PlayerSide.B)
    balloonSensorA.measure().write()
    balloonSensorB.measure().write()
    time.sleep(1)
