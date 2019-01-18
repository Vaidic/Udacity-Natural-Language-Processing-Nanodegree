'''
    File name: test
    Author: Vaidic Joshi
    Date created: 17-Jan-19
    Python Version: 3.0
'''

"""Count words."""
import collections
import re


def count_words(text):
    """Count how many times each unique word occurs in text."""
    return collections.Counter(re.sub(r"[^a-zA-Z0-9]", " ", text.lower()).split())


def test_run():
    # with open("input.txt", "r") as f:
    #     text = f.read()
    counts = count_words('The hammer!!! and the nail.')
    sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)

    print("10 most common words:\nWord\tCount")
    for word, count in sorted_counts[:10]:
        print("{}\t{}".format(word, count))

    print("\n10 least common words:\nWord\tCount")
    for word, count in sorted_counts[-10:]:
        print("{}\t{}".format(word, count))


if __name__ == "__main__":
    test_run()
