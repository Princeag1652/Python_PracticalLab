import re
from collections import defaultdict, Counter


# 1. Clean text by removing spaces and punctuation
def clean_text(text):
    return re.sub(r"[^a-z0-9]", "", text.lower())


# 2. Find anagram groups using sorted characters
def find_anagram_pairs(words):
    groups = defaultdict(list)

    for word in words:
        cleaned = clean_text(word)
        if cleaned:
            key = "".join(sorted(cleaned))
            groups[key].append(word)

    return [
        tuple(group)
        for group in groups.values()
        if len(group) > 1
    ]


# 3. Find anagram groups using character counts
def find_anagram_pairs_count(words):
    groups = defaultdict(list)

    for word in words:
        cleaned = clean_text(word)
        if cleaned:
            # Immutable tuple key for dictionary lookup
            key = tuple(sorted(Counter(cleaned).items()))
            groups[key].append(word)

    return [
        tuple(group)
        for group in groups.values()
        if len(group) > 1
    ]


# 4. Match words against a pattern
# ? matches exactly one character
# * matches zero or more characters
def find_pattern_matches(words, pattern):
    pattern = clean_text(pattern)
    regex = "^" + re.escape(pattern) + "$"
    regex = regex.replace(r"\?", ".").replace(r"\*", ".*")

    return [
        word for word in words
        if re.fullmatch(regex, clean_text(word))
    ]


# 5. Main program
if __name__ == "__main__":

    words = [
        "listen", "silent", "enlist",
        "google", "googel",
        "abc", "bca", "cab",
        "python", "typhon",
        "night", "thing",
        "cat", "act", "tac",
        "dog", "god", "odg",
        "123", "321", "312",
        "hello", "world", "low", "owl", "rowl"
    ]

    print("--- Anagram Groups (Using Sorted String) ---")
    pairs = find_anagram_pairs(words)

    for i, pair in enumerate(pairs, 1):
        print(f"{i}. {pair}")

    print("\n--- Anagram Groups (Using Character Count) ---")
    pairs_count = find_anagram_pairs_count(words)

    for i, pair in enumerate(pairs_count, 1):
        print(f"{i}. {pair}")

    pattern = "??t"
    print(f"\n--- Pattern Matches (pattern: '{pattern}') ---")
    matches = find_pattern_matches(words, pattern)
    print("Matches:", matches)
