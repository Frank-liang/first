import line_profiler
import sys

def test():
    for i in range(0, 10):
        print i**2
    print "End of the function"

prof = line_profiler.LineProfiler(test) #pass in the function to profile
prof.enable() #start profiling
test()
prof.disable() #stop profiling
prof.print_stats(sys.stdout) #print out the results
