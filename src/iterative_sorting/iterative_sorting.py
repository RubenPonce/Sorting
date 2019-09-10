# TO-DO: Complete the selection_sort() function below 
# Set the current minimum to the first element
# if the current minimum is less than the current element, leave it alone,
# if the current element is less than the current minimum, the current element is the current min
# 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)      
        for x in range(cur_index, len(arr)):
            if(arr[x] < arr[smallest_index]):
                smallest_index = x

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr

numberList = [1,23,4,5,7,86,0]
print(selection_sort(numberList) )


def bubble_sort( arr ):
# 1. Loop through your array
#     - Compare each element to its neighbor
#     - If elements in wrong position (relative to each other, swap them)
# 2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
# TO-DO:  implement the Bubble Sort function below

    highest_index = len(arr) - 1
    for i in range( highest_index,0,-1):
        for j in range(i):
            if(arr[j] > arr[j + 1]):
                temp_arr = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp_arr

        
        


    return arr
numberList2 = [1,23,4,5,7,86,0]
print(bubble_sort(numberList2) )

# STRETCH: implement the Count Sort function below

def count_sort( arr, maximum=-1 ):

    return arr