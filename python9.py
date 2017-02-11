m1=int(input("sub1="))
m2=int(input("sub2="))
m3=int(input("sub3="))
m4=int(input("sub4="))
m5=int(input("sub5="))
sum=m1+m2+m3+m4+m5
mean=sum/5
perc=(sum/500)*100
print (mean)
if perc<35:
  print("pass")
else:
  print("fail")
