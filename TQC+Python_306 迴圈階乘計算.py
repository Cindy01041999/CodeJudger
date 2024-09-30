'''
請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數n，利用迴圈計算並輸出n!的值。
'''

# TODO
n = int(input())
total = 1
for i in range(1, n+1):
    total = total * i
print(total)