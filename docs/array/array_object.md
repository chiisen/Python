## Python 寫 array object 的方式

**1. 使用 list（最常用）**

- Python 沒有內建 array 物件，通常直接用 list 來儲存多個物件或資料。
- 範例：建立一個物件陣列（每個元素都是 dict 或自訂 class）

```python
# 陣列中放 dict
arr = [
    {"id": 1, "name": "Amy"},
    {"id": 2, "name": "Bob"}
]

# 陣列中放自訂 class 物件
class Person:
    def __init__(self, name):
        self.name = name

arr = [Person("Amy"), Person("Bob")]
```

list 可存放任何型態的物件。

**2. 使用 array 模組（只適合數值型）**

- array 模組只能存放同型態的數值資料。
- 範例：

```python
from array import array
arr = array('i', [1, 2, 3, 4])  # 'i' 代表整數
```

適合需要大量數值運算且型態一致時使用。

**3. 使用 NumPy 陣列（科學運算常用）**

- NumPy 的 ndarray 支援多維陣列與高效運算。
- 範例：

```python
import numpy as np
arr = np.array([1, 2, 3, 4])
```

適用於大量數值、矩陣、科學計算。

---

**總結：**

- 一般物件陣列：用 list。
- 數值且型態一致：可用 array 模組或 NumPy。

