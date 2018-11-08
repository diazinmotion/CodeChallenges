from math import sqrt

def isPrime(n):
    if n < 2:
        return False
    i = 2
    while i <= int(sqrt(n)):
        if n % i == 0:
            return False
        i += 1
    return True

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        data=int(input())
        msg = 'Prime' if isPrime(data) else 'Not prime'
        print(msg)
            