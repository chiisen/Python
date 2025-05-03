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
