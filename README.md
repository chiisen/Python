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

## 避免使用者辨識時混淆
[避免使用者辨識時混淆](./docs/generate_random_specify_code.md)  

## 資料庫中檢查資料是否存在
[資料庫中檢查資料是否存在](./docs/check_group_id_duplicate.md)  

## 背景執行
```python
from flask import Flask
from flask_apscheduler import APScheduler

def daemon_start():
    _notify_logger.info('== Restart API Service ==')
    # daemonize('/dev/null', '/tmp/daemon.log', '/tmp/daemon.log')
    if platform.system() != 'Windows': # 如果不是 Windows 系統（即在 Linux/Unix），可以用 daemonize 將服務變成背景行程，並將標準輸入、輸出、錯誤都導向 /dev/null，避免干擾終端機。
        daemonize(stdin='/dev/null', 
                 stdout='/dev/null',
                 stderr='/dev/null')  # context = (cer, key)
    app.run(
        host='0.0.0.0',
        port=5555,
        # ssl_context=context,
        debug=True,
        threaded=True,
        use_reloader=False  # 修正參數名稱應為 use_reloader
    )
```
啟動 Flask 等 Web 應用，監聽所有網路介面（0.0.0.0），port 設為 5555。  

threaded=True：支援多執行緒處理請求。  

debug=True：開啟除錯模式（開發時用）。  

use_reloader=False：不自動重新載入程式碼。  

ssl_context 可選，若啟用則支援 HTTPS。  

總結  
此程式設計用來啟動 API 服務，並可選擇以 daemon（背景行程）方式執行，且可設定 log 輸出位置與 HTTPS。  

實際啟動時會監聽在 0.0.0.0:5555，支援多執行緒與除錯模式。  

註解部分提供進階用法（如 log、SSL、daemonize）供參考。  

## 架構分析
