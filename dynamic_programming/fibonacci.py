import time

def fib_basic(n):
    if n == 1 or n == 2:
        return 1
    
    return fib_basic(n-1) + fib_basic(n-2)

def fib_memo(n, dct):
    if n == 1 or n == 2:
        return 1
    
    if n in dct:
        return dct[n]
    else:
        value = fib_memo(n-1,dct) + fib_memo(n-2, dct)
        dct[n] = value
        return value

def fib_bottom(n):
    arr = [None for i in range(n+2)]
    arr[1] = 1
    arr[2] = 1
    for i in range(3, n+2):
        arr[i] = arr[i-1] + arr[i-2]
    
    return arr[n]



if __name__ == "__main__":
    n = 30
    start = time.time()
    value_basic = fib_basic(n)
    end = time.time()
    print("value_basic:", value_basic, "time:", end-start)
    start = time.time()
    value_memo = fib_memo(n,{})
    end = time.time()
    print("value_memo:", value_memo, "time:", end-start)
    start = time.time()
    value_bottom = fib_bottom(n)
    end = time.time()
    print("value_bottom:", value_bottom, "time:", end-start)
