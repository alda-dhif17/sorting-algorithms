import utils

def bubble_sort(l):
    l = l.copy()
    
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    
    return l

def main():
    l = utils.get_random_ints(10)

    nl = bubble_sort(l)
    print(nl)

    w, m, b = utils.eval_stats(bubble_sort)
    print('='*64)
    print('Worst:\t%.3fms\nMean:\t%.3fms\nBest:\t%.3fms' % (w / (10**6), m / (10**6), b / (10**6)))
    print('='*64)

if __name__ == '__main__':
    main()