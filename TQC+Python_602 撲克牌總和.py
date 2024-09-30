'''
請撰寫一程式，讓使用者輸入52張牌中的5張，計算並輸出其總和。

提示：J、Q、K以及A分別代表11、12、13以及1。
'''

# TODO
# J、Q、K以及A分別代表11、12、13以及1

s = []
total = 0
for i in range(5):
    s.append(input())
    if s[i] == 'J':
        total += 11
    elif s[i] == 'Q':
        total += 12
    elif s[i] == 'K':
        total += 13
    elif s[i] == 'A':
        total += 1 
    else:
        total += eval(s[i])
print(total)
        
    