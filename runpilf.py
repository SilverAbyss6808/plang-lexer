
from scr_lexer import get_tokens
import sys

with open(sys.argv[1]) as f:
# f = open('pilf_ex/ShowXlist.pilf')  # switch with above to use cmd; for example: "py scripts/run.py bco_examples/HelloWorld.bco"
    code = f.read()
    tokens = get_tokens(code)

for token in tokens: print(str(token))  # test line lol

