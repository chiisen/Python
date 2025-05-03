## Python 字串轉物件方法

**將 JSON 字串轉為 Python 物件（dict）**

最常見的情境是將 JSON 格式的字串轉換為 Python 物件（通常是 dict）。做法如下：

```python
import json

json_str = '{"id": 123, "Name": "wsrsw", "Email": "wsrsw@example.com"}'
obj = json.loads(json_str)
print(obj)         # {'id': 123, 'Name': 'wsrsw', 'Email': 'wsrsw@example.com'}
print(type(obj))   # &lt;class 'dict'&gt;
```

這樣就能將字串轉成 Python 的物件（dict）來操作。

**補充：如果你要將 Python 物件轉回字串（JSON 格式），可用**

```python
json_str = json.dumps(obj)
```

**注意事項**

- 字串必須是有效的 JSON 格式，否則會報錯。
- 這種轉換常用於 API 資料處理、設定檔等情境。

**其他字串轉型態**

- 若只是將字串轉成數字，可用 `int()`、`float()`。
- 若要把字串轉成其他 Python 物件（如 list、tuple），可用 `eval()`，但有安全風險，建議只用於可信內容。

**常用方法整理**


| 需求 | 方法 | 範例 |
| :-- | :-- | :-- |
| JSON字串→dict | `json.loads()` | `json.loads('{"a":1}')` |
| dict→JSON字串 | `json.dumps()` | `json.dumps({'a':1})` |
| 字串→數字 | `int()`、`float()` | `int('123')`、`float('1.23')` |
| 字串→list/tuple等 | `eval()`（不建議） | `eval('[1][2][3]')` |

建議處理 JSON 格式時，優先使用 `json` 模組。