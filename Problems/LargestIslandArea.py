def findLargestIslandArea(arr):
  """for a two dimensional array
     return an integer representing the area of the largest islan  
  """
  def findAreaAndMark(arr, i, j, nRow, nCol):
    #BFS search
    from collections import deque
    q = deque()
    q.append((i,j))
    marker[i][j] = True
    area = 0
    while (q):
      ii,jj = q.popleft()
      area += 1
      if(ii > 0 and arr[ii - 1][jj] == 1 and marker[ii - 1][jj] == False):
        q.append((ii - 1,jj))
        marker[ii - 1][jj] = True
      if(ii < nRow - 1 and arr[ii + 1][jj] == 1 and marker[ii + 1][jj] == False):
        q.append((ii + 1, jj))
        marker[ii + 1][jj] = True
      if(jj > 0 and arr[ii][jj - 1] == 1 and marker[ii][jj - 1] == False):
        q.append((ii, jj - 1))
        marker[ii][jj - 1] = True
      if(jj < nCol - 1 and arr[ii][jj + 1] == 1 and marker[ii][jj + 1] == False):
        q.append((ii, jj + 1))
        marker[ii][jj + 1] = True
    return area

  nRow = len(arr)
  if (nRow < 1):
    return 0
  nCol = len(arr[0])
  if (nCol < 1):
    return 0

  #helper memory to keep track of whether an element (value == 1) has been processed
  marker = [ [False for i in range(nCol)] for j in range(nRow)  ]
  res = 0

  for iRow in range(nRow):
    for iCol in range(nCol):
      if(arr[iRow][iCol] == 1 and marker[iRow][iCol] == False):
        #unprocessed island
        area = findAreaAndMark(arr, iRow, iCol, nRow, nCol)
        res = max(area, res)
  return res

arr = [
[0, 1, 1, 0],
[0, 0, 0, 1],
[1, 0, 0, 1],
[0, 0, 0, 1],
]
result = 3
assert(findLargestIslandArea(arr) == result)
print "pass test 1"
arr = [
[0, 1, 1, 0],
[0, 0, 0, 1],
]
result = 2
assert(findLargestIslandArea(arr) == result)
print "pass test 2"
arr = [
[0, 1, 1, 0],
[0, 0, 0, 1],
[1, 0, 1, 1],
[0, 0, 1, 1],
[0, 1, 1, 0],
[0, 0, 1, 0],
[0, 0, 1, 1],
[0, 0, 0, 1],
[0, 0, 0, 1],
]
result = 12
assert(findLargestIslandArea(arr) == result)
print "pass test 3"
arr = [
[1, 1, 1, 1],
[1, 1, 1, 1],
[0, 0, 0, 0],
[1, 1, 1, 1],
[1, 0, 0, 1],
[1, 0, 1, 1],
[1, 1, 1, 1],
[0, 0, 0, 1],
[0, 0, 1, 1],
]
result = 16
assert(findLargestIslandArea(arr) == result)
print "pass test 4"
arr = [
[1, 1, 1, 1],
[1, 1, 1, 1],
[1, 1, 1, 1],
[1, 1, 1, 1]
]
result = 16
assert(findLargestIslandArea(arr) == result)
print "pass test 5"
