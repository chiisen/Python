# Python
Python 進階實戰開發

---

# 讓 code-runner 輸出到 Terminal
GitHub Copilot 只有 `#terminalLastCommand`  
無法取得 【輸出】視窗的訊息  
所以調整 `code-runner.runInTerminal`  
方便分析錯誤，不用複製貼上，省麻煩。  

## 設定預設終端機
```shell
terminal.integrated.defaultProfile
```
`Command Prompt` 是 `cmd.exe`  
`PowerShell` 是 `PowerShell 7.5.1`  

---

## 判斷是否是 Python 程式碼的方法
可以從以下幾點判斷：
1. 使用了 Python 風格的註解（以 `#` 開頭）
2. 使用了 Python 的列表推導式（list comprehension）：`[random.choice(...) for i in range(6)]`
3. 使用了 Python 的內建函數 `range()`
4. 變數命名和函數定義風格符合 Python 的慣例 `def `、變數命名前面不須型別宣告

---

## 查看所有已安装的包
```shell
pip list
```

---

## 常見問題

**題目一：類變數與實例變數的區別與行為**

```python
class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)
```

**答案與解析：**

輸出結果為：

```
1 1 1
1 2 1
3 2 3
```

解析：  
- `Parent.x` 是類變數，所有子類在未覆寫前都會共用這個變數。
- 當 `Child1.x = 2` 時，`Child1` 類自己有了 `x`，不再繼承自 `Parent`。
- 當 `Parent.x` 改為 3，`Child2` 沒有自己的 `x`，所以會跟著 `Parent` 變成 3，而 `Child1.x` 因為已經被覆寫，所以還是 2[1]。

---

**題目二：Python 除法運算的差異**

```python
def div1(x, y):
    print("%s/%s = %s" % (x, y, x/y))

def div2(x, y):
    print("%s//%s = %s" % (x, y, x//y))

div1(5, 2)
div1(5., 2)
div2(5, 2)
div2(5., 2.)
```

**答案與解析：**

在 Python 3 中，輸出為：

```
5/2 = 2.5
5.0/2 = 2.5
5//2 = 2
5.0//2.0 = 2.0
```

解析：  
- `/` 是浮點除法，不論參數是否為整數，結果都會是浮點數。
- `//` 是地板除法，會回傳不大於結果的最大整數（若有浮點則回傳浮點數）[1]。

---

**題目三：列表切片超出範圍的行為**

```python
lst = ['a', 'b', 'c', 'd', 'e']
print(lst[10:])
```

**答案與解析：**

輸出結果為：

```
[]
```

解析：  
- 列表切片時，如果起始索引超出列表長度，Python 只會回傳空列表，不會丟出 IndexError。
- 只有直接訪問不存在的索引（如 `lst[10]`）才會報錯。

---

## 將 JSON 字串轉為 Python 物件（dict）
[json_loads.md](./docs/json/json_loads.md)  
[json_loads.py](./src/json/json_loads.py)  

## 清除字串後面空格
[rstrip.md](./docs/string/rstrip.md)  
[rstrip.py](./src/string/rstrip.py)  

## 反轉字串的方法
[rstrip.md](./docs/string/reversed.md)  
[rstrip.py](./src/string/reversed.py)  

## 寫 array object 的方式
[array_object.md](./docs/array/array_object.md)  
[array_object.py](./src/array/array_object.py)  

## 用 get/set 控制網頁 session（以 Django 為例）
[用 get/set 控制網頁 session（以 Django 為例）](./docs/session.md)  

## 避免使用者辨識時混淆
[避免使用者辨識時混淆](./docs/generate_random_specify_code.md)  

## 資料庫中檢查資料是否存在
[資料庫中檢查資料是否存在](./docs/check_group_id_duplicate.md)  

## 背景執行
[背景執行](./docs/daemonize.md)  

## 架構分析
[架構分析](./docs/sa.md)  
[架構分析2](./docs/sa2.md)  

## 套件分析
[套件分析](./docs/import.md)  
[套件分析2](./docs/import2.md)  