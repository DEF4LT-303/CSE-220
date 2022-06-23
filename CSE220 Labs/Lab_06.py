def selection_sort(array, i, n):

    min_val = i

    for j in range(i+1, n):

        if array[j] < array[min_val]:                   # find min val
            min_val = j

    array[min_val], array[i] = array[i], array[min_val] # swap current val with min val

    if i+1 < n:
        selection_sort(array, i+1, n)                   # runs till all the val are iterated

def insertion_sort(array, n):

    if n <= 1:
        return

    insertion_sort(array, n-1)                          # runs till all val are iterated

    i = array[n-1]                  # last val
    j = n-2                         # prev last val

    while j >= 0 and array[j] > i:

        array[j+1] = array[j]       # shifts val for insertion
        j = j-1

    array[j+1] = i                  # inserts current val to proper index

#----------Linked List-----------#
class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class MyList:

    def __init__(self, a):
        self.head = None

        for i in a:                         

            if self.head is None:          
                new_node = Node(i, None)
                self.head = new_node

            else:                           
                n = self.head
                while n.next:

                    n = n.next

                n.next = Node(i, None)

    def showList(self):

        if self.head is None:
            print('Empty List')
            return
        
        n = self.head
        while n:

            print(n.data, '-> ', end='')
            n = n.next

    def length(self):

        count = 0
        n = self.head

        while n:

            n = n.next
            count += 1

        return count

def bubble_sort_list(head):
    
    n = head
    next_val = None

    
    while n:

        next_val = n.next               

        while next_val:                 

            if n.data > next_val.data:  
                temp = n.data
                n.data = next_val.data      # swaps
                next_val.data = temp

            next_val = next_val.next
        n = n.next

def selection_sort_list(head): 

    n = head

    while n:

        min_val = n
        j = n.next

        while j:

            if j.data < min_val.data:
                min_val = j

            j = j.next

        n.data, min_val.data = min_val.data, n.data     #swaps

        n = n.next

def binary_search(array, start, end, value):

    if start <= end:
        mid = (start + end) // 2

        if array[mid] == value:
            return mid

        elif array[mid] < value:
            return binary_search(array, mid+1, end, value)

        else:
            return binary_search(array, start, mid-1, value)

    else:
        return None  

memory = {}

def fibonacci_memoization(n):

    if n in memory:
        return memory[n]        # returns if val already in memo

    if n <=1:
        return 1

    else:
        value = fibonacci_memoization(n-1) + fibonacci_memoization(n-2)

    memory[n] = value           # stores val in memo
    return value     


my_list=[1,2,3,10,4,6]
selection_sort(my_list, 0, len(my_list))

print('Selection Sort:', my_list)

insertion_sort(my_list, len(my_list))
print('Insertion Sort:', my_list)

bubble = MyList(my_list)
bubble_sort_list(bubble.head)
print('\nBubble sorted singly linked list: ')
bubble.showList()
print()

selection = MyList(my_list)
selection_sort_list(selection.head)
print('\nSelection sorted singly linked list: ')
selection.showList()
print()

my_list=[1,2,3,4,5,6]
value = 4
print('\nBinary Search:', binary_search(my_list, 0, len(my_list)-1, value))

print('\nFibonacci using memoization: ', fibonacci_memoization(3))