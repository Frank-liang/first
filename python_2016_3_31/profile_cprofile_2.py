#!/usr/bin/env python
import cProfile
def runRe():
    import re
    cProfile.runctx('re.compile("foo|bar")', None, locals())
runRe()
