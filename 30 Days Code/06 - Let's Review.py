class StrFormatter:
    def __init__(self, strInput):
        try:
            self.userInput = strInput
        except TypeError:
            raise TypeError("Type is not valid")
        
    def process(self):
        arrEven = []
        arrOdd = []
        
        arrWords = list(self.userInput)
        
        for i in range(len(arrWords)):
            # check if index is odd or even
            if (i == 0) or (i % 2 == 0):
                arrEven.append(arrWords[i])
            else:
                arrOdd.append(arrWords[i])
                
        print("".join(arrEven) + " " + "".join(arrOdd))
        
# main program
# TestCase number
n = int(input())

# test case constraint
if 1 <= n <= 10:
    arr_input = []
    for i in range(n):
        uInput = str(input())

        # string constraint
        jum_string = len(uInput)
        if 2 <= jum_string <= 10000:
            arr_input.append(uInput)

    # result
    for i in arr_input:
        sf = StrFormatter(i)
        sf.process()