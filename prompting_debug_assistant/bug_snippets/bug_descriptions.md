# Bug Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Sum a list of prices and print the total as 40.00.  
**Issue Type**: Syntax error.  
**Notes**: The for statement is missing a colon, preventing the script from running.

## Bug 2 – bug2.js
**Intended Behavior**: Apply a percentage discount to a product price. A 20% discount on 100 should return 80.  
**Issue Type**: Logical error.  
**Notes**: The discount is added to the original price instead of being subtracted.

## Bug 3 – bug3.cs
**Intended Behavior**: Look up a product by ID and display its name, or report that the product was not found.  
**Issue Type**: Runtime exception.  
**Notes**: Looking up ID 3 directly in the dictionary throws KeyNotFoundException because the key does not exist.

## Bug 4 – bug4.py
**Intended Behavior**: Sum all items in a list and return 60 for [10, 20, 30].  
**Issue Type**: Off-by-one error.  
**Notes**: The loop includes index len(items), which is outside the valid range and raises IndexError.

## Bug 5 – bug5.cs
**Intended Behavior**: Calculate an average with fractional precision. Dividing 7 by 2 should return 3.5.  
**Issue Type**: Data type misuse.  
**Notes**: Integer division truncates the result to 3 before conversion to double.
