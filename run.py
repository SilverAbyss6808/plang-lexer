
from scr_lexer import get_tokens
import sys

# with open(sys.argv[1]) as f:
f = open('bco_examples/TryEverything.bco')  # switch with above to use cmd; for example: "py scripts/run.py bco_examples/HelloWorld.bco"
code = f.read()
tokens = get_tokens(code)

for token in tokens: print(str(token.value), end=' ')  # test line lol

