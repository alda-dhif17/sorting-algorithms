package at.ALDA.BinarySearch;

public class BinarySearch {
    public Car get(Car[] arr, int criteria){
        return search(arr, criteria, 0, arr.length - 1);
    }
    
    public Car search(Car[] arr, int criteria, int left, int right){
        int center = (right - left) / 2 + left;
        
        if(criteria > arr[center].getKey()){
            return search(arr, criteria, center + 1, right);
        }else if(criteria < arr[center].getKey()){
            return search(arr, criteria, left, center - 1);
        }else if(criteria == arr[center].getKey()){
            return arr[center];
        }
        
        return null;
    }
}
