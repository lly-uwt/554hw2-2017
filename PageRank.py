import numpy, pandas

print('Program Starts\n')
beta = .85  # Dampening factor

# Inputs into pandas
graphFile = open('graph.txt', 'r')
adjList = []
df = pandas.DataFrame(columns=list('ABC'))
for line in graphFile.readlines():
  line = line.replace('\t', ' ').replace('\n', '')
  adjList.append(line.split())
adjList_df = pandas.DataFrame(adjList, columns=['A', 'B', 'C'])

# Count nodes, # of nodes = matrix size
a_uni = adjList_df.A.unique()
b_uni = adjList_df.B.unique()
labels = sorted(list(set(a_uni) | set(b_uni)))

matrix_df = pandas.DataFrame(index=labels, columns=labels).fillna(0.0)
count = adjList_df.groupby(['A']).size()
for index, row in adjList_df.iterrows():
  matrix_df.at[row['B'], row['A']] = (1 / count[row['A']]) # down to left

# contruct vector
vector_df = pandas.Series(1/len(labels), index=labels)
surfer = (1-beta)/len(labels)
iter = 0

# print(matrix_df , '\n')
# print(vector_df , '\n')
# print(surfer  , '\n')

def PageRank(old_v):
  global iter 
  iter += 1
  new_v =  beta * matrix_df.dot(old_v) + surfer
  if numpy.allclose(new_v, old_v, rtol=1e-06, atol=1e-06):
    return new_v
  else:
    return PageRank(new_v)

print('Beta =', beta)
print('(a) What is the output for Matrix M? Give the matrix.\n', matrix_df, '\n', sep='')
print('(b) What is the original rank vector (rj)?\n', vector_df, '\n', sep='')
print('(c) What is the Converged rank vector (R)?\n', PageRank(vector_df), '\n', sep='')
print('(d) How many iterations did it take to get the convergence?\n', iter, '\n', sep='')
print('Program Ended')