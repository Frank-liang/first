一： 简单的剖析 
1: python剖析脚本的工具,追踪事件,最基本的
------------------------------------
profile_time.py
profile_trace.py 参考这两个脚本
--------------------------------------
http://oprofile.sourceforge.net/download/   profile 工具的网站
 计数器的统计

 程序运行时间
 Constant time O(1)   就是不管程序的输入的数值是怎么样的，所消耗的时间是一样的
 Linear time O(n)     根输入的数值成正比，输入的数值越大，消耗的时间也越大
 logarithmic time O(log n) 刚开始消耗的时间很多很快，达到一定量的时候，输入多少的数据，时间也是一点点的涨，知道无穷
Linearithmic time – O(nlog n) A particular combination of the previous two orders of execution is the linearithmic time. It grows quickly as soon as the value of x starts increasing
Factorial time – O(n!)  Factorial time is one of the worst execution times we might get out of an algorithm.
It grows so quickly that it is hard to plot.
Quadratic time – O(n^)  Quadratic execution time is another example of a fast growing algorithm. The bigger
the input size, the longer it is going to take (this is true for most complexities, but then
again, specially true for this one). Quadratic execution time is even less efficient that
linearithmic time.

排序 从忧到差 （ Constant time O(1)除外，很多复杂的算法很难实现）
• Logarithmic
• Linear
• Linearithmic
• Quadratic
• Factorial

二  pyhton中的一些剖析的工具
cProfile，剖析整个函数的执行的效率
•  enable(): This starts collecting profiling data
• disable(): This stops collecting profiling data
• create_stats(): This stops collecting data and records the information
gathered as the current profile
• print_stats(sort=-1): This creates a stats object and prints the result
into STDOUT
• dump_stats(filename): This writes the content of the current profile
into a file
• run(cmd): This is same as the run function we saw earlier
• runctx(cmd, globals, locals): This is same as the runctx function we
saw earlier
• runcall(func, *args, **kwargs): This gathers profiling information
about the function called

命令 剖析已经写好的脚本
python -m cProfile your_script.py -o your_script.profile

另一个剖析的工具   pstats
  利用一个缓存的技术，是脚本的执行的时间 成倍的提高
  例如：
        class cached:
            def __init__(self, fn):
                self.fn = fn
                self.cache = {}
            def __call__(self, *args):
                try:
                    return self.cache[args]
                except KeyError:
                    self.cache[args] = self.fn(*args)
                    return self.cache[args]

这两个工具 可以结合的用  参考 test.py

cProfile pstats 这两个工具 主要的功能在于统计函数的时间和调用的其他的函数



line_profiler，一句一句的剖析代码，查看每一行代码的效率
yum install python-dev libxml2-dev libxslt-dev
pip install line_profiler

kernprof -l -v script_to_profile.py
python -m line_profiler stats_file.py.lprof

可以调用API执行 如： line_profiler_1.py 

70页



