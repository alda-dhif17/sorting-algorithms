import utils

def main():
    arr = [8, 3, 3, 5, 9, 7, 2]
    print(arr)
    arr = merge_sort(arr, 0, len(arr) - 1)
    print(arr)

def merge_sort(arr, left, right):
    center = int(round((left + right) / 2))

    #split further down
    if (left - right) == 1:
        merge_sort(left, center)
        merge_sort(center + 1, right)
    
    #merge together
    temp = center
    temp += 1

    while left != (center + 1) and temp != (right + 1):
        if arr[left] > arr[temp]:
            arr[left], arr[temp] = arr[temp], arr[left]
            temp += 1
        else:
            left += 1
    
if __name__ == "__main__":
    main()