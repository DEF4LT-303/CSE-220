class KeyIndex:

    k = []
    x = 0

    def __init__(self, a):
        
        self.a = a

        min = 0
        for item in a:

            if item < min:
                min = item
        
        KeyIndex.x = min * -1           # stores positive min value on global var

        for i in range(len(a)):         # for supporting negative numbers

            a[i] += KeyIndex.x
        
        max = 0
        for item in a:

            if item > max:
                max = item
        
        KeyIndex.k = [0]*(max+1)        # building aux array
        for i in range(len(a)):

            idx = a[i]
            KeyIndex.k[idx] = KeyIndex.k[idx] + 1

    def search(self, val):

        if KeyIndex.k[val+KeyIndex.x] != 0:
            return True
        
        else:
            return False

    def sort(self):
        lst = []
        for i in range(len(KeyIndex.k)):

            if KeyIndex.k[i] != 0:
                for j in range(KeyIndex.k[i]):
                    lst.append(i - KeyIndex.x)

        return lst

    def printList(self):

        for i in range(len(self.a)):

            self.a[i] -= KeyIndex.x

        print(self.a)
        


my_list = [4,-2,3,-4,7,4]
my_list = [4,2,3,4,7,4]
lst = KeyIndex(my_list)

print(lst.search(-2))
lst.printList()
print(lst.sort())

class HashTable:

    Hash = [0]*9

    def __init__(self, arr):
        
        self.arr = arr

        vowels = ['A', 'E', 'I', 'O', 'U']
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        
        for x in arr:
            cons = 0
            numbers = 0
            for i in x: 

                if i not in vowels:
                    if i not in nums:
                        cons += 1

                    else:
                        i = int(i)
                        numbers += i

            res = ((cons*24)+numbers)%9
            
            if HashTable.Hash[res] == 0:
                HashTable.Hash[res] = x

            else:                                                   # linear probing
                for i in range(res, len(HashTable.Hash)+res):       # iterate circular array

                    if HashTable.Hash[i%len(HashTable.Hash)] == 0:  # next available space
                        HashTable.Hash[i%len(HashTable.Hash)] = x
                        break               

        print(HashTable.Hash)

my_list = ['ST1E89B8A32', 'RYAN72', 'CSE220', 'ST1E89B8A32', 'TEST', 'TEST']
hs = HashTable(my_list)
