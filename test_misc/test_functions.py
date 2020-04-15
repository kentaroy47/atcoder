
# 戻り値なしで関数内でresultsを持つ。
# 関数の定義。ここで初期化される。
def has_results(arg, results=[]):
    results.append(arg)
    print(results)
    
def has_results_return(arg, results=[]):
    results.append(arg)
    print(results)
    return results

# ここでは関数を呼び出しているだけ。初期値はもう入っている！
for i in range(10):
    print("戻りなし")
    has_results(i)
for i in range(10):
    print("戻りあり")
    has_results_return(i)

"""
戻りなし
[0]
戻りなし
[0, 1]
戻りなし
[0, 1, 2]
戻りなし
[0, 1, 2, 3]
戻りなし
[0, 1, 2, 3, 4]
戻りなし
[0, 1, 2, 3, 4, 5]
戻りなし
[0, 1, 2, 3, 4, 5, 6]
戻りなし
[0, 1, 2, 3, 4, 5, 6, 7]
戻りなし
[0, 1, 2, 3, 4, 5, 6, 7, 8]
戻りなし
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
戻りあり
[0]
戻りあり
[0, 1]
戻りあり
[0, 1, 2]
戻りあり
[0, 1, 2, 3]
戻りあり
[0, 1, 2, 3, 4]
戻りあり
[0, 1, 2, 3, 4, 5]
戻りあり
[0, 1, 2, 3, 4, 5, 6]
戻りあり
[0, 1, 2, 3, 4, 5, 6, 7]
戻りあり
[0, 1, 2, 3, 4, 5, 6, 7, 8]
戻りあり
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

# イミュータブルなデフォルト値だと毎回デフォルトが入っている？？
def test_func(arg, results=1):
    if arg > 10:
        results = 10
    print(results)

test_func(5)
test_func(11)
test_func(5)
"""
1
10
1
"""

# イミュータブル..int型の実数など
a = 1
print(a.real)
a.real=10 # エラーを吐く。変更できないから変数を再定義する必要がある。

class Person:
    def __init__(self, name, year):
        self.name = name
        self.year = year

person = Person('yaruo', 10)
print(person.name)
print(person.year)

# 変更できた -> mutable
person.name = 'yarumi' 
person.year = 30
print(person.name)
print(person.year)