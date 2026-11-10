using System;

class Program
{
    static double CalculateAverage(int total, int count)
    {
        return total / count;
    }

    static void Main()
    {
        int total = 7;
        int count = 2;
        double average = CalculateAverage(total, count);
        Console.WriteLine($"Average: {average}");
    }
}
