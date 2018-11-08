class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        # bila head kosong berarti list masih baru
        if head == None:
            # buat node baru
            head = Node(data)
        else:
            # bila head sudah ada, maka list sudah ada isinya
            # set head sebagai current object reference
            current = head

            # looping sampai dengan awal list
            # ditandai dengan current next == null
            while current.next != None:
                # set current obj ref sesuai dengan referece pada list sebelumnya
                current = current.next
                
            # buat node baru dan set sebagai reference berikutnya
            current.next = Node(data)

        return head

# main program
if __name__ == '__main__':
    mylist= Solution()
    T=int(input())
    head=None
    for i in range(T):
        data=int(input())
        head=mylist.insert(head,data)    
    mylist.display(head); 	 