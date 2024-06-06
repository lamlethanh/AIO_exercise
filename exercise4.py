import math

def is_number(x):
    try:
        int(x.replace('.', '', 1))
    except ValueError:
        return False
    return True

def cal_sin(x,n):
    arr = []
    for i in range(0,n+1):
        temp = pow(-1, i)*(pow(x, 2*i+1)/math.factorial(2*i+1))
        arr.append(temp)
    return(sum(arr))
    
def cal_cos(x,n):
    arr = []
    for i in range(0,n+1):
        temp = pow(-1, i)*(pow(x, 2*i)/math.factorial(2*i))
        arr.append(temp)
    return(sum(arr))

def cal_sinh(x,n):
    arr = []
    for i in range(0,n+1):
        temp = pow(x, 2*i+1)/math.factorial(2*i+1)
        arr.append(temp)
    return(sum(arr))

def cal_cosh(x,n):
    arr = []
    for i in range(0,n+1):
        temp = pow(x, 2*i)/math.factorial(2*i)
        arr.append(temp)
    return (sum(arr))

x, n = input().split()
if (is_number(x) and is_number(n) and int(n) > 0):
    n = int(n)
    x = float(x)
    print(cal_sin(x,n))
    print(cal_cos(x,n))
    print(cal_sinh(x,n))
    print(cal_cosh(x,n))
else:
    print('x and n must be a number and n > 0')
    
    