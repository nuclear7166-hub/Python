class television:
    serialNumber = 0

    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
        television.serialNumber += 1  # 변수 증가 시키기
        self.number = television.serialNumber

    def show(self):
        print(self.channel, self.volume, self.on, self.number)


tv1 = television(12, 15, True)
tv1.show()
tv2 = television(24, 14, True)
tv2.show()
tv3 = television(23, 14, False)
tv3.show()
