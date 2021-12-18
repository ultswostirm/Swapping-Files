def swapfile():
     i1=input("Enter first file name-> ")
     i2=input("Enter second file name-> ")
     #File1
     a=open(i1,"r")
     dataA=a.read()
     #File2
     b=open(i2,"r")
     dataB=b.read()
     #Swap1
     a=open(i1,"w")
     a.write(dataB)
     #Swap2
     b=open(i2,"w")
     b.write(dataA)
     
     
swapfile()