# -*- coding: utf-8 -*-

def fib(N):
    if N == 0:
        return 0
    elif N == 1 or N == 2:
        return 1
    else:
        t1 = 1; t2 = 1;
        for i in range(N-2):
            tmp = t1+t2
            t1 = t2;
            t2 = tmp
        return tmp
    
def fib_rec(N):
    if N == 0:
            return 0
    elif N == 1 or N == 2:
        return 1
    else:
        return fib_rec(N-1) + fib_rec(N-2)

def fib_memo(N, no):
    memo=["EMPTY"]*(N+1)
    def _fib(N):
        if N == 0:
            return 1
        elif N == 1:
            return 1
        elif memo[N] != "EMPTY":
            return memo[N]
        elif N in no:
            memo[N] = 0
            return memo[N]
        else:
            memo[N] = _fib(N-1)+_fib(N-2)
            print("N",N)
            print(memo[N])
            return memo[N]
    return _fib(N)
            
no = [1, 23, 45, 67, 89]
print(fib_memo(100, no))
print(fib_memo(100, no) % (1e9+7))
#for i in range(100):
#    print(fib_memo(i))
    
            
            