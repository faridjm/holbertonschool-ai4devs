Coding Benchmark Tasks
Use C# and ASP.NET Core with .NET 8 or later for this sprint. Before timing either run, prepare a shared starting commit with a minimal Web API project and an xUnit test project that references it. Include the product data and the pagination starter code below. Start each run from that commit and use the same acceptance criteria for both runs.
Task 1 - Filter products by category (20–25 minutes)
Requirements
- Implement GET /api/products using the in-memory product data below.
- Support an optional categoryId query parameter. Keep products in ascending ID order and return 400 Bad Request if a supplied value is zero, negative, or not an integer.
Inputs
Product ID	Name	Category ID
1	Keyboard	1
2	Office Chair	2
3	Desk Lamp	2


Outputs

A JSON array of objects with id, name, and categoryId on success. An invalid filter returns HTTP 400.

Acceptance criteria
- GET /api/products returns 200 OK and product IDs [1, 2, 3].
- GET /api/products?categoryId=2 returns 200 OK and product IDs [2, 3].
- GET /api/products?categoryId=99 returns 200 OK with [].
- categoryId=0, categoryId=-1, and categoryId=abc each return 400 Bad Request.
Task 2 - Calculate a delivery quote (15–20 minutes)
Requirements
- Implement decimal CalculateDeliveryFee(int distanceKm, bool requiresStairs) as a pure C# method.
- Charge a base fee of 10.00 AZN, plus 1.50 AZN for each kilometre beyond the first 5 km. Add 5.00 AZN when stair handling is required.
- Reject negative distances with ArgumentOutOfRangeException.
Inputs

The distance in whole kilometres and a boolean indicating whether stair handling is required.

Outputs

A decimal amount in AZN, or an ArgumentOutOfRangeException for a negative distance.

Acceptance criteria
distanceKm	requiresStairs	Expected result
0	false	10.00 AZN
5	false	10.00 AZN
6	false	11.50 AZN
8	true	19.50 AZN
-1	false	ArgumentOutOfRangeException


Task 3 - Fix product pagination and add regression tests (20–30 minutes)
Requirements
- Fix the starter method so that page numbering starts at 1 and TotalCount reports the number of items before pagination.
- Preserve input order and the existing validation for page numbers and sizes. Add xUnit regression tests for the first page, a partially filled final page, and a page beyond the end.
Inputs

An ordered list of product IDs, a page number, and a page size.
public static class ProductPagination
{
    public static (int[] Items, int TotalCount) GetPage(
        IReadOnlyList<int> productIds,
        int pageNumber,
        int pageSize)
    {
        ArgumentOutOfRangeException.ThrowIfNegativeOrZero(pageNumber);
        ArgumentOutOfRangeException.ThrowIfNegativeOrZero(pageSize);

        int[] items = productIds.Skip(pageNumber * pageSize).Take(pageSize).ToArray();
        return (items, items.Length);
    }
}
Outputs

A tuple containing the requested page's product IDs and the total number of product IDs. A nonpositive page number or page size throws ArgumentOutOfRangeException.

Acceptance criteria

With product IDs [10, 20, 30, 40, 50] and page size 2:
Page number	Expected items	Expected total count
1	[10, 20]	5
2	[30, 40]	5
3	[50]	5
4	[]	5


- A page number or page size of 0 still throws ArgumentOutOfRangeException.
- All three regression cases pass with dotnet test.
