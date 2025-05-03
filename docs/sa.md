若目前公司開發的系統中的資料庫（Ex: MySQL）需開放 API/CGI 讓外部部門程式存取，請說明應如何做，請描述架構、流程或做法，文長建議精簡程式語言請自選，為什麼？：

---

# CGI是什麼？

CGI（Common Gateway Interface，通用閘道介面）是一種網頁伺服器與外部應用程式（如腳本或程式）之間的標準介面。
它的主要功能是**讓網頁伺服器能夠呼叫外部程式，動態產生網頁內容**，而不是只回傳靜態的 HTML 檔案。

---

## 主要原理與用途

- 當使用者在瀏覽器發送請求（如填寫表單、投票、留言等），Web 伺服器會根據請求呼叫對應的 CGI 程式。
- CGI 程式收到請求資料後，進行處理（如查詢資料庫、寫入檔案），再將結果（通常是 HTML）回傳給伺服器，最後由伺服器回應給使用者。
- 常見留言板、討論區、線上表單等動態網頁功能，早期多以 CGI 實現。

---

## 特點

- **動態網頁技術的早期標準**：CGI 是最早讓網頁可以互動、動態產生內容的技術。
- **語言不限**：CGI 程式可以用多種語言撰寫（如 Perl、Python、C 等）。
- **一次請求一個行程**：每次請求都會啟動一個新的 CGI 程式行程，效率較低，但實現簡單。

---

## 簡單總結

CGI 就是**讓 Web 伺服器和外部程式溝通的橋樑**，使網頁能根據用戶輸入產生動態內容，是動態網頁的基礎技術之一。

---

## 架構說明

1. **三層式架構（建議）**  
   - 外部部門**不直接連線資料庫**，而是透過 API/CGI 介面進行資料存取。
   - 架構如下：
     - **前端/外部部門系統**（Client）：發送 HTTP 請求。
     - **API/CGI 伺服器**（中介層）：負責接收請求、驗證權限、處理業務邏輯，並與資料庫互動。
     - **資料庫（MySQL）**：僅允許 API 伺服器存取，對外部部門不開放。

2. **流程說明**
   - 外部部門系統透過 HTTP(S) 請求（如 RESTful API）呼叫公司提供的 API。
   - API 伺服器驗證請求（如 API Key、Token、OAuth）。
   - 通過驗證後，API 伺服器執行對資料庫的查詢或更新，並將結果以 JSON/XML 回傳給外部部門。
   - API 伺服器可記錄存取 log、限制流量、處理異常。

3. **安全性與維護性**
   - 資料庫不對外開放，減少資安風險。
   - API 可控權限、統一格式、易於維護與擴充。
   - 可加密傳輸（HTTPS），確保資料安全。

---

## 範例程式（Python Flask）

```python
# API 伺服器：Flask 範例
from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

@app.route('/get_data', methods=['GET'])
def get_data():
    # 權限驗證（簡易範例）
    token = request.headers.get('Authorization')
    if token != 'your_api_token':
        return jsonify({'error': 'Unauthorized'}), 401

    # 連線資料庫
    conn = pymysql.connect(host='localhost', user='user', password='pwd', db='dbname')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM table WHERE id=%s", (request.args.get('id'),))
    result = cursor.fetchone()
    conn.close()
    return jsonify({'data': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

---

## 為什麼這樣設計？

- **安全**：資料庫不直接對外開放，避免被攻擊或誤操作。
- **權限控管**：API 可針對不同部門設計不同權限與存取日誌。
- **維護性高**：API 介面統一，易於修改與擴充，不影響資料庫結構。
- **可擴展**：未來可根據需求增加認證、流量控制、錯誤處理等功能。

---

## 總結

**推薦做法是建立 API/CGI 中介層，讓外部部門透過標準協定（如 HTTP/REST）間接存取資料庫，確保安全、可控、易於維護與擴充。**