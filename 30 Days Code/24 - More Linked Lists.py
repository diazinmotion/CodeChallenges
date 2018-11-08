class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 


class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  

    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        cur = head
        while cur != None and cur.next != None:
            while cur.next != None and cur.data == cur.next.data:
                cur.next = cur.next.next
            cur = cur.next

        return head

if __name__ == '__main__':
    mylist= Solution()
    T=int(input())
    head=None
    for i in range(T):
        data=int(input())
        head=mylist.insert(head,data)    
    head=mylist.removeDuplicates(head)
    mylist.display(head); 