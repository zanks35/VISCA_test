import argparse
import time

import serial



# com =input('输入端口号：')
# port = serial.Serial(port=com, baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.025)
class Port():
    # print(1)
    def __init__(self):
        # print(2)
        # com = input('输入端口号：')
        parser = argparse.ArgumentParser(description='输入端口号')
        parser.add_argument("--COM", type=str, default="com3")
        args = parser.parse_args()
        port = args.COM
        self.port = serial.Serial(port=port, baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.08)
    def send(self, cmd):
        self.port.write(cmd)
        # time.sleep(1)
        response = self.port.readall()
        # time.sleep(3)
        # print(response)
        response = self.convert_hex(response)
        # print(response)
        return response

    def convert_hex(self, string):
        result = []
        # print(string)
        for item in string:
            result.append(hex(item))
        return result

    def check(self, timing, send_data):
        """
        测试数据返回值函数
        :param timing:
        :param send_data:
        :return:
        """
        data = self.send(send_data)
        time.sleep(timing)
        print("+++++++++++++++++++++++++data:", data)

        if data == ['0x90', '0x41', '0xff', '0x90', '0x51', '0xff']:
            return True
        elif data == ['0x90', '0x61', '0x41','0xff']:
            print('无法识别该指令')
            return False
        else:
            print('校验错误')
            print(data)
            return False
# Port().send(WB_Quire)