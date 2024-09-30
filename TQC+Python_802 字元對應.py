'''
請撰寫一程式，要求使用者輸入一字串，顯示該字串每個字元的對應ASCII碼及其總和。
'''

# TODO
total = 0
data = input()

for i in range(len(data)):
    num = ord(data[i])
    print("ASCII code for '%s' is %d" %(data[i], num))
    total += num
print(total)