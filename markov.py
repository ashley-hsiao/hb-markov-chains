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
        # chains[key] = chains.get(key, [])

import random 

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    current_key = random.choice(chains.keys())

    text = current_key[0] + current_key[1]

    # chains.items() returns a list that contains tuples, in which each tuple contains a tuple (key) and a list (value).
    # loops through each key and gets a random word
    # key is then rebinded to second word in key and the chosen word, then this key loops through dict to get the next random word and concatenated to the text

    while current_key != ('Sam', 'I'):
        for key, value in chains.items():
            if key == current_key:
                chosen_word = random.choice(value)
                # print "Key inside: ", key
                # print "Word inside: ", chosen_word
                current_key = (current_key[1], chosen_word)
                text += chosen_word
                
                print "First key: ", key
                print "Chosen word: ", chosen_word
                print "Second key: ", current_key


    print "Text: ", text
        # for key, value in chains.items():
        #     if key == new_key:
        #         chosen_word = random.choice(value)
        #         new_key = (new_key[1], chosen_word)

        #         print "Rebinded key: ", new_key

    # print "Current key: ", current_key
    # print "Chosen word: ", chosen_word

    

    #     text += key[1] + ' ' + random.choice(value) + ' '
    
    # print text
    # return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
