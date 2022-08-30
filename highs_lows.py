import csv
from datetime import datetime
from matplotlib import pyplot as plt
filename = "data/csv_sitka_weather_07-2014.csv"
# first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
# print(first_date)
fig = plt.figure(dpi=128, figsize=(10,6))
# 读取csv 文件
with open(filename) as f:
    reader = csv.reader(f)
    # 读取头名称
    header_row =next(reader)
    # 打印csv 文件
    # print(header_row)
    for index, column_header in enumerate(header_row):
        print(index,column_header)

    # 读取每行数据
    dates, highs = [], []
    for row in reader:
        dates.append(datetime.strptime(row[0], '%Y-%m-%d'))
        highs.append(int(row[1]))
    # print(highs)
plt.plot(dates, highs, c="red")
plt.title("Daily high temperatures,July 2014", fontsize=24)
plt.xlabel("", fontsize=8)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.show()


