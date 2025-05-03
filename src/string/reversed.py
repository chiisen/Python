s = "Hello Python"
reversed_s = s[::-1]
print("使用切片：\n" + reversed_s)  # 輸出：nohtyP olleH


s = "Hello Python"
reversed_s = ''.join(reversed(s))
print("使用 reversed() 函式再用 join() 合併：\n" + reversed_s)


s = "Hello Python"
reversed_s = ""
for c in s:
    reversed_s = c + reversed_s
print("迴圈累加反向字元：\n" + reversed_s)


s = "Hello Python"
l = list(s)
l.reverse()
reversed_s = ''.join(l)
print("轉成 list 用 reverse()，再用 join()：\n" + reversed_s)

