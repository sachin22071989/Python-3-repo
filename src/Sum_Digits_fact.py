Num=int(input("Enter any number:"));
Sum=0;
while(Num>0):
	Digit=Num%10;
	Num=Num//10;
	if (Digit==0):
	   continue;
	Fact=1;
	for i in range(1,Digit+1):
	    Fact=Fact*i;
	Sum=Sum+Fact;
	
print("Sum of factorial of individual digits is:", Sum);

	