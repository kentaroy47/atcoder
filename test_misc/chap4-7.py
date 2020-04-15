
# *argsにするとタプルで受けられる
def print_args(*args):
    print("Positional argument tuple:", args)
    
print_args()

print_args(3, 2, 1, "wait!", "hmmmm")

# **argsにすると辞書が作れる
def print_kwargs(**kwargs):
    '''
    docstring.
    関数の最初に文字列を入れてドキュメントをすること。大事やで。
    '''
    print("keyword args:", kwargs)
    return kwargs
    
print_kwargs()
kwargs = print_kwargs(wine="merlot", entree="mutton", dessert="donought!")

# helpでdocstringは読み出せる！
'''
help(print_kwargs)
Help on function print_kwargs in module __main__:

print_kwargs(**kwargs)
    docstring.
    関数の最初に文字列を入れてドキュメントをすること。大事やで。
'''

print_kwargs()