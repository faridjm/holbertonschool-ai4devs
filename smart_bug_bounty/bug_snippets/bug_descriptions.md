# Bug Descriptions

## bug1.py

- **Intended behavior:** Return the last `count` items in their original order. Return an empty list for zero and all items if `count` exceeds the list length. Reject negative counts.
- **Current issue:** An off-by-one error moves the slice start one position too far. The included example returns `['eraser']` instead of `['ruler', 'eraser']`.
- **Run:** `python3 bug1.py`

## bug2.js

- **Intended behavior:** Return the product with the requested ID, or `null` if no product matches.
- **Current issue:** The search returns `null` after the first non-matching product. The included example should return the Pencil with ID `102` but prints `null`.
- **Run:** `node bug2.js`

## bug3.java

- **Intended behavior:** Return the arithmetic mean of a non-empty array of integer scores, including the fractional part. Reject empty arrays.
- **Current issue:** Integer division discards the fractional part before the result is converted to `double`. The included example prints `8.0` instead of `8.5`.
- **Run:** `java bug3.java`

## bug4.py

- **Intended behavior:** Trim the task title and add it to the supplied list. When no list is supplied, start a fresh list on each call. Reject blank titles.
- **Current issue:** Python reuses the mutable default list. The second call prints `['Read chapter 1', 'Review notes']` instead of `['Review notes']`.
- **Run:** `python3 bug4.py`

## bug5.js

- **Intended behavior:** Return delivery times in ascending numeric order while preserving the original array.
- **Current issue:** The default sort compares string representations. The included example returns `[12,25,3,8]` instead of `[3,8,12,25]`.
- **Run:** `node bug5.js`
