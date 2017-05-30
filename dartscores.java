// Solution to https://open.kattis.com/problems/dartscores
// Accepted

import java.util.Scanner;

public class dartscores {

    static int[] circles = { 20, 40, 60, 80, 100, 120, 140, 160, 180, 200 };

    public static boolean isInside(int x, int y, int r) {
        return ((x*x + y*y) <= r*r);
    }

    public static int score(int x, int y){
        int count = 10;

        for(int c: circles){
            if (isInside(x, y, c)){
                return count;
            }
            count--;
        }
        return 0;
    }


    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        sc.useDelimiter("\\n");
        int games = sc.nextInt();

        for(int i=0; i<games; i++){
            int tries = sc.nextInt();
            int points = 0;

            for(int j=0; j<tries; j++){
                String[] coords = sc.next().split(" ");
                int x = Integer.parseInt(coords[0]);
                int y = Integer.parseInt(coords[1]);

                points += score(x, y);
            }
            System.out.println(points);
        }
    }
}
