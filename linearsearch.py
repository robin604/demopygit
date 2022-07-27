# Binary Search

def bsort(list):
    for i in range(0,len(list)-1):
        minpos = i
        for j in range(i, len(list)):
            if list[j] < list[minpos]:
                minpos = j
                
        temp = list[i]
        list[i] =list[minpos]
        list[minpos] = temp
        
    
list = [255,5,18,14,45,345,265]

bsort(list)
#print
print(list)
