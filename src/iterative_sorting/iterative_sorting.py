# TO-DO: Complete the selection_sort() function below 
'''
Selection Sort
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.



Following example explains the above steps:
'''
example_arr = [2,1,10,9,4,1]
def selection_sort( arr ):
    # loop through n-1 elements
    # find the minimum element
    # move the big element to the sorted array
    # if the current element is less than the smallest element
    # make the current index the smallest index
  

    for currentIndex in range(0, len(arr) - 1):
        smallest_index = currentIndex
        for remaining_index in range(smallest_index, len(arr) ):
            if arr[smallest_index] > arr[remaining_index]:
                smallest_index = remaining_index
        if(smallest_index != currentIndex):
            arr[currentIndex], arr[smallest_index] =  arr[smallest_index], arr[currentIndex]

    print(arr)
    return arr

# selection_sort(example_arr)
# TO-DO:  implement the Bubble Sort function below
def swap(arr, currIndex, remainIndex):
    temp = arr[currIndex]
    arr[currIndex], arr[remainIndex] = arr[remainIndex], temp
def bubble_sort( arr ):
    #if the current element greater than the nextelement, swap it
    for current_index in range(len(arr)):
        for remaining_index in range(len(arr)-current_index - 1):
            if(arr[remaining_index] > arr[remaining_index + 1]):
                temp = arr[remaining_index]
                arr[remaining_index], arr[remaining_index + 1] = arr[remaining_index+1], temp
            
      
    print("bubble_sort", example_arr)
    return arr
# bubble_sort(example_arr)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr