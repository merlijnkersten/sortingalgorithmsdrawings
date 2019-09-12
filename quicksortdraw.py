# See read me
'''
import random

anne = list(range(0,5))

print(anne)

random.shuffle(anne)

print(anne)

def ziggy(bob):
    cas = []
    deidre = []
    last_item = bob[-1]
    for i in range(len(bob)-1):
        if bob[i] < last_item:
            cas.append(bob[i])
        else:
            deidre.append(bob[i])
    cas.append(last_item)
    bob = cas + deidre
    print(bob)

anne = ziggy(anne)
'''

def xavier(bob, charlie, emily): #Bob: before, Charlie: to be sorted, Emily: after.
    print(bob + charlie + emily)
    ogcharlie = charlie
    fransesca = [] # smaller or equal than Charlie
    pivot = ogcharlie[-1]
    for i in range(len(ogcharlie)-1):
        if ogcharlie[i] <= pivot:
           fransesca.append(ogcharlie[i])
           charlie.remove(ogcharlie[i])
        print(bob + fransesca + charlie + emily)
    fransesca.append(pivot)
    print(bob + fransesca + charlie + emily)

xavier([], [1,4,2,7,3,5,7,3], [])





    

