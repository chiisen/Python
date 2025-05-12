# uv 安裝
uv 本身並不需要 Python，所以不建議用 pip 或是 pipx 安裝，這樣都會跟特定的 Python 環境綁在一起，Windows 上就直接透過 PowerSehll 安裝即可：
```shell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
或是透過 scoop 等軟體管理工具安裝:
```shell
scoop install uv
```

## 使用 uv 管理多個 Python 環境版本
顯示可安裝以及已安裝的 Python 版本：
```shell
uv python list
```
安裝最新版本:
如果已經安裝過 Python，除非額外指定版本，否則就不會安裝
```shell
uv python install
```
指定安裝特定的版本：
```shell
uv python install 3.10
```
安裝 Python 時也可以同時指定多個版本：
```shell
uv python install 3.10 3.11
```
找到 Python 的安裝路徑：
```shell
uv python dir
```
移除已經安裝的 Python:
```shell
uv python uninstall 3.10
```
移除 Python 時也可以同時指定多個版本：
```shell
uv python uninstall 3.10 3.11
```

# 使用 uv 替代 python/pip 工具
uv 管理的 Python 環境並不能直接透過 python 指令執行，必須透過 uv 來執行。
```shell
uv run .\src\show_version.py
```
執行時透過 --python 引數指定 Python 版本：
```shell
uv run --python 3.10 .\src\show_version.py
```