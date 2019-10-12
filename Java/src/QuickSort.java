import utils.SortingAlgorithm;

import java.util.List;

class QuickSort implements SortingAlgorithm {
    public void sort(List<Integer> elements) {
        sort(elements, 0, elements.size()-1, 5);
    }

    public void sort(List<Integer> elements, int limit) {
        sort(elements, 0, elements.size()-1, limit);
    }

    public void sort(List<Integer> elements, int left, int right, int limit) {
        if (left <= right - limit) {
            int pivot = right,
                    l = left,
                    r = right;

            while (l < r) {
                for (; l < r; l++) {
                    if (elements.get(l) > elements.get(pivot))
                        break;
                }
                for (; r > l; r--) {
                    if (elements.get(r) < elements.get(pivot))
                        break;
                }

                int temp = elements.get(l);
                elements.set(l, elements.get(r));
                elements.set(r, temp);
            }

            int temp = elements.get(pivot);
            elements.set(pivot, elements.get(l));
            elements.set(l, temp);

            sort(elements, left, l-1, limit);
            sort(elements, l+1, right, limit);
        } else {
            new InsertionSort().sort(elements, left, right+1);
        }
    }
}