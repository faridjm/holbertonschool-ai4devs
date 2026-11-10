# AI Debug Log

The original buggy files are preserved. Each diagnosis below is based on the original source. Corrected Python and JavaScript copies were executed separately; C# results are expected outcomes pending execution in a .NET environment.

## Bug 1 – bug1.py

**Prompt**: This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it? [Original bug1.py; SyntaxError: expected ':']

**AI Diagnosis**: The `for price in prices` statement lacks a colon. Python requires a colon before the loop body, so parsing fails before `main()` can run.

**Suggested Fix**: Add the missing colon:

```python
for price in prices:
    total += price
```

**Alternative Fixes Tested**: None; one minimal fix was suggested.

**Result**: Executed the corrected script with Python. Exit code 0; output `Total: 40.00`, matching the intended result.

## Bug 2 – bug2.js

**Prompt**: This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it? [Original bug2.js; actual output: Final price: 120]

**AI Diagnosis**: The discount calculation is correct, but adding the discount increases the original price. A 20% discount on 100 should subtract 20, not add it.

**Suggested Fix**: Replace the return statement:

```javascript
return price - discount;
```

**Alternative Fixes Tested**: None; one minimal fix was suggested.

**Result**: Executed the corrected script with Node.js. Exit code 0; output `Final price: 80`, matching the intended result.

## Bug 3 – bug3.cs

**Prompt**: This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it? [Original bug3.cs; requestedId = 3]

**AI Diagnosis**: The dictionary contains keys 1 and 2 only. Accessing `products[requestedId]` with key 3 throws a `KeyNotFoundException`. The dictionary declaration itself is valid.

**Suggested Fix**: Replace the direct lookup with `TryGetValue` so missing products are handled safely:

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

**Alternative Fixes Tested**: None; one minimal fix was suggested.

**Result**: Static review confirms the missing-key path is handled without indexing the dictionary. Expected output for ID 3: `Product not found`; for ID 1: `Keyboard`. Execution pending because the .NET SDK is unavailable in the test environment.

## Bug 4 – bug4.py

**Prompt**: This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it? [Original bug4.py; IndexError: list index out of range]

**AI Diagnosis**: `range(len(items) + 1)` includes index 3 for a three-element list. Valid indices are 0, 1 and 2. Accessing index 3 raises an IndexError.

**Suggested Fix**: Remove the extra iteration:

```python
for index in range(len(items)):
    total += items[index]
```

**Alternative Fixes Tested**: None; one minimal fix was suggested.

**Result**: Executed the corrected script with Python. Exit code 0; output `Sum: 60`, matching the intended result.

## Bug 5 – bug5.cs

**Prompt**: This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it? [Original bug5.cs; total = 7, count = 2]

**AI Diagnosis**: Both operands of `total / count` are integers, so C# performs integer division and truncates 7 / 2 to 3. Conversion to double occurs afterward and cannot restore the lost fraction.

**Suggested Fix**: Cast one operand to double before division:

```csharp
return (double)total / count;
```

**Alternative Fixes Tested**: None; one minimal fix was suggested.

**Result**: Static review confirms floating-point division will preserve the fractional part. Expected numeric result: 3.5 (console formatting may vary by culture). Execution pending because the .NET SDK is unavailable in the test environment.
