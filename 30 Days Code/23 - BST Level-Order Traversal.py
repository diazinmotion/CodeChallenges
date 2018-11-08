import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self, root):
        # stack untuk menyimpan reference class
        ref_bst = []

        # untuk root BST
        ref_bst.insert(0, root)

        result = []
        while ref_bst:
            # dapatkan data reference di atasnya dan hapus setelahnya
            node = ref_bst.pop()
            result.append(node.data)

            # bila node kiri tidak kosong (ada referene)
            if node.left:
                ref_bst.insert(0, node.left)

            # bila node kanan tidak kosong (ada referene)
            if node.right:
                ref_bst.insert(0, node.right)

        # print hasil
        print(*result, sep=' ')


if __name__ == '__main__':
    T=int(input())
    myTree=Solution()
    root=None
    for i in range(T):
        data=int(input())
        root=myTree.insert(root,data)
    myTree.levelOrder(root)
