# Bug Descriptions

## Bug 1 – bug1.py

**Intended Behavior**: This Python script should calculate and display the total cost of a list of products. When executed, `main()` creates a list of prices `[12.5, 20.0, 7.5]` and passes it to `calculate_total()`. The function should initialize a running total to zero, iterate over every price, add each price to the total, and return the final sum. The main function should then format the returned value to two decimal places and print `Total: 40.00`. An empty list should produce a total of zero.

**Issue Type**: Syntax error.

**Notes**: The `for price in prices` statement is missing a colon. Python cannot parse the script, so execution stops before `main()` runs.

## Bug 2 – bug2.js

**Intended Behavior**: This JavaScript program should calculate a product's final price after a percentage discount. The `main()` function supplies an original price of 100 and a discount percentage of 20 to `calculateDiscount()`. The function should calculate the discount amount as the original price multiplied by the percentage divided by 100, subtract that amount from the original price, and return the discounted price. The main function should display `Final price: 80`. A zero-percent discount should leave the original price unchanged.

**Issue Type**: Logical error.

**Notes**: The function adds the discount amount instead of subtracting it. The program runs but prints 120 instead of 80.

## Bug 3 – bug3.cs

**Intended Behavior**: This C# console application should look up a product by its numeric ID. The program initializes a dictionary containing ID 1 for Keyboard and ID 2 for Mouse, then sets the requested ID to 3. It should check whether the requested ID exists in the dictionary. If the ID exists, it should display the associated product name. If the ID does not exist, it should display a product-not-found message and finish normally. For the supplied ID 3, the expected result is a message such as `Product not found`, without an unhandled exception.

**Issue Type**: Runtime exception.

**Notes**: Directly accessing a missing dictionary key with `products[requestedId]` throws `KeyNotFoundException` when the dictionary is correctly declared.

## Bug 4 – bug4.py

**Intended Behavior**: This Python script should sum all numeric elements in a list. The `main()` function creates the list `[10, 20, 30]` and passes it to `sum_items()`. The function should initialize a total to zero, visit each valid list index from zero through the last index, add the corresponding element, and return the sum. The main function should print `Sum: 60`. An empty list should return zero without attempting to access any elements.

**Issue Type**: Off-by-one error.

**Notes**: The loop uses `range(len(items) + 1)`, which attempts to access index 3 in a three-element list. This raises `IndexError` before the total can be returned.

## Bug 5 – bug5.cs

**Intended Behavior**: This C# console application should calculate an arithmetic average while preserving fractional precision. The `Main()` method supplies a total of 7 and a count of 2 to `CalculateAverage()`. The function should divide the total by the count using floating-point arithmetic and return the result as a `double`. The main method should print the average, which is 3.5 for the supplied inputs. The calculation should preserve fractional values rather than truncate them to integers. The count is assumed to be positive.

**Issue Type**: Data type misuse.

**Notes**: Both operands of `total / count` are integers, so C# performs integer division and produces 3 before converting the result to `double`. The displayed average is therefore 3 instead of 3.5.
