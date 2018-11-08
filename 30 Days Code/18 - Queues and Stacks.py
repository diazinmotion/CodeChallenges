class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, ch):
        self.stack.append(ch)

    def enqueueCharacter(self, ch):
        self.queue.append(ch)

    def popCharacter(self):
        # stack is LIFO (Last In First Out)
        # so, we remove the last index of the array
        len_arr = (len(self.stack) - 1)
        top_ch = self.stack[len_arr]
        self.stack.pop(len_arr)

        return top_ch
        
    def dequeueCharacter(self):
        # queue is FIFO (First in First Out)
        # so, we remove the first index of the array
        fst_ch = self.queue[0]
        self.queue.pop(0)

        return fst_ch
    

if __name__ == '__main__':
    # read the string s
    s=input()
    #Create the Solution class object
    obj=Solution()   

    l=len(s)
    # push/enqueue all the characters of string s to stack
    for i in range(l):
        obj.pushCharacter(s[i])
        obj.enqueueCharacter(s[i])
        
    isPalindrome=True
    '''
    pop the top character from stack
    dequeue the first character from queue
    compare both the characters
    ''' 
    for i in range(l // 2):
        if obj.popCharacter()!=obj.dequeueCharacter():
            isPalindrome=False
            break
    #finally print whether string s is palindrome or not.
    if isPalindrome:
        print("The word, "+s+", is a palindrome.")
    else:
        print("The word, "+s+", is not a palindrome.")    