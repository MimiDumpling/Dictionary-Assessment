"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    unique_words = {}

    split_phrase = phrase.split(" ")

    for word in split_phrase:
        if unique_words.get(word) == None:
            unique_words[word] = 1
        else:
            unique_words[word] += 1

    return unique_words


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    melons = {
        "Watermelon": 2.95,
        "Cantaloupe": 2.50,
        "Musk": 3.25,
        "Christmas": 14.25
    }

    if melon_name in melons:
        return melons[melon_name]
    else:
        return "No price found"


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """

    length_of_words = {}

    for word in words:
        length = len(word)

        if length_of_words.get(length) == None:
            length_of_words[length] = [word]
       
        else:
            length_of_words[length].append(word)
            length_of_words[length].sort()

    return sorted(length_of_words.items())


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    translation = {
            "sir": "matey",
            "hotel": "fleabag inn",
            "student": "swabbie",
            "man": "matey",
            "professor": "foul blaggart",
            "restaurant": "galley",
            "your": "yer",
            "excuse": "arr",
            "students": "swabbies",
            "are": "be",
            "restroom": "head",
            "my": "me",
            "is": "be"
        }

    split_phrase = phrase.split(" ")
    translated_list = []

    for word in split_phrase:
        if word in translation:
            word = translation[word]
            translated_list.append(word)
        else:
            translated_list.append(word)

    return " ".join(translated_list)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # Holy cow. This is a super fun and challenging puzzle. I spent
    # about 2 hrs on it (while only 1 hr for all the previous problems)
    # and I think I should stop. BUT I WANNA SOLVE IT! But, it's time to
    # move on to the classes assessment. I hope whoever is reading this
    # can make some sense of what I was trying to do below. :) Thanks! 

    # # dict only has unique keys
    # # this will help check if we've already used the word
    # words_already_used = {}
    # solved = []
    # index = 0

    # # keeps loop going until all possible words exhausted
    # # ? while True: ?
    # if index < (len(names) - 1):
    #     for word in names:
    #         print "word at first for loop:" + word

    #         # first word will always go into solution
    #         # kicks off the puzzle
    #         if solved == []:
    #             solved.append(word)
    #             words_already_used[word] = index

    #         word_split = list(word)
    #         last_letter = word_split[-1]

    #         # moves loop to next word in list
    #         # why isn't it giving back the very next word??
    #         for other_word in names:
    #             other_word_split = list(other_word)
    #             first_letter = other_word_split[0]

    #         print "word:" + word
    #         print "solved:" + str(solved)
    #         print words_already_used
    #         print "last_letter:" + last_letter
    #         print "other_word:" + other_word
    #         print "first_letter:" + first_letter
    #         print "============"

    #     index += 1     
            

    #     #         if last_letter == first_letter:
    #     #             # checks if we've already used this word
    #     #             if words_already_used.get(other_word) == None:
    #     #                 solved.append(word)
    #     #                 words_already_used[other_word] = (index + 1)

    #     #             print words_already_used

    #     #                 # else:
    #     #                 #     # if no more words available because we're back to our word
    #     #                 #     # if our word has looped all the way around and ends up 
    #     #                 #     # at the same index
    #     #                 #     if index == words_already_used[word].keys():
    #     #                 #         return solved 
    #     #                 #     else:
    #     #                 #         continue

    #     # # even if loop reaches end, but needs to keep looking, the index will let
    #     # # it keep looping, instead of ending on last item of list                 
    #     # elif index == (len(names) - 1):
    #     #     index = 0
    #     # index += 1

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
