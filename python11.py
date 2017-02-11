def intr(p,r,t):
  n=r/t
  d=t*t
  i=(p*((1+n)**(d)))-p
 
a=float(input("principle="))
b=float(input("rate="))
c=int(input("time(in year)="))
print (intr(a,b,c))
