package utils;

import java.util.List;

public class Timer {
    public long time(SortingAlgorithm sort, List<Integer> elements) {
        long stime = System.currentTimeMillis();
        sort.sort(elements);
        return System.currentTimeMillis() - stime;
    }
}