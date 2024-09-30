'''
請撰寫一程式，讓使用者輸入一個正整數，將此正整數以反轉的順序輸出，並判斷如輸入0，則輸出為0。
'''
# TODO
n = input()
ans = ''
for i in range(1, len(n)+1):
    ch = n[-i]
    ans += ch
print(ans)