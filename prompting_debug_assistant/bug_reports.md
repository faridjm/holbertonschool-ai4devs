# Bug Reports

This report summarizes five bugs, their root causes, AI-assisted resolutions, and lessons learned. The original buggy snippets are preserved in `bug_snippets/`; corrected versions are stored in `bug_fixes/`. AI proposed the code fixes, and the fixes were applied to separate files. No additional manual changes to the fix logic were required. The C# runtime checks were performed locally by the student.

## Bug Report – bug1.py

- **File Name**: `bug1.py` (corrected: `bug1_fixed.py`).
- **Summary**: The script cannot calculate the total of a list of prices because it contains a syntax error.
- **Root Cause**: The `for` statement is missing the colon required by Python's compound-statement syntax. Python raises a `SyntaxError` before executing the program.
- **Resolution**: AI suggested adding the missing colon. The suggestion was applied to the corrected file without further manual edits. The list `[12.5, 20.0, 7.5]` produces `Total: 40.00` after the fix.
- **Lesson Learned**: Check language syntax before investigating runtime behavior. A syntax error prevents the program from executing, even when the intended calculation is correct.

Before:
```python
for price in prices
    total += price
```

After:
```python
for price in prices:
    total += price
```

## Bug Report – bug2.js

- **File Name**: `bug2.js` (corrected: `bug2_fixed.js`).
- **Summary**: The discount calculation increases the product price instead of reducing it.
- **Root Cause**: The discount amount is added to the original price rather than subtracted. The code executes successfully but implements the wrong business rule.
- **Resolution**: AI suggested replacing addition with subtraction. The corrected file uses the suggested expression without further manual edits. A price of 100 with a 20% discount produces `Final price: 80` instead of 120.
- **Lesson Learned**: Successful execution does not guarantee correct business logic. Verify calculations against known expected results and boundary cases such as 0% and 100% discounts.

Before:
```javascript
return price + discount;
```

After:
```javascript
return price - discount;
```

## Bug Report – bug3.cs

- **File Name**: `bug3.cs` (corrected: `bug3_fixed.cs`).
- **Summary**: Looking up a product ID that does not exist causes an unhandled runtime exception.
- **Root Cause**: Direct dictionary indexing with `products[requestedId]` throws `KeyNotFoundException` when the requested key is absent. The dictionary contains IDs 1 and 2, but the program requests ID 3.
- **Resolution**: AI suggested using `TryGetValue` to check for the key and retrieve its value in one operation. The corrected file prints the product name when found and `Product not found` otherwise. No further manual edits to the fix logic were needed. The student confirmed both the missing-key test (ID 3) and the existing-key test (ID 1, `Keyboard`) using .NET SDK 10.0.403. The latter was tested in a temporary copy.
- **Lesson Learned**: Do not assume a requested key exists in a collection. Use safe lookup methods and explicitly handle expected missing-data scenarios instead of allowing avoidable exceptions.

Before:
```csharp
Console.WriteLine(products[requestedId]);
```

After:
```csharp
if (products.TryGetValue(requestedId, out var productName))
{
    Console.WriteLine(productName);
}
else
{
    Console.WriteLine("Product not found");
}
```

## Bug Report – bug4.py

- **File Name**: `bug4.py` (corrected: `bug4_fixed.py`).
- **Summary**: The list-summing function attempts to access an element beyond the end of the list.
- **Root Cause**: `range(len(items) + 1)` includes index `len(items)`, but the last valid index of a nonempty Python list is `len(items) - 1`. The extra iteration raises `IndexError`.
- **Resolution**: AI suggested changing the loop to `range(len(items))`. The suggested fix was applied without further manual edits. The input `[10, 20, 30]` produces `Sum: 60`. Empty-list and single-element cases were also checked successfully.
- **Lesson Learned**: Understand inclusive and exclusive loop boundaries. Test empty collections and single-element collections to detect off-by-one errors early.

Before:
```python
for index in range(len(items) + 1):
    total += items[index]
```

After:
```python
for index in range(len(items)):
    total += items[index]
```

## Bug Report – bug5.cs

- **File Name**: `bug5.cs` (corrected: `bug5_fixed.cs`).
- **Summary**: The average calculation loses the fractional part of its result.
- **Root Cause**: Both operands of `total / count` are integers, so C# performs integer division before converting the result to `double`. For example, 7 divided by 2 becomes 3 rather than 3.5.
- **Resolution**: AI suggested casting `total` to `double` before division so that floating-point division is performed. The corrected file uses this expression without further manual edits. The student confirmed `Average: 3.5` for total 7 and count 2, and `Average: 4` for total 8 and count 2 using a temporary test copy for the second case.
- **Lesson Learned**: The return type does not determine how an arithmetic expression is evaluated. Check operand types and perform necessary conversions before arithmetic operations. Test fractional as well as whole-number results.

Before:
```csharp
return total / count;
```

After:
```csharp
return (double)total / count;
```
