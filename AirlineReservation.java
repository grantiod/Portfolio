import java.util.Scanner;
import java.util.Random;

public class AirlineReservation {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String choice = "";
        Reservation res = new Reservation();

        System.out.print("Would you like to make a reservation (y/n)? ");
        choice = input.next();

        if (choice.equals("y")) {
            System.out.print("Enter first name: ");
            String fname = input.next();
            System.out.print("Enter last name: ");
            String lname = input.next();
            res.setName(fname + " " + lname);

            System.out.println();
            printAirlines();
            System.out.print("Select Airline: ");
            int airline = input.nextInt();
            switch (airline) {
                case 1:
                    res.setAirline("DA");
                    break;
                case 2:
                    res.setAirline("UA");
                    break;
                case 3:
                    res.setAirline("SA");
                    break;
                case 4:
                    res.setAirline("AA");
                    break;
                default:
                    break;
            }

            System.out.println("Enter date below (MM/DD/YYYY)");
            String date = input.next();
            while (date.length() != 10 || date.charAt(2) != '/' || date.charAt(5) != '/') {
                System.out.println("Wrong format");
                System.out.println("Enter date below (MM/DD/YYYY)");
                date = input.next();
            }
            int month = 0;
            int day = 0;
            int year = 0;
            for (int i = 0; i < date.length(); i++) {
                if (i == 0)
                    month = Integer.parseInt( String.valueOf(date.charAt(i)) ) * 10;
                else if (i == 1)
                    month += Integer.parseInt( String.valueOf(date.charAt(i)) );
                else if (i == 3)
                    day = Integer.parseInt( String.valueOf(date.charAt(i)) ) * 10;
                else if (i == 4)
                    day += Integer.parseInt( String.valueOf(date.charAt(i)) );
                else if (i == 6)
                    year = Integer.parseInt( String.valueOf(date.charAt(i)) ) * 1000;
                else if (i == 7)
                    year += Integer.parseInt( String.valueOf(date.charAt(i)) ) * 100;
                else if (i == 8)
                    year += Integer.parseInt( String.valueOf(date.charAt(i)) ) * 10;
                else if (i == 9)
                    year += Integer.parseInt( String.valueOf(date.charAt(i)) );
            }
            res.setDate(day, month, year);

            Random rand = new Random();
            int number = rand.nextInt((9999 - 100) + 1) + 10;
            res.setNumber(number);


            System.out.println();
            res.printReservation();


            System.out.println("What would you like to do?");
            System.out.println("1) Commit Reservation");
            System.out.println("2) Cancel Reservation");
            int cc = input.nextInt();
            switch (cc) {
                case 1:
                    System.out.println("Thank you!");
                    break;
                case 2:
                    System.out.println("Cancelling...");
                    res.cancelReservation();
                    break;
                default:
                    break;
            }
        }
    }

    public static void printAirlines() {
        System.out.println("Airlines");
        System.out.println("--------------------");
        System.out.println("1) Delta Airlines (DA)");
        System.out.println("2) United Airlines (UA)");
        System.out.println("3) Southwest Airlines (SA)");
        System.out.println("4) American Airlines (AA)");
    }
}

class Reservation {
    private int number;
    private String airline;
    private Date date; 
    private String name;

    public Reservation() {
        number = 0;
        airline = "";
        date = new Date();
        name = "";
    }

    public void setNumber(int n) {
        number = n;
    }

    public void setAirline(String a) {
        airline = a;
    }

    public void setDate(int d, int m, int y) {
        date.setDay(d);
        date.setMonth(m);
        date.setYear(y);
    }

    public void setName(String s) {
        name = s;
    }

    public void printReservation() {
        System.out.println("Name: " + name);
        System.out.println("Date: " + date.getDate());
        System.out.println("Flight: " + airline + " " + number);
    }

    public void cancelReservation() {
        number = 0;
        airline = "";
        date = null;
        name = "";
    }
}

class Date {
    private int day;
    private int month;
    private int year;

    public Date() {
        day = 0;
        month = 0;
        year = 0;
    }

    public Date(int d, int m, int y) {
        if (d >= 1 && d <= 31)
            day = d;
        else
            day = 0;

        if (m >= 1 && m <= 12)
            month = m;
        else
            month = 0;

        if (y >= 2000)
            year = y;
        else
            year = 0;
    }

    public void setDay(int d) {
        if (d >= 1 && d <= 31)
            day = d;
    }

    public void setMonth(int m) {
        if (m >= 1 && m <= 12)
            month = m;
    }

    public void setYear(int y) {
        if (y >= 2000)
            year = y;
    }
    
    public String getDate() {
        return month + "/" + day + "/" + year;
    }
}