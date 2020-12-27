grades=[[50,90,60],[15,60,75],[99,95,91]]
av=[]
for i in range(3):
  m1=grades[i,0]
  m2=grades[i,1]
  f=grades[i,2]
  average=m1*0,3+m2*0,3+f*0,4
  av.append(average)
print(av)