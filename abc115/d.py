def const(inb):
    outb='B' + inb + 'P' + inb + 'B'
    return(outb)

def burger(N, X):
    # construct burger
    for n in range(N+1):
        if n == 0:
            output='P'
        else:
            output = const(output)
    print(output)
    # calculate how many eaten
    count = 0
    for i, e in enumerate(range(X)):
        end = len(output)-1
        if end-i < 0:
            break
        if output[end-i] == 'P':
            count += 1
    return count

N = 2
X = 7
exp = 4
out = burger(N, X)
if out == exp:
   print("GOT it right. answer:{}, exp:{}", out, exp) 
else:
   print("Wrong. answer:{}, exp:{}", out, exp) 
   
N = 1
X = 1
exp = 0
out = burger(N, X)
if out == exp:
   print("GOT it right. answer:{}, exp:{}", out, exp) 
else:
   print("Wrong. answer:{}, exp:{}", out, exp) 

N = 50
X = 4321098765432109
exp = 2160549382716056
out = burger(N, X)
if out == exp:
   print("GOT it right. answer:{}, exp:{}", out, exp) 
else:
   print("Wrong. answer:{}, exp:{}", out, exp) 