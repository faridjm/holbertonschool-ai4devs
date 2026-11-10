using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var products = new Dictionary<int, string>
        {
            { 1, "Keyboard" },
            { 2, "Mouse" }
        };
        int requestedId = 3;
        Console.WriteLine(products[requestedId]);
    }
}
