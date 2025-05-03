# 清除字串後面空格

要清除字串**後面**的空格，可以使用 Python 的 `rstrip()` 方法：

```python
s = "Hello world   "
s = s.rstrip()
print(s)  # 結果：'Hello world'
```

`rstrip()` 只會移除字串**結尾**的空白，不會影響前面的內容。




