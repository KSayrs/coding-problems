// Solution for https://open.kattis.com/problems/cardtrick2
// Card Trick
// Submission accepted

import java.util.*;

public class CardTrick {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        sc.useDelimiter("\\n");
        int cases = sc.nextInt(); // number of cases

        for(int i=0;i<cases;i++) {

            List<Integer> queue = new ArrayList<>();
            int n = sc.nextInt();

            queue.add(n);

            for(int j=n-1;j>0;j--){

                queue.add(0, j);

                for(int x=0;x<j;x++){
                    int val = queue.remove(queue.size() - 1);
                    queue.add(0, val);
                }
            }
            for(int item : queue){
                System.out.print(item + " ");
            }
        }
    }
}
