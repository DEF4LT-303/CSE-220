class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyList:

    def __init__(self, a=None):
        self.head = Node()                              # dummy node
        self.head.next = self.head.prev = self.head

        if a is None:
            return

        for val in a:
        
            if self.head.next is self.head:
                new_node = Node(val)

                new_node.next = self.head.next      # new node next links to dummy [maintains circularity]
                new_node.prev = self.head           # new node prev links to dummy
                self.head.next = new_node           # dummy next links to new node
                new_node.next.prev = new_node       # new node next (dummy) prev links to new node [maintains circularity - i guess?]


            else:
                n = self.head.next

                while n.next is not self.head:
                    
                    n = n.next

                new_node = Node(val)
                
                n.next = new_node
                new_node.prev = n
                new_node.next = self.head
                new_node.next.prev = new_node 
                
    def showList(self):

        if self.head.next.data is None:
            print('Empty List')
            return

        else:
            current = self.head.next
            final = ''

            while current is not self.head:
                
                if current.next is not self.head:
                    final += str(current.data) + ' => '

                else:
                    final += str(current.data)

                current = current.next
                
            print(final)
            print('Len =', self.nodeCounter())

    def nodeCounter(self):

        count = 0
        n = self.head.next

        while n is not self.head:

            n = n.next
            count += 1

        return count

    def insert(self, newElement, index=None):

        new_node = Node(newElement)

        n = self.head.next

        while n.next is not self.head:                         # check if value already exists
            
            if n.next.data == newElement or n.data == newElement:
                print('Value already exists!')
                return
            
            n = n.next

        if index is None:                                      # if index is not specified
            n = self.head.next

            while n.next is not self.head:               

                n = n.next
            
            n.next = new_node
            new_node.prev = n
            new_node.next = self.head
            new_node.next.prev = new_node

        elif index == 0:                                        # if index is 0

            new_node.next = self.head.next    
            new_node.prev = self.head           
            self.head.next = new_node           
            new_node.next.prev = new_node

        elif index == self.nodeCounter():                       # if index is the last index

            n = self.head.next

            while n.next is not self.head:
                
                n = n.next
            
            n.next = new_node
            new_node.prev = n
            new_node.next = self.head
            new_node.next.prev = new_node
        
        else:                                                   # if index is somewhere in the middle
            if index < 0 or index > self.nodeCounter():
                print('Invalid Index!')
                return

            else:
                n = self.head.next
                count = 0                                                  #-new_node-#
                                                               #           /         \
                while n.next is not self.head:                 #  <-- n --/           \-- q --> 

                    if count == index - 1:                       
                        q = n.next                               # stores next val address
                        new_node.next = q                        # sets new node next link to next val address
                        new_node.prev = n                        # sets new node prev link to prev val address
                        n.next = new_node                        # sets prev val next link to new node
                        q.prev = new_node                        # sets next val prev link to new node

                    n = n.next
                    count += 1

    def remove(self, index): 

        n = self.head.next
        count = 0

        if index < 0 or index >= self.nodeCounter():
            print('Invalid Index!')
            return
            
        while n.next is not self.head:

            if index == self.nodeCounter() - 1:
                n = self.head.prev      # going to the last node

                p = n.prev              # unlinking the last node
                p.next = self.head
                p.next.prev = p

                n.next = n.prev = None
                n.data = None

                break

            elif count == index:
                
                p = n.prev              # p = prev node
                q = n.next              # q = next node

                p.next = q              # removes link from given index
                q.prev = p

                n.next = n.prev = None
                n.data = None

                break

            n = n.next
            count += 1
        
    def removeKey(self, deletekey):

        n = self.head.next

        while n.next is not self.head:

            if deletekey == n.data:
                print('Deleted value:', n.data)
                deleted = n.data

                p = n.prev
                q = n.next

                p.next = q
                q.prev = p

                n.next = n.prev = None
                n.data = None

                return deleted

            n = n.next

        
#---------Tester-----------#           

source = [1,2,3,4,5]

lst = DoublyList(source)
lst.insert(50)
lst.insert(50,7)
lst.showList()
lst.remove(6)
lst.removeKey(5)
lst.showList()