import utils.Timer;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Integer> elements = new ArrayList<>();

        elements.add(9);
        elements.add(3);
        elements.add(5);
        elements.add(8);
        elements.add(1);
        elements.add(9);
        elements.add(4);

        System.out.println(new Timer().time(new QuickSort(), elements));
    }
}
