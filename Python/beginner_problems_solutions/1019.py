input_sec = int(input())
hour = input_sec // 3600
remain_sec = input_sec % 3600
min = remain_sec // 60
sec = remain_sec % 60
print(f"{hour}:{min}:{sec}")
