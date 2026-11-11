Fix Validation
Bug 1 – bug1_fixed.py
- Input: [12.5, 20.0, 7.5]
- Expected Output: Total: 40.00
- Actual Output: Total: 40.00
- Fix Confirmation: PASS. Adding the missing colon to the for statement resolves the syntax error. The script runs successfully and prints the correct total.
- Manual Tweaks: None.
Bug 2 – bug2_fixed.js
- Input: price = 100, percent = 20
- Expected Output: Final price: 80
- Actual Output: Final price: 80
- Fix Confirmation: PASS. Subtracting the discount instead of adding it produces the correct discounted price. The program runs successfully and prints the expected output.
- Manual Tweaks: None.
Bug 3 – bug3_fixed.cs
- Input: Dictionary containing ID 1 (Keyboard) and ID 2 (Mouse); requestedId = 3.
- Expected Output: Product not found
- Actual Output: Product not found
- Fix Confirmation: PASS. Using TryGetValue instead of direct dictionary indexing handles the missing key without throwing a KeyNotFoundException. The program runs successfully and prints the expected message.
- Manual Tweaks: None.
Bug 4 – bug4_fixed.py
- Input: [10, 20, 30]
- Expected Output: Sum: 60
- Actual Output: Sum: 60
- Fix Confirmation: PASS. Changing the loop to range(len(items)) prevents the out-of-range access. The script runs without an IndexError and prints the correct sum.
- Manual Tweaks: None.
Bug 5 – bug5_fixed.cs
- Input: total = 7, count = 2
- Expected Output: Average: 3.5
- Actual Output: Average: 3.5
- Fix Confirmation: PASS. Casting total to double before division prevents integer truncation. The program runs successfully and prints the correct fractional average.
- Manual Tweaks: None.