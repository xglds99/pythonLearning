sunrise = "上午06：15"
sunset = "下午07：10"
rise_hour = sunrise[2:4]
rise_minute = sunrise[-2:]
set_hour = sunset[2:4]
set_minute = sunset[-2:]
hour = int(set_hour) + 12 - int(rise_hour)
minute = int(set_minute) - int(rise_minute)
if minute >= 0:
    print(f"日出时间为{hour}小时{minute}分钟")
else:
    print(f"日出时间为{hour-1}小时{minute + 60}分钟")