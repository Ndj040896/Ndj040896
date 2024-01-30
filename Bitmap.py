Using the Python language, have the function BitmapHoles(strArr) 
take the array of strings stored in strArr, which will be a 2D matrix 
of 0 and 1's, and determine how many holes, or contiguous regions of 0's, 
exist in the matrix. A contiguous region is one where there is a 
connected group of 0's going in one or more of four directions: up, 
down, left, or right. For example: if strArr is 
["10111", "10101", "11101", "11111"], then this looks like the following matrix: 
1 0 1 1 1
1 0 1 0 1
1 1 1 0 1
1 1 1 1 1 
For the input above, your program should return 2 because
there are two separate contiguous regions of 0's, which create 
"holes" in the matrix. You can assume the input will not be empty. 
Input:"01111", "01101", "00011", "11110"
Output:3
Input:"1011", "0010"
Output:2
"""



ASS.
  def BitmapHoles(strArr):
  matrix ={}
  for i in range(len(strArr)):
   for j in range(len(strArr[i])):
     matrix[(i,j)] = int(strArr[i][j])
  count=0
  hole =set()
  done =set()
  flag =True
  for i in range(len(strArr)):
    for j in range(len(strArr[i])):
       s= [(i,j)]
       while s:
         c = s.pop()
         if c not in done:
           done.add(c)
           if matrix[c] == 0 & c not in hole:
             hole.add(c)
             if flag ==True:
               count += 1
               flag = False
             if c[0] - 1 >= 0 and (c[0]-1,c[1]) not in done:
               s.append((c[0]-1, c[1]))
             if c[0] + 1 < len(strArr) and (c[0]+1, c[1]) not in done:
               s.append((c[0]+1, c[1]))
             if c[1] - 1 >= 0 and (c[0],c[1]-1) not in done:
               s.append((c[0],c[1]-1))
             if c[1] + 1 < len(strArr[c[0]]) and (c[0],c[1]+1) not in done:
               s.append((c[0], c[1]+1)) 
  flag = True
  return count