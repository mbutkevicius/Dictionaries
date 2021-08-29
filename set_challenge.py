# Geez this took a long time but I finally figured it out.
# I wasn't using a frozen set and I wasn't setting up my set right either.
# Sets have to be like {"z", "b", "d",} not {"zbd"}
# So anyways, here's two solutions. One is a function and one isn't. (Obviously comment one out to get it to work)

def consonant(phrase: str) -> None:
    """
    Take all the consonants from a phrase and list them in alphabetical order.
    :param phrase: `str` input to be sorted
    :return: Return all the consonants in alphabetical order.
    """
    consonant_set = frozenset("bcdfghjklmnpqrstvwxyz")
    result = sorted(consonant_set.intersection(phrase))
    print(set(result))


words = input("Please enter a phrase to be checked: ").casefold()
consonant(words)


consonant_set = frozenset("bcdfghjklmnpqrstvwxyz")
words = input("Please enter a phrase to be checked: ").casefold()
consonants = set()
for letter in words:
    if letter in consonant_set:
        consonants.add(letter)
print(sorted(consonants))


# This is just crap that I couldn't get to work

# consonant_set = frozenset("bcdfghjklmnpqrstvwxyz")
# alphanumeric_set = frozenset("abcdefghijklmnopqrstuvwxyz1234567890")
# consonants = set()
# words = input("Please enter a phrase to be checked: ")
# for char in words:
#     if char in alphanumeric_set.intersection(consonant_set):
#         consonants.add(alphanumeric_set.intersection(consonant_set))
# print(consonants)

# sample_text = "Python is a very powerful language"
#
# vowels = frozenset("aeiou")
