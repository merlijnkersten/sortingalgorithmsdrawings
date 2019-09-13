# See read me

import random

def find_first_sublist(sublist):
    length = len(sublist)
    for index in range(0, len(anne)):
        if anne[index:index+length] == sublist:
            return index, index+length
def replace_sublist(sublist, replacement):
    length = len(replacement)
    index = 0
    for start, end in iter(lambda: find_    first_sublist(sublist), None):
        anne[start:end] = replacement
        index = start + length

def xavier(charlie): #Bob: before, Charlie: to be sorted, Emily: after.
    #print(charlie)
    dave = []
    dave.extend(charlie)
    fransesca = [] # smaller or equal than pivot
    pivot = dave[-1]
    for i in range(len(dave)-1):
        if dave[i] <= pivot:
            fransesca.append(dave[i])
            charlie.remove(dave[i])
        print(fransesca + charlie)
    replace_sublist(dave, [fransesca, pivot, charlie])
    #fransesca.append(pivot)
    #charlie.remove(pivot)
    #print(fransesca + charlie)


anne = list(range(0,10))
print(anne)
random.shuffle(anne)
xavier(anne)
print(anne)
#           0 1 2 3 4 5 6 7






    

