from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # text = open(file_path)

    # return text.read()

    return open(file_path).read()


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """


    words = input_text.split()

    chains = {}


    for index in range(len(words) - 2):

        key_tuple = (words[index], words[index + 1])
        value = [words[index + 2]]

        # chains[key_tuple] = value

        if key_tuple in chains:
            value.append(words[index + 2])
        else:
            chains[key_tuple] = value
            # value = [words[index + 2]]







        # chains[(words[index], words[index + 1])] = values


        # key_tuple = values

        # chains.get((words[index], words[index + 1]), values.append(words[index + 2]))  # check if key in dictionary, if not, make a list.

        # words[index + 2:]# key tuples
    print chains



    # return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
