"""Find the k most frequent words using a min-heap of size k."""
import argparse
import heapq
import re
from pathlib import Path

SAMPLE = Path(__file__).resolve().parent / "sample_text.txt"


def word_counts(text):
    counts = {}
    words = re.findall(r"[a-zA-Z]+", text.lower())
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k_words(text, k):
    if k <= 0:
        return []
    counts = word_counts(text)
    heap = []
    for word, count in counts.items():
        item = (count, word)
        if len(heap) < k:
            heapq.heappush(heap, item)
        elif item > heap[0]:
            heapq.heapreplace(heap, item)
    # On equal counts, words later alphabetically come first.
    return sorted(heap, reverse=True)


def main():
    parser = argparse.ArgumentParser(description="Top-K frequent words using a min-heap")
    parser.add_argument("--file", default=str(SAMPLE), help="Plain-text file to read")
    parser.add_argument("--k", type=int, default=5, help="Number of top words")
    args = parser.parse_args()
    text = Path(args.file).read_text(encoding="utf-8")
    counts = word_counts(text)
    print(f"Total words: {sum(counts.values())}; unique words: {len(counts)}")
    for i, (count, word) in enumerate(top_k_words(text, args.k), start=1):
        print(f"{i}. {word}: {count}")


if __name__ == "__main__":
    main()
