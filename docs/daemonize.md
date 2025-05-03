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