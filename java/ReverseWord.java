import java.util.Scanner;
public class ReverseWord {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter word: ");
        String word = input.next();

        word = word.toLowerCase();
        char[] reverse = new char[word.length()];
        
        for (int i = 0; i < word.length(); i++) {
            reverse[i] = word.charAt(word.length() - 1 - i);
            System.out.print(reverse[i]);
        }
    }
}