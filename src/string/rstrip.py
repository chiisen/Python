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

s = "Hello world   "
s = s.rstrip()
print(Back.YELLOW + Fore.BLACK + s)  # 結果：'Hello world'