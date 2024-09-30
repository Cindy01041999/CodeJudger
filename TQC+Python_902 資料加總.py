'''
請撰寫一程式，讀取read.txt的內容（內容為數字，以空白分隔）並將這些數字加總後輸出。檔案讀取完成後要關閉。
'''

f = open("read.txt", 'r')
# TODO
data = f.read()
f.close()

num = data.split()

total = 0
for i in range(len(num)):
     total += eval(num[i])
 
print(total)