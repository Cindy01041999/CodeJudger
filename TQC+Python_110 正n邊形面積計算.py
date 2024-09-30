'''
請撰寫一程式，讓使用者輸入兩個正數n、s，代表正n邊形之邊長為s，計算並輸出此正n邊形之面積（Area）。

提示1：建議使用import math模組的math.pow及math.tan
提示2：正n邊形面積的公式如下：Area=(n*s*s)/(4*tan(pi/n))
提示3：輸出浮點數到小數點後第四位
'''

# TODO

n = eval(input())
s = eval(input())

# TODO
import math

"""
Area = _
"""
Area = (n*s*s) / (4 * math.tan(math.pi/n))
Area2 = "Area = %.4f" % Area
print(Area2)