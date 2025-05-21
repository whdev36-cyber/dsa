### 🫧 **Bubble Sort – Introduction**

**Bubble Sort** is a simple sorting algorithm that works by repeatedly **swapping adjacent elements** if they are in the **wrong order**. It's called "bubble" sort because smaller elements gradually **bubble up to the top** (beginning) of the list.

---

### 🔁 **How It Works**

For each pass through the array:

* Compare each pair of adjacent elements.
* Swap them if the first is greater than the second.
* Repeat the process until no more swaps are needed.

---

### ⏱️ **Time Complexity**

| Case        | Complexity |                                                                     |
| ----------- | ---------- | ------------------------------------------------------------------- |
| **Best**    | `O(n)`     | When the array is already sorted (optimized with a `swapped` flag). |
| **Average** | `O(n²)`    | Typical case with unsorted elements.                                |
| **Worst**   | `O(n²)`    | When the array is in reverse order.                                 |
| **Space**   | `O(1)`     | In-place sorting (no extra memory needed).                          |

---

### ❗ Pros and Cons

**✅ Pros:**

* Easy to understand and implement.
* Doesn’t require extra space.

**❌ Cons:**

* Very inefficient for large datasets.
* Much slower than more advanced algorithms like Merge Sort or Quick Sort.

---

### 📊 Example

Original: `[5, 3, 8, 4]`
Pass 1: `[3, 5, 4, 8]`
Pass 2: `[3, 4, 5, 8]`
Pass 3: No swaps → done.

