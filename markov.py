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

        key = (words[index], words[index + 1])
        value = words[index + 2]

        # Lines 43 - 57, semantic error 
        # if key not in chains:
        #     values = []
        #     chains[key] = values
        #     print "ID before: ", id(values)
        #     # print "ID chains[key]: ", id(chains[key])
        #     print key, "has empty list: ", chains[key]
        #     values.append(value)
        #     print "ID after: ", id(values)
        #     print key, "has list of 1 value: ", chains[key]


        # else:
        #     values.append(value)
        #     print key, "just added", value, "now consists of: ", chains[key]
        #     print "ID key exists: ", id(values)


    # print chains
    # return chains


    # WORKING CODE

        if key not in chains:
            chains[key] = []
            # print key, "has empty list: ", chains[key]
            chains[key].append(value)
            # print key, "has list of 1 value: ", chains[key]
        else:
            chains[key].append(value)
            # print key, "just added", value, "now consists of: ", chains[key]
 

    print chains 
    return chains

        # Below code is same as above, but logic is reversed (else statement read first)

        # if key in chains:
        #     chains[key].append(value) 

        # else:
        #     chains[key] = []  
        #     chains[key].append(value)


        # Below code is what we tried first time around, but values not linked to key and is outside of if/else statement so resets each iteration

        # values = []
        # chains[key] = value

        # if key in chains:
        #     values.append(value)
        # else:
        #     values.append(value)
        #     chains[key] = values
        #     # value = [words[index + 2]]


        # .setdefault code below works same as if/else statement above, but not understanding why .get does not work and returns empty dictionary {}

        # chains.setdefault(key, []).append(value)
        # chains.get(key, []).append(value) 


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
