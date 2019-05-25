// Planting Trees
// https://open.kattis.com/problems/plantingtrees
// submission accepted

using System;

namespace Kattis
{
    class PlantingTrees
    {
        public static void Run(string[] args)
        {
            int numTrees = Int32.Parse(Console.ReadLine());
            var treeLine = Console.ReadLine().Trim('\n').Split(' '); ;
            int[] trees = Array.ConvertAll(treeLine, int.Parse);
            Array.Sort(trees);

            int maxDays = 0;
            for (int i = 0; i < numTrees; i++)
            {
                int maxDaysForThisTree = numTrees + trees[i] - i;
 
                if (maxDaysForThisTree > maxDays)
                {
                    maxDays = maxDaysForThisTree;
                }
            }

            Console.WriteLine(maxDays+1);
        }
    }
}
