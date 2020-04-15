# -*- coding: utf-8 -*-

def document_it(func):
    def new_function(*args, **kwargs):
        print("running func:", func.__name__)
        print("input args:", args)
        results = func(*args, **kwargs)
        print("results:", results)
        return results
    return new_function

# デコレータ。
@document_it
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

ranger = my_range(1, 5)

print("type of ranger is.. ", type(ranger))


# mainで定義した変数はグローバル変数になる。ローカルからも参照可能に。
animal = "doggy"

def print_global():
    print("from inside:", animal)
#    animal = "bat" # error
print_global()

