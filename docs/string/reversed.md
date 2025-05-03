## Python 反轉字串的方法

**最簡單且常用的方法是使用切片：**

```python
s = "Hello Python"
reversed_s = s[::-1]
print(reversed_s)  # 輸出：nohtyP olleH
```
這種寫法簡潔且效率高[2][5][8]。

**其他常見方法：**

- 使用 `reversed()` 函式再用 `join()` 合併：
  ```python
  s = "Hello Python"
  reversed_s = ''.join(reversed(s))
  print(reversed_s)
  ```
- 迴圈累加反向字元：
  ```python
  s = "Hello Python"
  reversed_s = ""
  for c in s:
      reversed_s = c + reversed_s
  print(reversed_s)
  ```
- 轉成 list 用 `reverse()`，再用 `join()`：
  ```python
  s = "Hello Python"
  l = list(s)
  l.reverse()
  reversed_s = ''.join(l)
  print(reversed_s)
  ```

**總結**  
最推薦用 `s[::-1]`，簡單又直觀。