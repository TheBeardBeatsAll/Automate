#! python3

import os
import re

def madLibs(input_file, output_file):
    """lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file
    Args:
        filename (str): name of file to parse
    Returns:
        None
    """
    regex = re.compile(r'(NOUN|ADJECTIVE|ADVERB|VERB)')

    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        # read input file
        content = in_file.read()
        # find matches in content
        matches = regex.findall(content)

        # take in new input & replace
        for found in matches:
            sub = input('Enter a ' + found + ': ')
            content = content.replace(found, sub, 1)

        out_file.write(content)
        print(content)

madLibs('chpt7-11/madLibsData/input.txt', 'chpt7-11/madLibsData/output.txt')