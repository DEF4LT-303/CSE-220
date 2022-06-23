class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class MyList:

    def __init__(self, a):
        self.head = None

        for i in a:                         # iterates list

            if self.head is None:           # if list is empty
                new_node = Node(i, None)
                self.head = new_node

            else:                           # if not empty, inserts list data at the end
                n = self.head
                while n.next:

                    n = n.next

                n.next = Node(i, None)
#----------------------------------------------#

    def showList(self):

        if self.head is None:
            print('Empty List')
            return

        else:
            current = self.head
            final = ''

            while current:

                if current.next is not None:
                    final += str(current.data) + ' => '

                else:
                    final += str(current.data)

                current = current.next

            print(final)
#----------------------------------------------#

    def isEmpty(self):

        bool = False
        if self.head is None:
            bool = True

        print(bool)
#----------------------------------------------#

    def clear(self):

        n = self.head

        while n:

            temp = n            # stores n in temp
            n = n.next          # updates n value to next n for iteration
            temp.next = None    # sets temp (aka n) address to null

        self.head = None        # sets head address to null
#----------------------------------------------#

    def insert(self, newElement, index=None):

        if index is None:                                             # if second parameter isnt provided
            if self.head is None:                                     # if list is empty
                new_node = Node(newElement, None)
                self.head = new_node
                return

            else:
                n = self.head
                while n.next:

                    if n.next.data == newElement or n.data == newElement:   # checks if value already present
                        print('Value already exists!')
                        return

                    n = n.next

                # appends at end if value is not present
                n.next = Node(newElement, None)

        # if second parameter is provided (index to insert)
        else:
            size = 0
            n = self.head

            while n:                                    # finding the size of linked list

                size += 1
                n = n.next

            if index < 0 or index > size:               # validating index
                print('Invalid Index!')

            elif index == 0:                            # inserting at the beginning
                new_node = Node(newElement, self.head)
                self.head = new_node                    # assigns it to head

            else:
                count = 0
                n = self.head

                while n:

                    if n.next is not None:                                      # if next address is not none, validates index
                        if n.next.data == newElement or n.data == newElement:
                            print('Value already exists!')
                            return

                    if count == index - 1:                                      # if count reaches value before index, inserts new element
                        new_node = Node(newElement, n.next)
                        n.next = new_node                                       # assigns next address to next address

                        break

                    n = n.next
                    count += 1
#----------------------------------------------#

    def remove(self, deleteKey):

        n = self.head
        index = 0
        while n.data != deleteKey:        # finds the index of value to be removed

            index += 1
            n = n.next

        value = None
        if index == 0:                    # if index is 0, updates head address to next address
            value = self.head.data
            self.head = self.head.next

        count = 0
        n = self.head
        while n:

            if count == index - 1:              # stops before the value to be removed
                value = n.next.data             # stores deleted value
                n.next = n.next.next            # updates address of deleted value to next address

                break

            count += 1
            n = n.next
        print('Deleted Value: ', value)

    def even_numbers(self):

        new_head = None
        n = self.head
        even = []                           # store the nums in array to pass it in the class

        while n:

            if n.data % 2 == 0:
                if new_head is None:        # prepend
                    new_node = Node(n.data, new_head)
                    new_head = new_node
                    

                else:                       # append
                    x = new_head
                    
                    while x.next:

                        x = x.next
                    
                    x.next = Node(n.data, None)
                    

            n = n.next

        n = new_head

        while n:                            # appends the data in array

            even.append(n.data)
            n = n.next

        MyList(even).showList()             # passes array to the class

    def is_present(self, data):

        bool = False
        n = self.head

        while n:

            if n.data == data:
                bool = True
                break

            n = n.next

        print(bool)



#-------------------Tester---------------------#


source = [1, 2, 3, 4, 5]
# source = []

my_list = MyList(source)
#------------------------------------------------------------#
print('showList():')
my_list.showList()
print("======================================================")
#------------------------------------------------------------#
print('isEmpty():')
my_list.isEmpty()
print("======================================================")
#------------------------------------------------------------#
print('clear():')
my_list.clear()
my_list.showList()
print("======================================================")
#------------------------------------------------------------#
print('insert(newElement):')
my_list.insert(6)
my_list.insert(7)
my_list.insert(8)
my_list.insert(9)
my_list.showList()
print("======================================================")
#------------------------------------------------------------#
print('insert(newElement, index):')
my_list.insert(10, 4)
my_list.showList()
print("======================================================")
#------------------------------------------------------------#
print('remove(deleteKey/value):')
my_list.remove(8)
my_list.showList()
print("======================================================")

print('\nTASK 3')
print("======================================================")

source = [3, 2, 5, 1, 8, 10]

my_list_TASK3 = MyList(source)
#------------------------------------------------------------#
print('Prints even numbers:')
my_list_TASK3.even_numbers()
print("======================================================")
#------------------------------------------------------------#
print('Checks if number is present:')
my_list_TASK3.is_present(10)
print("======================================================")
#------------------------------------------------------------#
