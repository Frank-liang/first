import cProfile
import pstats
def runRe():
    import re
    re.compile("foo|bar")
prof = cProfile.Profile()
prof.enable()
runRe()
prof.create_stats()
p = pstats.Stats(prof)
p.print_stats(10, 1.0, '.*.py.*')
