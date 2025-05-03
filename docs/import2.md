# 套件分析

以下說明各底層模組的用途：

---

**1. from daemon import daemonize**

- 用於將 Python 程式「守護化」（daemonize），讓程式在背景以守護行程（daemon process）方式執行，常用於服務型應用或長時間執行的任務。

**2. from signal import SIGTERM**

- 匯入 SIGTERM 訊號，用於程式終止時的訊號處理。SIGTERM 是一種標準訊號，可讓程式收到「要求正常終止」的通知，常用於優雅（graceful）關閉守護行程或服務。

**3. from os import listdir**

- 匯入 listdir 函式，用來取得指定目錄下所有檔案與資料夾的名稱清單，常用於目錄瀏覽或檔案管理。

**4. from flask import Flask, jsonify, request, make_response, redirect**

- 匯入 Flask 相關物件與工具：
    - `Flask`：建立 Flask 應用主體。
    - `jsonify`：將資料轉為 JSON 格式回傳。
    - `request`：存取 HTTP 請求內容（如參數、表單、標頭等）。
    - `make_response`：自訂 HTTP 回應內容。
    - `redirect`：產生 HTTP 重導向回應。

**5. from flask_restful import Resource, Api**

- 匯入 Flask-RESTful 的資源類別與 API 管理器：
    - `Resource`：定義 RESTful API 的資源與行為（如 GET、POST 方法）。
    - `Api`：將 Resource 註冊到 Flask 應用，統一管理 API 路由。

**6. from flask_mail import Mail, Message**

- 匯入 Flask-Mail 的郵件物件：
    - `Mail`：設定並初始化郵件伺服器連線。
    - `Message`：建立郵件內容（主旨、收件人、內容等），用於發送 email。

---

**總結**
這些模組分別用於：

- 守護行程管理（daemonize, SIGTERM）
- 檔案目錄操作（listdir）
- Web 應用與 API 開發（Flask, flask_restful）
- 郵件發送（flask_mail）
