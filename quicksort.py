import utils

def quickSort(l):
    l = l.copy()
    partition(l, 0,len(l))
    return l

def partition(arr,left, right):
    if right > left:
        p = arr[-1]
        i = left-1
        k = right
        while(i < k):
            while(arr[i]<p):
                i = i+1
            while(arr[k]>p):
                k = k-1
            if i < k:
                arr[i], arr[k] = arr[k], arr[i]
            else:
                break
        arr[i], arr[right] = arr[right], arr[i]
    partition(arr,left,i-1)
    partition(arr,i+1,right)


    
    

def main():
    l = utils.get_random_ints(10)

    nl = quicksort(l)
    print(nl)

    w, m, b = utils.eval_stats(quicksort)
    print('='*64)
    print('Worst:\t%.3fms\nMean:\t%.3fms\nBest:\t%.3fms' %
          (w / (10**6), m / (10**6), b / (10**6)))
    print('='*64)


if __name__ == '__main__':
    main()