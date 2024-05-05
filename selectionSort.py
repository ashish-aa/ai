def sort(arr):
    for i in range(len(arr)-1):
        min =i 
        for j in range(i+1,len(arr)):
            if arr[j]< arr[min]:
                min = j
        if i!= min:
            arr[i],arr[min] = arr[min],arr[i]
    return arr


def main():
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    arr = sort(arr)
    print("Sorted Array : ",arr)

main()