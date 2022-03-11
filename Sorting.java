public class Sorting {
    public static void main(String[] args) {
        int list[] = {1, 14, 13, 9, 8, 11, 15, 16, 2, 7, 12, 4, 19, 5, 17, 6, 3, 18, 0, 10};
        long start = System.currentTimeMillis();
        print(list);
        //insertionSort(list);
        mergeSort(list, 0, list.length - 1);

        print(list);

        long finish = System.currentTimeMillis();
        long elapsed = finish - start;
        System.out.println("Time elapsed: " + elapsed + " milliseconds");
    }

    public static void print(int[] list) {
        for (int i = 0; i < list.length; i++)
            System.out.print(list[i] + " ");
        System.out.println();
    }

    public static void insertionSort(int[] list) {
        int i;
        for (int j = 1; j < list.length; j++) {
          int key = list[j];
          i = j - 1;
          while (i >= 0 && list[i] > key) {
            list [i + 1] = list[i];
            i--;
          }
          list[i + 1] = key;
        }
      }
    
      public static void merge(int[] list, int left, int mid, int right) {
        int i = 0;
        int j = 0;
        int k = 0;
        int[] l = new int[mid - left + 1];
        int[] r = new int[right - mid];
    
        for (i = 0; i < l.length; i++)
          l[i] = list[left + i];
        for (j = 0; j < r.length; j++)
          r[j] = list[mid + 1 + j];
        
        i = 0;
        j = 0;
        k = left;
        while (i < l.length && j < r.length) {
            if (l[i] <= r[j]) {
              list[k] = l[i];
              i++;
            }
            else {
              list[k] = r[j];
              j++;
            }
            k++;
        }
         
        // Copy the remaining elements of l[] and r[], if there are any
        while (i < l.length) {
          list[k] = l[i];
          i++;
          k++;
        }
        while (j < r.length) {
          list[k] = r[j];
          j++;
          k++;
        }
      }
    
      public static void mergeSort(int[] list, int p, int r) {
        if (p < r) {
          int q = (p + r) / 2;
          mergeSort(list, p, q);
          mergeSort(list, q + 1, r);
          merge(list, p, q, r);
        }
      }
}
