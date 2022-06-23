import random

def shiftLeft(source, k):

  j = 0
  for i in range(k, len(source)):

    source[j] = source[i]  # replaces initial value with k value
    j += 1

  for x in range(j, len(source)):

    source[x] = 0          # sets remaining values to 0

  print('Task 01: ', end='')
  print(source)

def rotateLeft(source, k):
  
  for i in range(0, k):                # loop runs k amount of times to rotate

    temp = source[0]

    for j in range(0, len(source)-1):

        source[j] = source[j+1]        # shifts elements to left

    source[len(source)-1] = temp       # inserts first element to the last

  print('Task 02: ', end='')
  print(source)

def remove(source, size, idx):

  source[idx] = 0           # removes the value
  for i in range(idx, size):

    source[i] = source[i+1] # sets next value to initial value

  print('Task 03: ', end='')
  print(source)

def removeAll(source, size, element):
 
  for i in range(size):

    if source[i] == element:  # removes specified elemet
      source[i] = 0
  
  for k in range(size):          # runs loop (amount of elements removed) times for  sortting
    
    for j in range(size-1, 0, -1):

      temp = 0
      if source[j-1] == 0:    # sorts all the empty elements to right side
        temp = source[j]
        source[j] = source[j-1]
        source[j-1] =  temp
  
  print('Task 04: ', end='')
  print(source)

def splitArray(source):

  bool = False

  for i in range(1, len(source)):   # puts balance in each index

    left = 0
    right = 0

    for j in range(i):              # sums left pan
      left += source[j]
    
    for k in range(i, len(source)): # sums right pan
      right += source[k]
    
    if left == right:          
      bool = True
  
  print('Task 05: ', end='')
  print(bool)

def arraySeries(n):

  array = []

  for i in range(1, n+1):      # creating n spaces
    for j in range(n, 0, -1):  # for appending elements in n spaces

      if j <= i:               
        array.append(j)

      else:
        array.append(0)

  print('Task 06: ', end='')
  print(array)

def max_bunch(arr):

  count = 1
  final = 0

  for i in range(len(arr)-1):  

    if arr[i] == arr[i+1]:  # adds count if consecutive elements are same
      count += 1
      final = count

    else:                   # sets count back to 1 if consecutive elements are not same
      final = count
      count = 1 

    if final < count:       # sets final value if its less than count
      final = count

  print('Task 07: ', end='')  
  print(final)

def repetition(arr):

  lst = [] 
  total_count = []

  for i in arr:

    if i not in lst:   # appending each element on new list
      lst.append(i)
  
  for i in range(len(lst)):

    count = 0
    for j in range(len(arr)):   # appending the count of duplicates on new list

      if lst[i] == arr[j]:
        count += 1

    total_count.append(count)

    for x in range(0, len(total_count)):  # removing all 1s from list 

      if total_count[x] == 1:
        total_count.remove(1)

    bool= False
    for i in range(0, len(total_count)-1):   # checking if at least 2 elements in count_lst is same

        for j in range(i+1, len(total_count)):

            if(total_count[i]==total_count[j]):
                bool=True
                break

  print("Task 08: ", end="")
  print(bool)

def palindrome(source, start, size):

    linear = []
    idx = 0
    for i in range(start, start+size):

        linear.append(source[i%len(source)])  # copying circular array values to linear array

    bool = False

    if linear == linear[::-1]:  # checking reverse
        bool = True

    print("Task 09: ", end="")
    print(bool)

def intersection(source_1, start_1, size_1, source_2, start_2, size_2):

    final = []

    if size_2 > size_1:                             # if second array is greater
        for i in range(start_1, (start_1+size_1)):

            if source_1[i%len(source_1)] in source_2:
                final.append(source_1[i%len(source_1)])

    else:                                           # if first array is greater
        for i in range(start_2, (start_2+size_2)):

            if source_2[i%len(source_2)] in source_1:
                final.append(source_2[i%len(source_2)])

    print("Task 10: ", end="")
    print(final)

def musical_chair():

    names = []

    for i in range(1, 8):

        name = input(f'Enter name {i}: ')
        names.append(name)

    length = 7
    while (length != 1):                  # loop runs till 1 player left

        random_num = random.randint(0, 3)
        delete = int(length/2)

        if random_num == 1:               # sets middle value to 0 and decreases length
            names[delete] = 0
            length -= 1

        else:                             # right-shifts for rotation
            temp = names[length-1]        

            for i in range(length-1, 0, -1):

                names[i] = names[i-1]

            names[0] = temp

        for i in range(length):           # sorts all the 0s to the right

            if names[i] == 0:
                temp = names[i+1]
                names[i+1] = names[i]
                names[i] = temp

        # print('Random number = ', random_num)
        # print(names)
           
    print(names[0])


source=[10,20,30,40,50,60]
shiftLeft(source,4)
source=[10,20,30,40,50,60]
rotateLeft(source,4)
source=[10,20,30,40,50,0,0]
remove(source,5,2)
source=[10,2,30,2,50,2,2,0,0]
removeAll(source,7,2)
source=[10, 3, 1, 2, 10] 
splitArray(source)
arraySeries(3)
max_bunch([1,1,2, 2, 1, 1,1,1])
repetition([4,5,6,6,4,3,6,4])
palindrome([20,10,0,0,0,10,20,30], 5, 5)
# intersection([40,50,0,0,0,10,20,30], 5, 5, [10,20,5,0,0,0,0,0,5,40,15,25], 8, 7)
intersection([10,20,5,0,0,0,0,0,5,40,15,25], 8, 7, [40,50,0,0,0,10,20,30], 5, 5)

musical_chair()