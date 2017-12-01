## Implementation of PageRank algorithm
Input is a .txt file name *'graph.txt'* that has a graph represent by __adjacency list__ and each numbers is seperated by either tab /t or space (mix would work too)

For example:
![graph.PNG](/graph.PNG)

graph.txt
~~~~
1	2	1
2	3	1
2	4	1
2	5	1
3	2	1
3	4	1
3	5	1
4	2	1
4	3	1
4	5	1
5	2	1
5	3	1
5	4	1
5	6	1
~~~~
or
~~~~
A B 1
B C 1
B D 1
B E 1
C B 1
C D 1
C E 1
D B 1
D C 1
D E 1
E B 1
E C 1
E D 1
E F 1
~~~~

Execute command: `python PageRank.py`

*graph.txt* has to be in the same directory with *PageRank.py*

The beta know as dampening factor for algorithm is __.85__

The precision of numpy.allclose() is __rtol=1e-06, atol=1e-06__

The program will has console output to answers following question:
* (a) What is the output for Matrix M? Give the matrix.
* (b) What is the original rank vector (rj)?
* (c) What is the Converged rank vector (R)?
* (d) How many iterations did it take to get the convergence?

References:

http://www.math.cornell.edu/~mec/Winter2009/RalucaRemus/Lecture3/lecture3.html

https://introcs.cs.princeton.edu/java/16pagerank/





