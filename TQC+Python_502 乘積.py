'''
請撰寫一程式，將使用者輸入的兩個整數作為參數傳遞給一個名為compute(x, y)的函式，此函式將回傳x和y的乘積。
'''

# TODO
x = eval(input())
y = eval(input())

def compute(x, y):
    ans = x * y
    return ans

print(compute(x, y))