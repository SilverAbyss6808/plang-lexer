
from cls_BcoToken import BcoToken as btk
import re


def get_tokens(code):
    matches = []

    for token in btk.ttypes:
        token_regex = btk.get_by_regex(token)
        match_iter = re.finditer(token_regex, code)

        for match in match_iter:
            token_already_known = False
            for known_token in matches:
                if (match.start() >= known_token.start_location and match.end() <= known_token.end_location):  # or, if it starts and ends inside another token
                    token_already_known = True
                    continue

            if token_already_known == False:
                matches.append(btk(token, match.group(), match.start(), match.end()))    

    sorted_matches = btk.sort_tokens(matches)

    return sorted_matches

f = open('bco_examples/TryEverything.bco')
code = f.read()
tokens = get_tokens(code)

for token in tokens: print(token)

