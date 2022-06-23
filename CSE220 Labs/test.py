class TreeNode:

    arr = []

    def __init__(self, data=None):
        
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):

        if self.data is None:
            self.data = data

        if data == self.data:
            return

        if data < self.data:

            if self.left:
                self.left.add_child(data)

            else:
                self.left = TreeNode(data)

        else:
            
            if self.right:
                self.right.add_child(data)

            else:
                self.right = TreeNode(data)

    def find_pre(self, current):

        predecessor = current.left
        while predecessor.right is not None and predecessor.right != current:
            predecessor = predecessor.right
        
        return predecessor

    def InOrder(self):

        current = self

        while current is not None:

            if current.left is None:
                print(current.data, end=" ")
                current = current.right

            else:
                predecessor = self.find_pre(current)

                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left

                else:
                    predecessor.right = None
                    print(current.data, end=" ")
                    current = current.right


root = TreeNode(12)
root.add_child(6)
root.add_child(3)
root.add_child(7)
root.add_child(15)

print('\nIn-Order ->')
root.InOrder()
# print(TreeNode.arr)
