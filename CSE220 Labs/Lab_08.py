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

    def Height(self):

        if self.left and self.right:
            return 1 + max(self.left.Height(), self.right.Height())

        elif self.left:
            return 1 + self.left.Height()

        elif self.right:
            return 1 + self.right.Height()

        else:
            return 1

    def PreOrder(self):

        print(self.data, end=' ')

        if self.left:
            self.left.PreOrder()

        if self.right:
            self.right.PreOrder()


    def InOrder(self):

        if self.left:
            self.left.InOrder()
        
        print(self.data, end=' ')

        if self.right:
            self.right.InOrder()


    def PostOrder(self):

        if self.left:
            self.left.PostOrder()

        if self.right:
            self.right.PostOrder()

        print(self.data, end=' ')

    def level_of_node(self, data, level):

        if self.left:
            TreeNode.level_of_node(self.left, data, level+1)

        if self.right:
            TreeNode.level_of_node(self.right, data, level+1)     
        
        if self.data == data:
            print(level)

    def sort_arr(self):

        if self.left:
            self.left.sort_arr()
        
        TreeNode.arr.append(self.data)
        

        if self.right:
            self.right.sort_arr()

    def compare_Trees(self, x, y):
        

        if x == y:
            print(True)
        
        else:
            print(False)

#-----------Tester-----------#

root = TreeNode(12)
root.add_child(6)
root.add_child(3)
root.add_child(7)
root.add_child(15)

root_2 = TreeNode(12)
root_2.add_child(6)
root_2.add_child(3)
root_2.add_child(7)
root_2.add_child(16)

print('Height ->')
print(root.Height())

print('\nPre-Order ->')
root.PreOrder()
print()
print('\nIn-Order ->')
print(root.InOrder())
print()
print('\nPost-Order ->')
root.PostOrder()
print()

x = int(input('\nEnter node value: '))
print(f'Level of Node {x}: ')
root.level_of_node(x, 1)

print('\nComparing Trees: ')
root.sort_arr()
x = TreeNode.arr
TreeNode.arr = []

root_2.sort_arr()
y = TreeNode.arr

root.compare_Trees(x,y)