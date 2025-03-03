using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace jHyuk.week31
{
    class 돌_게임
    {
        static void Main()
        {
            int n = int.Parse(Console.ReadLine());

            if (n % 2 == 1)
            {
                Console.WriteLine("SK");
            }
            else
            {
                Console.WriteLine("CY");
            }
        }
    }
}
