class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        result = []
        data_len = len(self.__elements)

        for i in range(data_len):
            for n in range(i, data_len):
                if i == n:
                    continue

                x = self.__elements[i]
                y = self.__elements[n]
                
                # calculate the absolute value and push it into resul
                result.append(abs(x - y))

        self.maximumDifference = max(result)

if __name__ == '__main__':
    _ = input()
    a = [int(e) for e in input().split(' ')]

    d = Difference(a)
    d.computeDifference()

    print(d.maximumDifference)