<h1 align="center">Sequential Search</h1>

## Overview

**Sequential Search**, also called **Linear Search**, is the simplest searching algorithm.

It works by checking each element in the list one by one until the target value is found or the list ends.

It is known for being:

* ✅ Very simple to understand and implement
* ✅ Works on both sorted and unsorted data
* ✅ Requires no preprocessing
* ❌ Slow for large datasets

<a href="/src/main.py">Check out for source code</a>

---

## ⚙️ How Sequential Search Works

1. Start from the first element of the list
2. Compare it with the target value
3. If it matches → return the index
4. Otherwise move to the next element
5. Continue until found or list ends

---

### Example Walkthrough

Search for **7** in the list:

```id="sq1"
[4, 2, 7, 1, 9]
```

**Step-by-step comparisons**

```id="sq2"
4 ≠ 7  
2 ≠ 7  
7 = 7  ✅ Found at index 2
```

---

## ⏱️ Time & Space Complexity

| Case         | Time Complexity |
| ------------ | --------------- |
| Best Case    | O(1)            |
| Average Case | O(n)            |
| Worst Case   | O(n)            |

**Space Complexity:** O(1)

Worst case occurs when the element is not present or is the last item.

---

## 🧠 Python Implementation

```python id="sq3"
def sequential_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


# Example usage
numbers = [4, 2, 7, 1, 9]
print(sequential_search(numbers, 7))
# Output: 2
```

---

## 🧪 Example Runs

### Example 1

Input:

```id="sq4"
Array: [10, 20, 30, 40]
Target: 30
```

Output:

```id="sq5"
Index 2
```

---

### Example 2

Input:

```id="sq6"
Array: [5, 8, 12, 3]
Target: 6
```

Output:

```id="sq7"
-1  (not found)
```

---

## 👍 Advantages

* Very easy to implement
* Works on unsorted data
* No extra memory needed
* Useful for small datasets

---

## 👎 Disadvantages

* Slow for large lists
* Requires checking each element
* Inefficient compared to binary search on sorted data

---

## 📌 When to Use Sequential Search

Use Sequential Search when:

* The dataset is small
* The data is unsorted
* Simplicity is more important than speed
* Searching only occasionally

Common uses include:

* Small lists or arrays
* Simple validation checks
* Searching user inputs

---

## 🏁 Summary

Sequential Search is the most straightforward searching algorithm. While inefficient for large datasets, its simplicity and flexibility make it useful in many small-scale or unsorted-data situations.
