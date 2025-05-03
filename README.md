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

