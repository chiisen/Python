```python
import random

def generate_random_specify_code():
    # use in illegle and unlock method.
    rand_code = [random.choice('23456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ') for i in range(6)]
    gen_num = ''.join(rand_code)
    return gen_num
```
問題：「其中少了[1,l,0]，為什麼？」

答案
產生隨機驗證碼時，random.choice() 選用的字元字串是
'23456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'，
裡面沒有 1、l、0 這三個字元。

原因：
這是為了避免驗證碼辨識時產生混淆。

數字 1 和小寫 l（L）、大寫 I（i）、數字 0 和大寫 O（o）在某些字型下很容易看錯。

所以設計驗證碼時，常會把這些容易混淆的字元排除。

結論：
少了 [1, l, 0]，是為了避免使用者辨識時混淆，提升驗證碼的易讀性與正確性。