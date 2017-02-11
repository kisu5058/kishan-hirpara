def intr(p,r,t):
  i=(p*r*t)/100
  print("interest=",i)
 
p=float(input("principle="))
r=float(input("rate="))
t=int(input("time(in year)="))
print (intr(p,r,t))
