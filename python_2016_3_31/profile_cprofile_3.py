#针对于已经写好的代码的剖析
import cProfile
def runRe():
    import re
    re.compile("foo|bar")
prof = cProfile.Profile()
prof.enable()
runRe()
prof.create_stats()
prof.print_stats()
