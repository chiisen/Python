# Python
Python 進階實戰開發

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

## 判斷是否是 Python 程式碼的方法
可以從以下幾點判斷：
1. 使用了 Python 風格的註解（以 `#` 開頭）
2. 使用了 Python 的列表推導式（list comprehension）：`[random.choice(...) for i in range(6)]`
3. 使用了 Python 的內建函數 `range()`
4. 變數命名和函數定義風格符合 Python 的慣例 `def `、變數命名前面不須型別宣告

## 查看所有已安装的包
```shell
pip list
```

## 將 JSON 字串轉為 Python 物件（dict）
[json_loads.md](./docs/json/json_loads.md)  
[json_loads.py](./src/json/json_loads.py)  

# 清除字串後面空格
[rstrip.md](./docs/string/rstrip.md)  
[rstrip.py](./src/string/rstrip.py)  

## 反轉字串的方法
[rstrip.md](./docs/string/reversed.md)  
[rstrip.py](./src/string/reversed.py)  

## 寫 array object 的方式
[array_object.md](./docs/array/array_object.md)  
[array_object.py](./src/array/array_object.py)  

## 用 get/set 控制網頁 session（以 Django 為例）

在 Django 網頁後端開發中，可以直接透過 `request.session` 這個類似字典的物件來**存取（get）與設定（set）session 資料**：

- **取得 session 值（get）：**
  ```python
  my_car = request.session.get('my_car', 'mini')  # 若沒設定過則預設為'mini'
  ```

- **設定 session 值（set）：**
  ```python
  request.session['my_car'] = 'mini'
  ```

- **刪除 session 值：**
  ```python
  del request.session['my_car']
  ```

這些操作只會影響目前用戶（瀏覽器）的 session 資料，安全且簡單，和操作 dict 幾乎一樣。

##　避免使用者辨識時混淆
[避免使用者辨識時混淆](./docs/generate_random_specify_code.md)  


