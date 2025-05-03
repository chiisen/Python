import json
from termcolor import colored

def colored_json(data):
    # 將 JSON 格式的字串轉換為 Python 物件（dict）
    # 並將其格式化為彩色輸出
    formatted_json = json.dumps(data, indent=4)
    output = ""
    for line in formatted_json.splitlines():
        if line.strip().startswith('"'):
            # 键
            line = colored(line, 'green')
        elif line.strip().startswith('[') or line.strip().startswith('{'):
            # 开始符号
            line = colored(line, 'cyan')
        elif line.strip().startswith(']') or line.strip().startswith('}'):
            # 结束符号
            line = colored(line, 'cyan')
        elif line.strip().startswith(' ' * 4 + '"'):
            # 值
            line = colored(line, 'yellow')
        output += line + '\n'
    return output

# 陣列中放 dict
arr = [
    {"id": 1, "name": "Amy"},
    {"id": 2, "name": "Bob"}
]

# 陣列中放自訂 class 物件
class Person:
    def __init__(self, name):
        self.name = name

# arr = [Person("Amy"), Person("Bob")]
# TypeError: Object of type Person is not JSON serializable

#這是因為 json.dumps() 預設無法序列化自訂的 class 物件（如 Person），只能處理內建型別（如 dict、list、str、int 等）。你傳給 colored_json(arr) 的 arr 是 Person 物件的 list，導致無法序列化。

#解決方式： 你需要將 Person 物件轉換成 dict，例如：
arr = [vars(p) for p in [Person("Amy"), Person("Bob")]]

print("1. 使用 list（最常用）\n" + colored_json(arr))


from array import array
arr = array('i', [1, 2, 3, 4])  # 'i' 代表整數
print("2. 使用 array 模組（只適合數值型）\n" + str(arr))  # array('i', [1, 2, 3, 4])


import numpy as np
arr = np.array([1, 2, 3, 4])
print("3. 使用 NumPy 陣列（科學運算常用）\n" + str(arr))  # [1 2 3 4]