package at.ALDA.InterpolationSearch;

public class InterpolationSearch {
    public Car search(Car[] arr, int n, int x){
        int lo = 0;
        int hi = n - 1;
        
        while((lo <= hi) && (x >= arr[lo].getKey()) && (x <= arr[hi].getKey())){
            int pos = lo + (hi - lo) / (arr[hi].getKey() - arr[lo].getKey()) * (x - arr[lo].getKey());
            
            if(x == arr[pos].getKey()){
                return arr[pos];
            }
            
            if(x > arr[pos].getKey()){
                lo = pos + 1;
            }else{
                hi = pos - 1;
            }
        }
        
        return null;
    }
}
