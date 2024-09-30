'''
請撰寫一程式，輸入並建立兩組數組，各以-9999為結束點（數組中不包含-9999）。將此兩數組合併並從小到大排序之，顯示排序前的數組和排序後的串列。
'''

# TODO
data1=()
data2=()
print("Create tuple1:")
# TODO

while True:
    num = eval(input())
    if num == -9999:
        break
    data1 += (num,)

print("Create tuple2:")
# TODO

while True:
    num = eval(input())
    if num == -9999:
        break
    data2 += (num,)

"""
Combined tuple before sorting: _
Combined list after sorting: _
"""
print('Combined tuple before sorting:', data1 + data2)
print('Combined list after sorting:', sorted(list(data1 + data2)))
