using System;
using System.Collections.Generic;

class Program
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