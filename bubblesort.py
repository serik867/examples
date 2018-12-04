

def bubbleSort(the_list):
    count = 0
    for i in range(0, len(the_list) - 1):
        for j in range(0,len(the_list) - 1 - i):
            if the_list[j] > the_list[j+1]:
                the_list[j], the_list[j+1] = the_list[j+1], the_list[j]
                count+=1
    
    result = 'It is a ordered list {} and it takes {} count of task!!! '.format(the_list, count)
    return the_list

#aList =[2,2,3,4,5,67,8,9,54,56,34,8]
#print(bubbleSort(aList))