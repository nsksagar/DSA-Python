def partitioning(array, low, high):
   
    pivot = array[low]
    
    i = low 
    j = high 

    while i < j: 

        while i < high and array[i] <= pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

       
        if i < j:
            array[i], array[j] = array[j], array[i]
        
    
    array[low], array[j] = array[j], array[low]

    return j

def quicksort(array, low, high):
    if low < high:
       
        partition_index = partitioning(array, low, high)

       
        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)

    return array 

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quicksort(arr, 0, n-1)
    print("Sorted array is:", arr)