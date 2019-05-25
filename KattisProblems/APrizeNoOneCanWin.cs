// A Prize No One Can Win
// https://open.kattis.com/problems/aprizenoonecanwin
// submission accepted

using System;

namespace Kattis
{
    class APrizeNoOneCanWin
    {
        public static void Run(string[] args)
        {
            var info = Console.ReadLine().Split(' ');
            int must_surpass = Int32.Parse(info[1]);
            int maxnum = Int32.Parse(info[0]);
            var inp = Console.ReadLine().Trim('\n').Split(' ');

            int[] item_prices = Array.ConvertAll(inp, int.Parse);

            Array.Sort(item_prices);

            var result = maxnum;
            for (int i = 1; i < maxnum; i++)
            {
                if (item_prices[i] + item_prices[i - 1] > must_surpass)
                {
                    result = i;
                    break;
                }
            }

            Console.WriteLine(result);
        }
    }
}
