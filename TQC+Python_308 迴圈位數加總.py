'''
請使用迴圈敘述撰寫一程式，要求使用者輸入一個數字，此數字代表後面測試資料的數量。每一筆測試資料是一個正整數（由使用者輸入），將此正整數的每位數全部加總起來。
'''

# TODO
n1 = int(input())

"""
Sum of all digits of _ is _
"""

for i in range(n1):
    n2 = input()
    ans = 0
    for i in n2:
        ans += eval(i)
    print('Sum of all digits of ' + str(n2) + ' is ' + str(ans))