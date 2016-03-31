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
cProfile
29页开始

