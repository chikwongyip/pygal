from re import I
from die import Die
import pygal

# 创建一个撒子，并将结果返回列表
die_1 = Die()
die_2 = Die()
# 每扔一次都把结果都放在数组上
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# 分析结果 分析每一面 1，2，3，4，5，6 每面出现次数
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果可视化
hist = pygal.Bar()
hist.title = "Result off rolling one D6 1000 times"
# hist.x_labels = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12" ]
# 色子个数 到两个色子面的最大数之和
hist.x_labels = [str(x) for x in range(2,die_1.num_sides+die_2.num_sides+1)]
hist.x_title = "result"
hist.y_title = "Frequency Result"

hist.add("D6 + D6", frequencies)
hist.render_to_file("dice_visual.svg")
