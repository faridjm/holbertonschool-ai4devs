# Fix Validation

All five corrected snippets were validated. Python 3 and Node.js results are from executed tests; C# results are from student-confirmed local execution with .NET SDK 10.0.403. Original buggy files were preserved.

## Bug 1 -- bug1_fixed.py

**Fix**: Added the missing colon to the for statement.

### Test 1

-   **Input**: List of prices: `[12.5, 20.0, 7.5]`
-   **Expected Output**: `Total: 40.00`
-   **Actual Output**: `Total: 40.00`
-   **Result**: PASS --- actual output matches expected output.

### Test 2

-   **Input**: Empty list: `[]`
-   **Expected Output**: `0`
-   **Actual Output**: `0`
-   **Result**: PASS --- actual output matches expected output.

### Test 3

-   **Input**: Single price: `[5]`
-   **Expected Output**: `5`
-   **Actual Output**: `5`
-   **Result**: PASS --- actual output matches expected output.

**Fix Confirmation**: PASS --- all listed tests passed.

**Manual Tweaks**: None beyond the AI-suggested fix.

## Bug 2 -- bug2_fixed.js

**Fix**: Subtract the discount from the original price.

### Test 1

-   **Input**: Price 100, discount 20%
-   **Expected Output**: `Final price: 80`
-   **Actual Output**: `Final price: 80`
-   **Result**: PASS --- actual output matches expected output.

### Test 2

-   **Input**: Price 100, discount 0%
-   **Expected Output**: `100`
-   **Actual Output**: `100`
-   **Result**: PASS --- actual output matches expected output.

### Test 3

-   **Input**: Price 100, discount 100%
-   **Expected Output**: `0`
-   **Actual Output**: `0`
-   **Result**: PASS --- actual output matches expected output.

**Fix Confirmation**: PASS --- all listed tests passed.

**Manual Tweaks**: None beyond the AI-suggested fix.

## Bug 3 -- bug3_fixed.cs

**Fix**: Use TryGetValue to handle missing keys safely.

### Test 1

-   **Input**: Dictionary `{1: "Keyboard", 2: "Mouse"}`, requested ID 3
-   **Expected Output**: `Product not found`
-   **Actual Output**: `Product not found`
-   **Result**: PASS --- actual output matches expected output.

### Test 2

-   **Input**: Same dictionary, requested ID 1 (temporary test copy)
-   **Expected Output**: `Keyboard`
-   **Actual Output**: `Keyboard`
-   **Result**: PASS --- actual output matches expected output.

**Fix Confirmation**: PASS --- all listed tests passed.

**Manual Tweaks**: None beyond the AI-suggested fix.

## Bug 4 -- bug4_fixed.py

**Fix**: Use range(len(items)) to avoid an out-of-range index.

### Test 1

-   **Input**: List `[10, 20, 30]`
-   **Expected Output**: `Sum: 60`
-   **Actual Output**: `Sum: 60`
-   **Result**: PASS --- actual output matches expected output.

### Test 2

-   **Input**: Empty list: `[]`
-   **Expected Output**: `0`
-   **Actual Output**: `0`
-   **Result**: PASS --- actual output matches expected output.

### Test 3

-   **Input**: Single item: `[5]`
-   **Expected Output**: `5`
-   **Actual Output**: `5`
-   **Result**: PASS --- actual output matches expected output.

**Fix Confirmation**: PASS --- all listed tests passed.

**Manual Tweaks**: None beyond the AI-suggested fix.

## Bug 5 -- bug5_fixed.cs

**Fix**: Cast total to double before division.

### Test 1

-   **Input**: total = 7, count = 2
-   **Expected Output**: `Average: 3.5`
-   **Actual Output**: `Average: 3.5`
-   **Result**: PASS --- actual output matches expected output.

### Test 2

-   **Input**: total = 8, count = 2 (temporary test copy)
-   **Expected Output**: `Average: 4`
-   **Actual Output**: `Average: 4`
-   **Result**: PASS --- actual output matches expected output.

**Fix Confirmation**: PASS --- all listed tests passed.

**Manual Tweaks**: None beyond the AI-suggested fix.

## Summary

All 13 documented test cases passed across the five corrected files. The additional C# cases used temporary copies with modified input values; the repository source files were not changed for those tests.
