package at.ALDA.BinarySearch;

public class Main {
    public static void main(String[] args) {
        Car c1 = new Car("BMW", 0);
        Car c2 = new Car("Audi", 1);
        Car c3 = new Car("Mercedes", 2);
        Car c4 = new Car("Alfa Romeo", 3);
        Car c5 = new Car("Fiat", 4);
        
        BinarySearch search = new BinarySearch();
        Car found = search.get(new Car[]{c1, c2, c3, c4, c5}, 3);
        System.out.println(found.getName());
    }
}
