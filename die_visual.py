from re import I
from die import Die
import pygal

# 创建一个撒子，并将结果返回列表
die = Die()
# 每扔一次都把结果都放在数组上
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
# 分析结果 分析每一面 1，2，3，4，5，6 每面出现次数
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果可视化
hist = pygal.Bar()
hist.title = "Result off rolling one D6 1000 times"
#hist.x_labels = ["1", "2", "3", "4", "5", "6"]
hist.x_labels = [str(value+1) for value in range(die.num_sides)]
hist.x_title = "result"
hist.y_title = "Frequency Result"

hist.add("D6", frequencies)
hist.render_to_file("die_visual.svg")
