def bsort(list):
    for i in range(len(list)-1,0,-1):   # for i in range(0,len(list)-1) 
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
             
list = [255,5,18,14,45,345,265]

bsort(list)
print(list)
