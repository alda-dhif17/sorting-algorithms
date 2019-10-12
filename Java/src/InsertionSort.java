import utils.SortingAlgorithm;

import java.util.List;

class InsertionSort implements SortingAlgorithm {
    public void sort(List<Integer> elements) {
        sort(elements, 0, elements.size());
    }

    public void sort(List<Integer> elements, int left, int right) {
        for (int i = left + 1; i < right; i++) {
            int curr = elements.get(i),
                    j = i-1;

            for (; j >= left; j--) {
                if (elements.get(j) > curr) {
                    elements.set(j+1, elements.get(j));
                } else {
                    break;
                }
            }

            elements.set(j+1, curr);
        }
    }
}