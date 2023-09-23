from smbus2 import SMBus
import time

#SMBusの引数に1を指定する。Raspberry Piのi2cバスの番号
i2c = SMBus(1)
#デバイスのアドレス 0x52
addr = 0x52

#1バイト データの書き込み
#i2c.write_byte_data　アドレス　書き込みたいデータのアドレス　書き込むデータ
# i2c.write_byte_data(addr, 0x06, 0xF0)

#複数バイト　データ書き込み
#i2c.write_i2c_block_data　アドレス　書き込みたいデータのアドレス　書き込むデータ(配列)
# i2c.write_i2c_block_data(addr, 0x07, [0x02, 0x01])

#1バイト　データ読み込み
#コマンドフォーマット　アドレス　読み込みたいデータのアドレス
# data = i2c.read_byte_data(addr, 0xd3)
# print(data)

#複数バイト　データ読み込み
#i2c.read_i2c_block_data　アドレス　読み込みたいデータのアドレス　データ数
data = i2c.read_i2c_block_data(addr, 0xd3, 2)
print(data)
distance = data[0] * 1000 + data[1]
print(distance)

# ファイル書き込み
sideAFile = open('distance_a.txt', 'w+')
sideAFile.write(str(distance))
sideAFile.close()
