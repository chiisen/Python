import json
from termcolor import colored
# pip install termcolor
# 要让 Python 输出的 JSON 有格式化且带有颜色差异标注的功能，你可以结合json模块来格式化 JSON 数据，再使用termcolor库添加颜色。


from colorama import init, Fore, Back, Style
# pip install colorama
# colorama库能让你在 Windows、Linux 等不同系统下都可以方便地使用 ANSI 转义序列来输出彩色文本。

# 初始化 colorama
init(autoreset=True)

# 输出不同颜色的文本
print(Fore.RED + '这是红色的文本')
print(Fore.GREEN + '这是绿色的文本')
print(Fore.BLUE + '这是蓝色的文本')

# 背景颜色和样式示例
print(Back.YELLOW + Fore.BLACK + '这是黄色背景黑色文本')
print(Style.BRIGHT + '这是明亮样式的文本')


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

print(Back.YELLOW + Fore.BLACK + '# 將 JSON 字串轉為 Python 物件（dict）')
print(Back.YELLOW + Fore.BLACK + '# 最常見的情境是將 JSON 格式的字串轉換為 Python 物件（通常是 dict）。做法如下：')

json_str = '{"id": 123, "Name": "wsrsw", "Email": "wsrsw@example.com"}'
obj = json.loads(json_str)
print(colored_json(obj))         # {'id': 123, 'Name': 'wsrsw', 'Email': 'wsrsw@example.com'}
print(type(obj))   # <class 'dict'>


print(Back.YELLOW + Fore.BLACK + '# 這樣就能將字串轉成 Python 的物件（dict）來操作。')

print(Back.YELLOW + Fore.BLACK + '# 補充：如果你要將 Python 物件轉回字串（JSON 格式），可用 json.dumps() 方法。')

json_str = json.dumps(obj)
print(json_str)