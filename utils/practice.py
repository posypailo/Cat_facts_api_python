def reverse_long_words(sentence: str) -> str:
    if not isinstance(sentence, str):
        raise TypeError
    words = sentence.split(" ")
    reversed_words = [''.join(reversed(word)) if len(word) > 3 else word for word in words]
    return ' '.join(reversed_words)


# print(reverse_long_words("This is a test"))


def reverse_long_words1(sentence: str) -> str:
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")

    words = sentence.split()

    reversed_words = [
        word[::-1] if len(word) > 3 else word
        for word in words
    ]

    return ' '.join(reversed_words)


def remove_duplicates(integers: list[int]) -> list[int]:
    if not isinstance(integers, list):
        raise TypeError("Input must be a list.")

    # no_duplicates = list(set(integers))
    no_duplicates = list(dict.fromkeys(integers))
    sorted_integers = sorted(no_duplicates)

    return sorted_integers


remove_duplicates([4, 5, 2, 2, 4, 7, 8, 7])

# highest_scorer({"Alice": 85, "Bob": 92, "Charlie": 88})
# Output: "Bob"


def highest_scorer(students: dict) -> str:
    if not isinstance(students, dict):
        raise TypeError("Input must be a dict.")

    return max(students, key=students.get)


print(highest_scorer({"Alice": 85, "Bob": 92, "Charlie": 88}))
