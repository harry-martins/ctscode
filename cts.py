# your code goes here
m=int(input())
n=int(input())
count=0
temp=n
while(temp!=0):
	temp=temp//10
	count+=1
#print(count)
if(count==3):
	for i in range(m,n+1):
		if(i<10):
			print("00"+str(i),end=" ")
		if i>=10 and i<100:
			print("0"+str(i),end=" ")
		if i>=100 and i<1000:
			print(i,end=" ")
elif(count==2):
	for i in range(m,n+1):
		if(i<10):
			print("0"+str(i),end=" ")
		else:
			print(i,end=" ")
elif count==1:
	for i in range(m,n+1):
		if(i<10):
			print(i,end=" ")
