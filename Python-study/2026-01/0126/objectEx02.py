# 외워야함


class television:
    def __init__(self, channel, volume, on):
        self.channel = channel  # 속성,멤버 변수                변수                함수
        self.volume = volume  # 속성,멤버 변수              channel             __init__
        self.on = on  # 속성,멤버 변수               volume               show
        #                               on               set channel
        #                                                get channel

    def show(self):
        print(self.channel, self.volume, self.on)

    def setchannel(self, channel):
        self.channel = channel

    def getChannel(self):
        return self.channel

    def getVolume(self):
        return self.volume

    def setOn(self, on):
        self.on = on

    def getOn(self):
        return self.on


tv1 = television(9, 10, True)
tv1.show()
tv1.setchannel(24)
print(tv1.getChannel(), tv1.channel)
tv2 = television(6, 15, True)
