# 定執行時需要的套件
uv 提供有便捷的方式，你可以透過 --with 選項指定套件：
```shell
uv run --with cowsay .\src\cow.py
```
uv 會建立一個臨時的虛擬環境，即時下載安裝指定的套件。

如果想知道這個虛擬環境建置在哪裡：
```shell
uv cache dir
```

把臨時建立的虛擬環境清除：
```shell
uv cache clean
```

如果需要多個套件，例如以下這個同時需要 cowsay 與 rich 套件的程式：
```shell
uv run --with cowsay,rich .\src\cow_rich.py
```
執行時就可以用逗號隔開指定需要的套件。
或者也可以重複使用 --with 選項：
```shell
uv run --with cowsay --with rich .\src\cow_rich.py
```
你也可以同時指定套件的版本（由於 < 是轉向的符號，為避免 PowerShell 解譯錯誤，記得加上前後的單引號將套件名稱與版本條件包起來）：
```shell
uv run --with 'cowsay>6,<7,rich' .\src\cow_rich.py
```