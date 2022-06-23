def fact(n):

    if n <= 1:
        return n

    else:
        return n*fact(n-1)

def fib(n):

    if n < 0:
        return 'Invalid Input'
    
    if n == 0:          # first fib
        return 0

    elif n == 1:        # second fib
        return 1

    else:
        return fib(n-1) + fib(n-2)

def array(lst):

    if len(lst) == 0:
        return ""

    else:
        print(lst[0], end=' ')

        array(lst[1:])

def power(base, n):

    if n == 0:           # if power is 0, return 1
        return 1

    else:
        return base*power(base, n-1)

def binary(n):

    if n == 0:
        return
    
    else:
        binary(n//2)
        print(n%2, end='')


#-------------Linked List-------------#
class Node:

    def __init__(self, data=None, next=None):
        
        self.data = data
        self.next = next

class LinkedList:

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
#--------------------------------------#

def add(head):

    if head != None:
        return head.data + add(head.next)

    return 0


def hocBuilder(height):

    if height == 0:
        return 0

    elif height == 1:
        return 8

    else:
        return 5 + hocBuilder(height-1)

def patternOuter(n):            # row loop control

    if n == 0:
        return

    patternOuter(n-1)           
    print(patternInner(n))      # prints pattern
        
def patternInner(n):            # pattern generator

    if n == 1:
        return n

    else:
        print(patternInner(n-1), end=' ')
        return n
 
class FinalQ:

    def print(self, array, idx):

        if idx < len(array):
            profit = self.calcProfit(array[idx])
            
            print(f'Investment: {array[idx]}; Profit: {profit}')
            self.print(array, idx+1)        # iteration

        return                              # terminates the loop

    temp = 0        # global vars for handling profits and investments
    total = 0
    def calcProfit(self, investment):

        if investment >= 25000 and investment < 100000:
            FinalQ.temp = investment
            return 0

        elif investment <= 100000:
            investment -= FinalQ.temp  
            FinalQ.temp = array[1]         
            profit =  (investment/(100/4.5))
            
            FinalQ.total += profit
            return FinalQ.total

        elif investment > 100000:
            temp = investment
            investment -= FinalQ.temp
            FinalQ.temp = temp
            profit = (investment/(100/8))
            
            FinalQ.total += profit
            return FinalQ.total



#-------------------------------------#

print('Task 01\n')

print('Factorial: ', fact(int(input('Enter Number: '))))
print('Fibonacci: ', fib(int(input('Enter Number: '))))
print('Array: ', end='')
array([1,2,3,4])
print()

print('\nPower: ', power(5, 4))

print('\n-------------------------------------')
print('Task 02\n')

binary(int(input('Enter Decimal Value: '))) 
print()
print('Sum of linked list: ', end='')
source = [10,20,30,40,50]
lst = LinkedList(source)

print(add(lst.head))
# print(reverse(lst.head))

print('\n-------------------------------------')
print('Task 03\n')

print(hocBuilder(int(input('Enter Height: '))))

print('\n-------------------------------------')
print('Task 04\n')

patternOuter(int(input('Enter number: ')))

print('\n-------------------------------------')
print('Task 05\n')

array=[25000,100000,250000,350000] 
f = FinalQ() 
f.print(array,0)