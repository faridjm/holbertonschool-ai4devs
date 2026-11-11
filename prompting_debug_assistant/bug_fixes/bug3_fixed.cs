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
        if (products.TryGetValue(requestedId, out var productName))
        {
            Console.WriteLine(productName);
        }
        else
        {
            Console.WriteLine("Product not found");
        }
    }
}
