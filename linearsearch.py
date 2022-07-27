# Program to perform Bubble sort

def bsort(list):
    for i in range(0,len(list)-1):
        minpos = i
        for j in range(i, len(list)):
            if list[j] < list[minpos]:
                minpos = j
                
        temp = list[i]
        list[i] =list[minpos]
        list[minpos] = temp
        
#list of 5 numbers
list = [255,5,18,14,45,345,265]
bsort(list)

#print list
print(list)

# Thank you for visiting


# Done my changes in local repository and now merge both
################### Final copy ####################################

