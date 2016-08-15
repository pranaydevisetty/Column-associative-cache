#Pranay D.L.V.N.S,K
#Homework6
file=open("D:/Computer architecture/assignment6/extracredit2/tracer","r") #the trace given is read and is stored in file variable
#filew=open("tracew2.txt","w")
add=file.readlines() #here the file is stored in the form of list in the add variable
#print(len(add))
add1=[] #created other list add1
for i in range(len(add)):
    add1.append(bin(int(add[i][2:],16))[2:]) #converting the hexadecimal addreses to binary
    add1[i]=add1[i].zfill(32) #padding zeroes to make each address 32bits
    #filew.write(add1[i]+"\n")
#filew.close()
#print len(add1)  
c={}                #creating empty cache dictionary
rbit={}             #creating rehashbit dictionary
for i in range(512):
    p=(bin(i))[2:].zfill(9) #converting the indices 0 to 511 to binary
    rbit[p]=1               #initializing the rehash bit to 1 for every index
    c[p]=0                  #hashing cache to every index
#print rbit
l=[]
ind=[]
tag=[]
tagm=[]
hit=0
miss=0
for i in range(len(add1)):
    l.append(add1[i][19:])
    ind.append(l[i][:-4])
    ind[i]=ind[i]
    tag.append(add1[i][0:19])
    tagm.append(tag[i]+ind[i][0]) #creating lists for index and tag
for i in range(len(add1)):
    l1=add1[i][19:] 
    ind1=l1[:-4]    
    tag1=add1[i][0:19] #tag of every address is stored in l1 variable
    tagm1=tag1+ind1[0] #appending the msb bit of the index
    if c[ind1]==tagm1:
        hit=hit+1 #increasing the hit count as hit occurs
        rbit[ind1]=0 #the rehashed bit is changed to 0 according to algorithm
    else:
        if rbit[ind1]==1:
            miss=miss+1 #increasing the misscount as miss occurs
            c[ind1]=tagm1 #data is bring into the cache
            rbit[ind1]=0 #rehash bit is again set to zero
        else:
            if ind1[0]==0:
                ind2="1"+ind1[1:] #flipping the MSB bit if its '0' replacing with '1' according to the hashing(flipping) function
            else:
                ind2="0"+ind1[1:] #flipping the MSB bit if its '1' replacing with '0' according to the hashing(flipping) function
            if c[ind2]==tagm1:
                hit=hit+1         #increasing the hit count as hit occurs in respective condn is satisfied 
                kt=c[ind2]
                c[ind2]=c[ind1]
                c[ind1]=kt        #swapping after the hit occurs between 1st(0-255) addresses and 2nd(256-511) addresses
                rbit[ind1]=1    
            else:
                miss=miss+1    # increasing the miss count as miss occurs oin this situation
                c[ind2]=tagm1  #as its a miss address is fetched to the cache
                kt1=c[ind2]
                c[ind2]=c[ind1]
                c[ind1]=kt1     #swapping after the miss occurs between 1st(0-255) addresses and 2nd(256-511) addresses
                rbit[ind1]=1    #changing the rehash bit to 1
print "Number of misses:"
print miss #printing the number of misses
print "Number of hits:"
print hit  #printing the number of hits
print "miss rate of the column associative cache:"
print (miss/float(miss+hit)) #miss rate is printed


        

