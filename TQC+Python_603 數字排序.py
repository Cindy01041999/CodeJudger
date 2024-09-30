'''
請撰寫一程式，要求使用者輸入十個數字並存放在串列中。接著由大到小的順序顯示最大的3個數字。
'''

# TODO
data = []

for i in range(10):
    data.append(eval(input()))
    
data.sort()
print(data[-1], data[-2], data[-3])