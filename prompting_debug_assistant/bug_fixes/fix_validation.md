# Fix Validation

The original buggy files are unchanged. Python 3 and Node.js tests were executed successfully. The two primary C# tests were run on the student’s Windows computer using .NET SDK 10.0.403, and the student confirmed the expected outputs. Additional C# cases remain untested.

## Bug 1 – bug1_fixed.py
- **Fix**: Added the missing colon to the for statement.
- **Input**: `[12.5, 20.0, 7.5]`
- **Expected Output**: `Total: 40.00`
- **Actual Output**: `Total: 40.00`
- **Additional Tests**: Empty list returns 0; `[5]` returns 5. Both assertions passed.
- **Result**: PASS (exit code 0).
- **Manual Tweaks**: None.

## Bug 2 – bug2_fixed.js
- **Fix**: Subtract the discount instead of adding it.
- **Input**: Price 100, discount 20%.
- **Expected Output**: `Final price: 80`
- **Actual Output**: `Final price: 80`
- **Additional Tests**: Price 100 with 0% discount returns 100; with 100% discount returns 0. Both assertions passed.
- **Result**: PASS (exit code 0).
- **Manual Tweaks**: None.

## Bug 3 – bug3_fixed.cs
- **Fix**: Use TryGetValue instead of direct dictionary indexing.
- **Input**: Product ID 3, with keys 1 and 2 in the dictionary.
- **Expected Output**: `Product not found`
- **Actual Output**: `Product not found` (student-confirmed local execution).
- **Additional Test**: Change requestedId to 1 in a temporary copy; expected output `Keyboard`. Not executed (optional additional case).
- **Result**: PASS — primary missing-key test.
- **Manual Tweaks**: None.

## Bug 4 – bug4_fixed.py
- **Fix**: Use range(len(items)) to avoid an out-of-range index.
- **Input**: `[10, 20, 30]`
- **Expected Output**: `Sum: 60`
- **Actual Output**: `Sum: 60`
- **Additional Tests**: Empty list returns 0; `[5]` returns 5. Both assertions passed.
- **Result**: PASS (exit code 0).
- **Manual Tweaks**: None.

## Bug 5 – bug5_fixed.cs
- **Fix**: Cast total to double before division.
- **Input**: total = 7, count = 2.
- **Expected Output**: `Average: 3.5` (decimal separator may vary by culture).
- **Actual Output**: `Average: 3.5` (student-confirmed local execution).
- **Additional Test**: total = 8, count = 2; expected numeric result 4. Not executed (optional additional case).
- **Result**: PASS — primary fractional-average test.
- **Manual Tweaks**: None.
