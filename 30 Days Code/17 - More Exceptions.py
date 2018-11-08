class Calculator:
    def power(self, n, p):
        if n >= 0 and p >= 0:
            result = n**p
        else:
            err = ValueError("n and p should be non-negative")
            raise err

        return result


if __name__ == '__main__':
    myCalculator=Calculator()
    T=int(input())
    for i in range(T):
        n,p = map(int, input().split())
        try:
            ans=myCalculator.power(n,p)
            print(ans)
        except Exception as e:
            print(e)   