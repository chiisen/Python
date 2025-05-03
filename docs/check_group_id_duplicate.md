## 資料庫中檢查資料是否存在
```python
def check_group_id_duplicate(group_id):
    found = False
    query = "SELECT group_id FROM group_info WHERE group_id = %s;"
    value = (group_id,)
    center_logger.info('_CHECK_GROUP_ID_DUPLICATE:' + query % value)
    cursor = sql.run_sql(query, value)
    rows = cursor.fetchone()
    if rows is not None:
        found = True
    return found
```
程式功能說明：  
此函式用於檢查資料庫中 group_info 表是否已存在特定 group_id，若存在返回 True，否則返回 False。使用參數化查詢防止 SQL injection，並通過 center_logger 記錄檢查日誌。
