def Pyramid(N, ar):
 a=[]
 height = 240
 for i in ar:
     a.append(min(i))
 a.sort()
for i in range(len(a)):
      if a[i] > height:
         height = height+1
retun height

if ___name___ == 'main':
     N = 5000
     ar = [[1,1], [2,2], [3,3], [4,4]]
     print(" Height Of Pyramid is: ",Pyramid(N, ar))