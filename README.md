# Top-K Frequent Words

**Category:** Heap Algorithms  
**Language:** Python 3 (standard library only)

## Idea
Read a text file and find the `k` most frequent words. Instead of sorting every distinct word, I keep a **min-heap of size k**.

## Steps
1. Convert text to lowercase and count the words in a dictionary.
2. Insert `(count, word)` into a min-heap while it contains fewer than k entries.
3. If the heap is full and a new `(count, word)` is larger than its root, replace the root.
4. Sort just the final k entries for display.

Words are English alphabetic tokens. If two words have the same count, the word that comes **later** alphabetically is preferred (a simple deterministic rule for this demo).

## Run
```bash
python main.py
python main.py --file sample_text.txt --k 3
python -m unittest -v
```

## Complexity
If the text has `t` words and `u` unique words: counting is **O(t)**, scanning distinct words with the heap is **O(u log k)**, and output sorting is **O(k log k)**. Memory: **O(u + k)** for the dictionary and heap.
