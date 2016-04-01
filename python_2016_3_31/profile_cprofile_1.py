#!/usr/bin/env python
import cProfile
import re
cProfile.run('re.compile("foo|bar")', 'stats', 'cumtime')
