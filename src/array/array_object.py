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
