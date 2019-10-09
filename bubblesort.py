import utils


def bubble_sort(l):
    l = l.copy()

    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]

    return l


def bubble_sort_imp(l):
    l = l.copy()

    i = len(l)
    while i > 1:
        newi = 1
        for j in range(0, i-1):
            if l[j] > l[j+1]:
                l[j+1], l[j] = l[j], l[j+1]
                newi = j+1
        i = newi
    return l


def main():
    l = utils.get_random_ints(10000)

    # nl = bubble_sort(l)
    # print(nl)

    w, m, b = utils.eval_stats(bubble_sort, n=1000)
    print('='*64)
    print('Worst:\t%.3fms\nMean:\t%.3fms\nBest:\t%.3fms' %
          (w / (10**6), m / (10**6), b / (10**6)))
    print('='*64)

    # nl = bubble_sort_imp(l)
    # print(nl)

    w, m, b = utils.eval_stats(bubble_sort_imp, n=1000)
    print('='*64)
    print('Worst:\t%.3fms\nMean:\t%.3fms\nBest:\t%.3fms' %
          (w / (10**6), m / (10**6), b / (10**6)))
    print('='*64)


if __name__ == '__main__':
    main()
