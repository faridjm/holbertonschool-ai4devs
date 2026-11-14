# Fix Validation

The same checks ran against the original snippets and the fixed copies with Python 3.12.14, Node.js 24.22.1, and OpenJDK 21.0.13.

**Results** — 16/24 passed on the original snippets and 24/24 passed on the fixed copies.

The commands below run the included examples from `smart_bug_bounty/bug_fixes/`. The tables also record the boundary checks.

## bug1_fixed.py

- **Original issue.** The slice started one position too late.
- **Fix applied.** Set the start index to `max(0, len(items) - count)`.
- **Test results.** 5/5 passed.
- **Example.** Run `python3 bug1_fixed.py`. Output was `['ruler', 'eraser']`

| Check and expected behavior | Original | Fixed |
| --- | --- | --- |
| Count 2 returns `['ruler', 'eraser']` | Fail | Pass |
| Count 4 returns all four items | Fail | Pass |
| Count 0 returns `[]` | Pass | Pass |
| Count 5 returns all four items | Pass | Pass |
| Count -1 raises `ValueError` | Pass | Pass |

## bug2_fixed.js

- **Original issue.** The search returned `null` on the first mismatch.
- **Fix applied.** Remove the early `return null` inside the loop so the search can reach later products.
- **Test results.** 5/5 passed.
- **Example.** Run `node bug2_fixed.js`. Output was `{ id: 102, name: 'Pencil' }`

| Check and expected behavior | Original | Fixed |
| --- | --- | --- |
| ID 102 returns Pencil | Fail | Pass |
| ID 101 returns Notebook | Pass | Pass |
| ID 103 returns Ruler | Fail | Pass |
| ID 999 returns `null` | Pass | Pass |
| An empty product list returns `null` | Pass | Pass |

## bug3_fixed.java

- **Original issue.** Integer division truncated the fractional part of the mean.
- **Fix applied.** Cast the total to `double` before dividing.
- **Test results.** 5/5 passed.
- **Example.** Run `java bug3_fixed.java`. Output was `8.5`

| Check and expected behavior | Original | Fixed |
| --- | --- | --- |
| Scores `[8, 9]` return `8.5` | Fail | Pass |
| Scores `[7]` return `7.0` | Pass | Pass |
| Scores `[2, 4, 6]` return `4.0` | Pass | Pass |
| Two maximum `int` scores average to the maximum `int` | Pass | Pass |
| An empty array raises `IllegalArgumentException` | Pass | Pass |

## bug4_fixed.py

- **Original issue.** Calls without a task list shared the same mutable default.
- **Fix applied.** Use `None` as the default and create a list when `tasks is None`.
- **Test results.** 4/4 passed.
- **Example.** Run `python3 bug4_fixed.py`. Output was Two lines, `['Read chapter 1']` and `['Review notes']`.

| Check and expected behavior | Original | Fixed |
| --- | --- | --- |
| Two calls without a list return separate one-item lists | Fail | Pass |
| Trim the title and append it to the supplied list | Pass | Pass |
| Append to the same explicitly supplied empty list | Pass | Pass |
| A blank title raises `ValueError` and leaves the list intact | Pass | Pass |

## bug5_fixed.js

- **Original issue.** Default sorting compared the times as strings.
- **Fix applied.** Sort the copy with the numeric comparator `(a, b) => a - b`.
- **Test results.** 5/5 passed.
- **Example.** Run `node bug5_fixed.js`. Output was `{"sortedTimes":[3,8,12,25],"originalTimes":[12,3,25,8]}`

| Check and expected behavior | Original | Fixed |
| --- | --- | --- |
| `[12, 3, 25, 8]` sorts to `[3, 8, 12, 25]` | Fail | Pass |
| Return a separate array and preserve the input order | Pass | Pass |
| `[10, 0, 10, 2]` sorts to `[0, 2, 10, 10]` | Fail | Pass |
| `[]` returns `[]` | Pass | Pass |
| `[7]` returns `[7]` | Pass | Pass |
