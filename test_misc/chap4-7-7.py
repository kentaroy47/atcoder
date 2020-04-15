# -*- coding: utf-8 -*-

# 全てのものはオブジェクト。関数もオブジェクトである。

def answer():
    print(42)

def runstuff(func):
    func()
    
runstuff(answer)
print(type(answer))

def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)

a = knights("Ho!")
b = knights("Ha!")

# 関数内で生成されたオブジェクトはその関数（クラス）固有のものとなる。
# 同じ関数を呼んでも上書きされない

print(a)
print(b)
"""
We are the knights who say: 'Ho!'
We are the knights who say: 'Ha!'
"""

def enliven(word):
    return word.capitalize() + "!"

def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ["thud", "bow", "mow", "dud"]

edit_story(stairs, enliven)

# lambdaは一行の関数と等価。
# 普通に関数を書いたほうが読みやすいが。。
edit_story(stairs, lambda word: word.capitalize() + "!")

