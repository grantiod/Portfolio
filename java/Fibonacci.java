import java.util.Scanner;
public class Fibonacci {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Number of numbers: ");
        int n = input.nextInt();
        if (n <= 0)
            return; // end program if size is insufficient
        int fib[] = new int[n];
        fib[0] = 1;
        if (n == 1) {
            System.out.println(fib[0]);
            return; // no need to continue program if size is insufficient
        }
        fib[1] = 1;
        System.out.print(fib[0] + " " + fib[1] + " ");
        for (int i = 2; i < n; i++) {
            fib[i] = fib[i - 1] + fib[i - 2];
            if (i == 10)
                System.out.println();
            System.out.print(fib[i] + " ");
        }
        System.out.println();
    }
}
