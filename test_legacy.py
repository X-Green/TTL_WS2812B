import serial

testColorData = [0xEA, 0b01101011, 0x0D]  # rgb


def getBit(number, index):
    return (number >> index) & 1


def colorToMessage(colorData):
    # grb
    temp = colorData[0]
    colorData[0] = colorData[1]
    colorData[1] = temp

    serialMessages = []

    # totalColor = 0xFFFFFF & ~((colorData[0] << 16) + (colorData[1] << 8) + colorData[2])
    totalColor = (colorData[0] << 16) + (colorData[1] << 8) + colorData[2]
    # print(hex(totalColor))
    # print(bin(totalColor))

    constMessageMask = 0b0100100  # LSB First

    for i in range(8):
        i_offset = i * 3
        msg = constMessageMask + (getBit(totalColor, 23 - i_offset)) + (
                getBit(totalColor, 23 - (i_offset + 1)) << 3) + (getBit(totalColor, 23 - (i_offset + 2)) << 6)

        # print(bin(msg))
        # print(bin(~msg & 0x7f))

        serialMessages.append(~msg & 0x7f)
    return serialMessages


if __name__ == "__main__":
    print(colorToMessage(testColorData))
    msgs = colorToMessage(testColorData)

    try:
        # 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
        portx = "COM3"
        # 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
        # bps = 300000
        # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
        timex = 3
        # 打开串口，并得到串口对象
        ser = serial.Serial(portx, baudrate=3000000, timeout=timex,
                            bytesize=7, parity='N', stopbits=1)

        # 写数据
        result = ser.write(bytes(msgs) * 10)
        print("写总字节数:", result)

        ser.close()  # 关闭串口

    except Exception as e:
        print(e)

"""
import serial
import serial.tools.list_ports
port_list = list(serial.tools.list_ports.comports())
print(port_list[2])
"""
