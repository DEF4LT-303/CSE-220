#       Balanced parentheses checker       #

class Task1:

    def __init__(self):
        self.stack = []

    def peek(self):

        return self.stack[-1]

    def push(self, item):

        # self.stack.append(item)
        self.stack += [item]

    def pop(self):

        pop = self.stack[-1]
        self.stack = self.stack[:-1]

        return pop

    def show(self):

        return self.stack

    
    def checker(self, string):               # Taken partial help from for checking pairs -> (https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/)      

        openbraces = ['(', '{', '[']
        closedbraces = [')', '}', ']']

        for i in string:

            if i in openbraces:
                self.push(i)

            elif i in closedbraces:
                idx = closedbraces.index(i)

                if len(self.stack) > 0 and openbraces[idx] == self.peek():
                    self.pop()

                else:
                    if len(self.stack) == 0:
                        error = string.index(i)
                        msg = f'This expression is NOT correct.\nError at character #{error+1}. \'{i}\' - is not opened.'
                        return msg            
            print(self.stack)
        if len(self.stack) != 0:
            error = string.index(self.peek())
            return f'This expression is NOT correct.\nError at character #{error+1}. \'{self.peek()}\' - is not closed'

        else:
            return 'This expression is correct.'


stk = Task1()

final = stk.checker(input())
print(final)

class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Task2:

    def __init__(self):
        self.head = None

    def push(self, item):

        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            return

        else:
            n = self.head

            while n.next:

                n = n.next

            n.next = new_node

    def pop(self):

        n = self.head

        if self.head is None:
            return

        elif self.head.next is None:
            self.head = None
            return

        else:

            while n.next.next:

                n = n.next

            n.next = None

    def peek(self):

        n = self.head

        while n.next:

            n = n.next

        return n.data

    def nodeCounter(self):

        count = 0
        n = self.head

        while n:

            n = n.next
            count += 1

        return count

    def checker(self, string):

        openbraces = ['(', '{', '[']
        closedbraces = [')', '}', ']']

        for i in string:

            if i in openbraces:
                self.push(i)

            elif i in closedbraces:
                idx = closedbraces.index(i)

                if self.nodeCounter() > 0 and openbraces[idx] == self.peek():
                    self.pop()

                else:
                    if self.nodeCounter() == 0:
                        error = string.index(i)
                        msg = f'This expression is NOT correct.\nError at character #{error+1}. \'{i}\' - is not opened.'
                        return msg            

        if self.nodeCounter() != 0:
            error = string.index(self.peek())
            return f'This expression is NOT correct.\nError at character #{error+1}. \'{self.peek()}\' - is not closed'

        else:
            return 'This expression is correct.'


stk = Task2()

final = stk.checker(input())

print(final)