import sys
from sayings import hello,bye


if len(sys.argv) >= 2:
    bye(sys.argv[1])
