from datetime import datetime

current_time1 = datetime.now().strftime("%Y-%m-%d %H:%M")
current_time2 = datetime.now()
current_time3 = datetime.now().strftime("%Y년 %m월 %d일")
print(current_time3, end=" ")
current_time4 = datetime.now().strftime("%H시 %M분")
print(current_time4)
