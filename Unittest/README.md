# Unit Testing

## Tasks Overview
Python Unit Testing (Criterion U1).

### Included Files
* **`recursive_json_search.py`**: The function.
* **`test_json_search.py`**: The test.

---

## 🎓 Exam Prep: Concepts & Explanations

### 1. What is Unit Testing?
Testing individual "units" (functions) of code in isolation to ensure they work as expected before putting them into a larger system.

### 2. What is Recursion?
In `recursive_json_search.py`, the function calls *itself*.
* It looks at a JSON object. If it finds a list inside, it calls itself to search inside that list. It keeps digging deeper until it finds the key or runs out of data.

### 3. What is `assert`?
In `test_json_search.py`, `self.assertEqual(a, b)` checks if `a` is exactly the same as `b`. If they are different, the test fails, and Python screams at you.